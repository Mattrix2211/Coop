from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Category(models.Model):
	name = models.CharField("Nom", max_length=150, unique=True)
	description = models.CharField("Description", max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Catégorie"
		verbose_name_plural = "Catégories"
		ordering = ["name"]

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name="products", verbose_name="Catégorie")
	name = models.CharField("Nom", max_length=200)
	price = models.DecimalField("Prix", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
	quantity = models.IntegerField("Quantité", validators=[MinValueValidator(0)], help_text="Quantité en stock")
	min_stock = models.IntegerField("Seuil d'alerte stock", default=5, validators=[MinValueValidator(0)], help_text="Alerte si quantité ≤ seuil")
	image = models.ImageField("Photo", upload_to='products/', blank=True, null=True)
	created_at = models.DateTimeField("Créé le", auto_now_add=True)
	updated_at = models.DateTimeField("Mis à jour le", auto_now=True)

	class Meta:
		verbose_name = "Produit"
		verbose_name_plural = "Produits"
		ordering = ["name"]

	def __str__(self):
		return f"{self.name}"


class Customer(models.Model):
	first_name = models.CharField("Prénom", max_length=100)
	last_name = models.CharField("Nom", max_length=100)
	phone = models.CharField("Téléphone", max_length=30, blank=True, null=True)
	created_at = models.DateTimeField("Créé le", auto_now_add=True)

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"
		ordering = ["last_name", "first_name"]

	def __str__(self):
		# Afficher NOM puis Prénom (ex: DUPONT Jean)
		parts = []
		if self.last_name:
			parts.append(str(self.last_name).strip())
		if self.first_name:
			parts.append(str(self.first_name).strip())
		return " ".join(parts)

	def save(self, *args, **kwargs):
		# Normaliser les noms: NOM en majuscules, Prénom capitalisé
		if self.last_name:
			self.last_name = str(self.last_name).strip().upper()
		if self.first_name:
			val = str(self.first_name).strip().lower()
			# capitaliser uniquement la première lettre
			self.first_name = val[:1].upper() + val[1:]
		return super().save(*args, **kwargs)


class Sale(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Client")
	created_at = models.DateTimeField("Créé le", auto_now_add=True)
	note = models.CharField("Note", max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Vente"
		verbose_name_plural = "Ventes"
		ordering = ["-created_at"]

	def __str__(self):
		return f"Vente #{self.id} - {self.created_at:%Y-%m-%d %H:%M}"

	@property
	def total(self):
		return sum((item.line_total for item in self.items.all()), start=Decimal("0"))

	@property
	def amount_paid(self):
		return sum((p.amount for p in self.payments.all()), start=Decimal("0"))

	@property
	def balance(self):
		return self.total - self.amount_paid

	@property
	def is_credit(self):
		return self.balance > 0


class SaleItem(models.Model):
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items", verbose_name="Vente")
	product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produit")
	quantity = models.PositiveIntegerField("Quantité", validators=[MinValueValidator(1)])
	unit_price = models.DecimalField("Prix unitaire", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

	class Meta:
		verbose_name = "Ligne de vente"
		verbose_name_plural = "Lignes de vente"

	def __str__(self):
		return f"{self.product} x {self.quantity}"

	@property
	def line_total(self):
		return self.unit_price * self.quantity


class Payment(models.Model):
	CASH = 'CASH'
	CHEQUE = 'CHEQUE'
	OTHER = 'OTHER'
	METHOD_CHOICES = [
		(CASH, 'Espèce'),
		(CHEQUE, 'Chèque'),
		(OTHER, 'Autre'),
	]

	sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='payments', verbose_name="Vente")
	amount = models.DecimalField("Montant", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
	method = models.CharField("Méthode", max_length=10, choices=METHOD_CHOICES, default=CASH)
	created_at = models.DateTimeField("Créé le", auto_now_add=True)

	class Meta:
		verbose_name = "Paiement"
		verbose_name_plural = "Paiements"

	def __str__(self):
		return f"Paiement {self.amount} sur vente #{self.sale_id}"


class StockMovement(models.Model):
	RESTOCK = 'RESTOCK'
	SALE = 'SALE'
	ADJUST = 'ADJUST'
	OTHER = 'OTHER'
	REASONS = [
		(RESTOCK, 'Entrée (réassort)'),
		(SALE, 'Sortie (vente)'),
		(ADJUST, 'Ajustement'),
		(OTHER, 'Autre'),
	]

	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements', verbose_name='Produit')
	change = models.IntegerField('Variation')
	reason = models.CharField('Motif', max_length=16, choices=REASONS, default=OTHER)
	sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Vente liée')
	note = models.CharField('Note', max_length=255, blank=True, null=True)
	created_at = models.DateTimeField('Créé le', auto_now_add=True)

	class Meta:
		verbose_name = 'Mouvement de stock'
		verbose_name_plural = 'Mouvements de stock'
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.product} {self.change:+d} ({self.reason})"


# --- Gestion de caisse ---

class CashSession(models.Model):
	"""Session de caisse: ouverture -> fermeture.

	opening_counts / closing_counts: JSON avec la structure {
	  "cash": {"200": 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0, "0.50": 0, "0.20": 0, "0.10": 0, "0.05": 0},
	  "cheques": nombre total de chèques (int)
	}
	Seuls les champs nécessaires sont obligatoires; la fermeture peut contenir un snapshot de comptage réel.
	"""
	opened_at = models.DateTimeField("Ouverture", auto_now_add=True)
	closed_at = models.DateTimeField("Fermeture", blank=True, null=True)
	is_closed = models.BooleanField("Fermée", default=False)
	opening_counts = models.JSONField("Comptage ouverture", default=dict)
	closing_counts = models.JSONField("Comptage fermeture", default=dict, blank=True, null=True)
	current_counts = models.JSONField("Comptage courant", default=dict, blank=True, null=True)
	opening_note = models.CharField("Note ouverture", max_length=255, blank=True, null=True)
	closing_note = models.CharField("Note fermeture", max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Session de caisse"
		verbose_name_plural = "Sessions de caisse"
		ordering = ["-opened_at"]

	def __str__(self):
		state = "fermée" if self.is_closed else "ouverte"
		return f"Session caisse #{self.id} ({state})"

	@property
	def movements_total_cash(self):
		return sum((m.amount for m in self.movements.filter(method=Payment.CASH)), start=Decimal("0"))

	@property
	def movements_total_cheque(self):
		return sum((m.amount for m in self.movements.filter(method=Payment.CHEQUE)), start=Decimal("0"))

	@property
	def total_estimated(self):
		"""Total estimé = somme espèces (ouverture + mouvements espèces) + chèques (ouverture + mouvements chèques).
		Si opening_counts ne contient pas le détail, on suppose 0.
		"""
		cash_open = Decimal("0")
		cheque_open = Decimal("0")
		oc = self.opening_counts or {}
		cash_map = (oc.get("cash") or {})
		for denom, qty in cash_map.items():
			try:
				cash_open += Decimal(str(denom)) * Decimal(str(qty))
			except Exception:
				continue
		cheque_open = Decimal(str((oc.get("cheques") or 0)))  # valeur indicative; chèques ouverture stockés comme compte, pas montant précis
		return cash_open + self.movements_total_cash + self.movements_total_cheque  # on ajoute chèques reçus (montant) + espèces reçues


class CashMovement(models.Model):
	PAYMENT = 'PAYMENT'
	ADJUST_IN = 'ADJUST_IN'
	ADJUST_OUT = 'ADJUST_OUT'
	DROP = 'DROP'  # remise de caisse (retrait espèces)
	CHANGE = 'CHANGE'  # rendu monnaie au client
	COUNT = 'COUNT'  # snapshot de comptage en cours (non financier, informatif)
	MOVEMENT_TYPES = [
		(PAYMENT, 'Paiement'),
		(ADJUST_IN, 'Ajustement +'),
		(ADJUST_OUT, 'Ajustement -'),
		(DROP, 'Remise de caisse'),
		(CHANGE, 'Rendu'),
		(COUNT, 'Comptage'),
	]

	session = models.ForeignKey(CashSession, on_delete=models.CASCADE, related_name='movements', verbose_name='Session')
	movement_type = models.CharField('Type', max_length=16, choices=MOVEMENT_TYPES, default=PAYMENT)
	method = models.CharField('Méthode', max_length=10, choices=Payment.METHOD_CHOICES, blank=True, null=True)
	amount = models.DecimalField('Montant', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=Decimal('0'))
	counts_snapshot = models.JSONField('Comptage', blank=True, null=True, help_text="Détail des billets/monnaies pour ce mouvement si pertinent")
	tendered_breakdown = models.JSONField('Ventilation espèces données', blank=True, null=True)
	change_breakdown = models.JSONField('Ventilation rendu', blank=True, null=True)
	change_amount = models.DecimalField('Montant rendu', max_digits=10, decimal_places=2, blank=True, null=True)
	sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Vente liée')
	payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Paiement lié')
	note = models.CharField('Note', max_length=255, blank=True, null=True)
	created_at = models.DateTimeField('Créé le', auto_now_add=True)

	class Meta:
		verbose_name = 'Mouvement de caisse'
		verbose_name_plural = 'Mouvements de caisse'
		ordering = ['-created_at']

	def __str__(self):
		return f"Mvt caisse {self.movement_type} {self.amount}€ (session {self.session_id})"


# Helpers internes (on les laisse ici pour simplicité)
def get_active_cash_session():
	return CashSession.objects.filter(is_closed=False).order_by('-opened_at').first()


def _session_ensure_current(session: CashSession):
	"""S'assure que current_counts est initialisé à partir de opening_counts si vide."""
	if not session.current_counts:
		session.current_counts = session.opening_counts.copy() if session.opening_counts else {'cash': {}, 'cheques': 0}
		session.save(update_fields=['current_counts'])


def adjust_session_counts(session: CashSession, added: dict | None = None, removed: dict | None = None, cheques_delta: int = 0):
	"""Met à jour le comptage courant d'une session.

	added: dict {denom(str): qty(int)} à ajouter
	removed: dict {denom(str): qty(int)} à soustraire
	cheques_delta: variation (ex +1 pour nouveau chèque encaisse, -1 si rendu improbable)
	"""
	_session_ensure_current(session)
	cc = session.current_counts or {}
	cash_map = cc.get('cash') or {}
	if added:
		for k, v in added.items():
			cash_map[k] = int(cash_map.get(k, 0)) + int(v)
	if removed:
		for k, v in removed.items():
			cash_map[k] = max(0, int(cash_map.get(k, 0)) - int(v))
	cc['cash'] = cash_map
	cheques_base = int(cc.get('cheques') or 0)
	cc['cheques'] = cheques_base + cheques_delta
	session.current_counts = cc
	session.save(update_fields=['current_counts'])


def record_payment_movement(payment: Payment, tendered_breakdown: dict | None = None, change_breakdown: dict | None = None, change_amount: Decimal | None = None):
	"""Enregistre mouvement(s) pour un paiement espèces ou chèque.

	Arguments:
	- tendered_breakdown: billets/pièces donnés par le client (ajout à la caisse).
	- change_breakdown: billets/pièces rendus (sortie de la caisse).
	- change_amount: montant du rendu (pour mouvement CHANGE).
	"""
	session = get_active_cash_session()
	if not session:
		return None
	if payment.method not in (Payment.CASH, Payment.CHEQUE):
		return None

	# Mouvement principal (paiement enregistré) + ventilation espèces données
	counts_snapshot = None
	if tendered_breakdown and payment.method == Payment.CASH:
		counts_snapshot = {'cash_added': tendered_breakdown}
	mvt_pay = CashMovement.objects.create(
		session=session,
		movement_type=CashMovement.PAYMENT,
		method=payment.method,
		amount=payment.amount,
		sale=payment.sale,
		payment=payment,
		counts_snapshot=counts_snapshot,
		tendered_breakdown=tendered_breakdown if payment.method == Payment.CASH else None,
		note='Paiement enregistré'
	)
	# Ajuster counts courants
	if payment.method == Payment.CASH and tendered_breakdown:
		adjust_session_counts(session, added=tendered_breakdown)
	elif payment.method == Payment.CHEQUE:
		adjust_session_counts(session, cheques_delta=1)

	# Mouvement de rendu (si change) avec ventilation réelle
	if change_amount and change_amount > 0 and change_breakdown:
		CashMovement.objects.create(
			session=session,
			movement_type=CashMovement.CHANGE,
			method=Payment.CASH,
			amount=change_amount,
			sale=payment.sale,
			counts_snapshot={'cash_change': change_breakdown},
			change_breakdown=change_breakdown,
			change_amount=change_amount,
			note=f'Rendu {change_amount:.2f}€'
		)
		adjust_session_counts(session, removed=change_breakdown)
	return mvt_pay

