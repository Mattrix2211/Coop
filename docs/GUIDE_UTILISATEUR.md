# Guide utilisateur — Coop POS

Application de caisse enregistreuse pour coopérative.

---

## Table des matières

1. [Connexion / Déconnexion](#1-connexion--déconnexion)
2. [Thème clair / sombre](#2-thème-clair--sombre)
3. [Tableau de bord](#3-tableau-de-bord)
4. [Faire une vente (kiosk)](#4-faire-une-vente-kiosk)
5. [Historique des ventes](#5-historique-des-ventes)
6. [Gérer les dettes](#6-gérer-les-dettes)
7. [Catalogue produits](#7-catalogue-produits)
8. [Gérer les clients](#8-gérer-les-clients)
9. [Caisse](#9-caisse)
10. [Exports](#10-exports)
11. [Réglages utilisateurs (Admin)](#11-réglages-utilisateurs-admin)

---

## 1. Connexion / Déconnexion

### Se connecter

1. Ouvrez l'application dans votre navigateur.
2. Saisissez votre **nom d'utilisateur** et votre **mot de passe**.
3. Cliquez sur **Se connecter**.

### Se déconnecter

Cliquez sur votre nom en haut à droite → **Déconnexion**.

> **Rôles** : **Admin** (accès complet) ou **Caissier** (accès limité). Les boutons et actions non autorisés ne sont pas affichés pour les Caissiers.

---

## 2. Thème clair / sombre

Cliquez sur l'icône **lune** ou **soleil** dans la barre de navigation (à droite de votre nom) pour basculer entre le thème clair et sombre. Le choix est mémorisé dans votre navigateur.

---

## 3. Tableau de bord

**URL** : `/` ou `/dashboard/`

Vue d'ensemble de l'activité :

- **Chiffre d'affaires** du jour, du mois, de la période sélectionnée
- **Nombre de ventes** et panier moyen
- **Dettes totales** et top des clients débiteurs
- **Graphique des ventes** synchronisé avec la période choisie
- **Top 5 produits** (quantités vendues) et **Top 5 clients** (CA)
- **Alertes stock bas** (produits sous leur seuil minimum)
- **Ventes récentes** de la période

### Changer la période

Utilisez les boutons **Jour / Semaine / Mois / Année** ou sélectionnez une plage personnalisée.

---

## 4. Faire une vente (kiosk)

**URL** : `/sales/new/`

### Étape 1 — Sélectionner les produits

- Les produits sont affichés en grille, regroupés par catégorie.
- Cliquez sur une carte pour ajouter l'article au panier.
- Une fois ajouté, un bandeau bleu apparaît en bas de la carte avec **[−] quantité [+]** — cliquez directement dessus pour ajuster sans toucher au tableau panier.
- Utilisez la barre de recherche ou les filtres par catégorie pour trouver rapidement un article.
- Le stock disponible est affiché sous le prix de chaque article.
- Si un article est en rupture (stock = 0), sa carte est grisée et non cliquable.

### Étape 2 — Sélectionner le client

- Tapez le nom dans le champ **Client** — les suggestions apparaissent immédiatement.
- Cliquez sur un nom pour le sélectionner. Le champ affiche alors le client et un bouton **×** pour changer.
- Le client est obligatoire pour valider la vente.

### Étape 3 — Note (optionnel)

Cliquez sur **Ajouter une note** pour dérouler le champ de note.

### Étape 4 — Valider le panier

Cliquez sur **Valider panier**. La fenêtre de paiement s'ouvre.

### Étape 5 — Paiement

**Espèces** :
1. Sélectionnez **Espèce**.
2. Cliquez sur les billets/pièces remis par le client.
3. Le montant donné et le rendu monnaie sont calculés automatiquement.

**Chèque ou Autre** :
1. Sélectionnez l'onglet correspondant.
2. Saisissez le montant encaissé.

**À crédit (dette)** :
- Cliquez sur **Encaisser** sans entrer aucun montant. La vente est enregistrée avec un solde à régler.

> Si le stock d'un article est insuffisant au moment d'encaisser, un message d'erreur s'affiche et les boutons de paiement disparaissent — vous devez fermer la fenêtre et corriger le panier.

### Étape 6 — Reçu

Le reçu s'affiche automatiquement. Vous pouvez le télécharger en PDF. Le panier est vidé et l'app est prête pour la vente suivante.

### Bouton Vider

Le bouton **Vider** (à gauche de "Valider panier") efface tout le panier en un clic.

---

## 5. Historique des ventes

**URL** : `/sales/`

Liste paginée de toutes les ventes avec filtres par client et statut.

### Actions disponibles

| Bouton | Description |
|--------|-------------|
| **Détails** | Affiche le reçu complet en fenêtre |
| **Régulariser** | Enregistre un paiement sur une vente impayée |
| **Régler les dettes** | Paiement groupé sur toutes les dettes d'un client |
| **Supprimer** *(Admin)* | Supprime la vente avec options |
| **Vider l'historique** *(Admin)* | Supprime toutes les ventes |

### Supprimer une vente *(Admin)*

En cliquant sur l'icône poubelle, une fenêtre s'ouvre avec deux options (toggles) :

- **Remettre les produits en stock** — les quantités achetées sont réintégrées au catalogue
- **Annuler les mouvements de caisse** — le comptage caisse revient à l'état avant la vente

Les deux options sont activées par défaut. Décochez selon votre situation.

---

## 6. Gérer les dettes

### Régler une dette individuelle

Depuis l'historique → **Régulariser** sur la vente concernée → saisissez le montant et la méthode → **Valider**.

### Règlement groupé par client

1. Cliquez sur **Régler les dettes** (en haut de l'historique).
2. Sélectionnez le client.
3. Saisissez le montant global et la méthode.
4. Le système répartit automatiquement du plus ancien au plus récent.

---

## 7. Catalogue produits

**URL** : `/products/`

### Ajouter du stock

Sur la ligne du produit → **+ Stock** → saisissez la quantité → **Ajouter**.

### Ajuster le stock manuellement *(Admin)*

Menu déroulant → **Ajuster stock** → saisissez le delta (+/−) et une note → **Appliquer**.

### Créer un produit *(Admin)*

**+ Produit** → renseignez nom, catégorie, prix, stock initial et seuil d'alerte → **Enregistrer**.

### Gérer les catégories *(Admin)*

Bouton **Catégories** → créer, modifier ou supprimer.

### Historique des mouvements

Menu déroulant → **Historique stock** (ou `/stocks/movements/`).

---

## 8. Gérer les clients

**URL** : `/customers/`

- **Créer** : bouton **Nouveau client**
- **Modifier / Supprimer** *(Admin)* : boutons sur chaque ligne
- **Fiche client** : cliquez sur le nom pour voir toutes ses ventes, total acheté, dette

---

## 9. Caisse

**URL** : `/cash/`

### Initialiser le fond de caisse

**Réinitialiser** → saisissez les quantités de chaque billet/pièce → **Valider**.

À faire en début de journée. Ferme l'ancienne session et ouvre une nouvelle.

### Remise de caisse

**Remise** → saisissez les billets/pièces retirés → **Valider**.

Enregistre un retrait d'espèces (versement en banque, mise en coffre…).

### Tableau de bord caisse

- **Espèces courantes** : détail par billet/pièce, mis à jour à chaque vente
- **Chèques** : total des paiements par chèque sur la session
- **Total global** : espèces + chèques
- **Mouvements récents** : les 25 derniers mouvements

---

## 10. Exports

Tous les exports sont au format Excel (`.xlsx`).

| Export | Bouton |
|--------|--------|
| Ventes | Page historique des ventes |
| Clients endettés | Page historique des ventes |
| Dettes | Page dettes |
| Catalogue produits | Page catalogue |
| Mouvements caisse | Page caisse |

**Reçu PDF** : dans la fenêtre de détail d'une vente, cliquez sur **PDF**.

---

## 11. Réglages utilisateurs (Admin)

**URL** : `/settings/users/` — accessible via le menu utilisateur en haut à droite.

### Créer un utilisateur

**Nouvel utilisateur** → renseignez prénom, nom, nom d'utilisateur, mot de passe et rôle → **Créer**.

### Modifier un utilisateur

**Modifier** → changez le nom, le rôle ou le mot de passe (laisser vide pour ne pas changer) → **Enregistrer**.

### Supprimer un utilisateur

Icône poubelle → confirmer. Impossible de supprimer son propre compte.

### Rôles disponibles

| Rôle | Description |
|------|-------------|
| **Admin** | Accès complet à toutes les fonctionnalités |
| **Caissier** | Ventes, caisse, catalogue (lecture + ajout stock), exports |
| **Superadmin** | Comme Admin + accès aux réglages techniques (attribué automatiquement au premier compte) |
