# Coop POS

Caisse enregistreuse Django pour coopérative. Gestion des ventes, clients, stocks, dettes et caisse.

---

## Fonctionnalités

- Kiosk de vente avec grille produits par catégorie
- Gestion des paiements (espèces avec rendu monnaie, chèque, autre)
- Historique des ventes et gestion des dettes
- Catalogue produits avec gestion des stocks
- Tableau de bord avec statistiques et graphiques
- Gestion de caisse (fond, remises, mouvements)
- Exports Excel (ventes, dettes, catalogue)
- Reçus PDF
- Authentification à deux rôles : **Admin** et **Caissier**

---

## Installation développement (local, sans Docker)

**Prérequis** : Python 3.11+

```powershell
git clone <repo>
cd Coop1.0
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py setup_groups     # crée les groupes + superuser admin/admin123
python manage.py runserver 8001 --noreload
```

Accéder à `http://127.0.0.1:8001/` — vous serez redirigé vers la page de connexion.

---

## Installation production (Docker + PostgreSQL)

**Prérequis** : Docker et Docker Compose installés.

```bash
cp .env.example .env
# Éditer .env : SECRET_KEY, DB_PASSWORD, ALLOWED_HOSTS
docker-compose up --build -d
```

L'application est disponible sur `http://localhost:8000/`.

Au premier démarrage, les migrations sont appliquées et les groupes créés automatiquement. Le superuser `admin` (mot de passe `admin123`) est créé s'il n'existe pas — **changez-le immédiatement** via l'admin Django (`/admin/`).

---

## Comptes et rôles

| Rôle | Accès |
|------|-------|
| **Admin** (superuser ou groupe Admin) | Toutes les fonctionnalités, y compris créer/modifier/supprimer produits, catégories, clients, ventes ; vider l'historique |
| **Caissier** (groupe Caissier) | Ventes, historique, catalogue (lecture + ajout stock), clients (lecture), caisse, exports |

### Créer un utilisateur

1. Connectez-vous avec le compte admin
2. Allez sur `/admin/` → Utilisateurs → Ajouter
3. Assignez le groupe `Admin` ou `Caissier`

---

## Variables d'environnement

| Variable | Défaut | Description |
|----------|--------|-------------|
| `SECRET_KEY` | clé dev | Clé secrète Django — **obligatoire en prod** |
| `DEBUG` | `True` | Passer à `False` en production |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Hostnames autorisés (séparés par virgule) |
| `DB_HOST` | *(vide)* | Si défini → PostgreSQL ; sinon → SQLite |
| `DB_NAME` | `coop` | Nom de la base de données |
| `DB_USER` | `coop` | Utilisateur PostgreSQL |
| `DB_PASSWORD` | — | Mot de passe PostgreSQL |
| `DB_PORT` | `5432` | Port PostgreSQL |

---

## URLs clés

| URL | Description |
|-----|-------------|
| `/` | Dashboard (redirige vers la page de connexion si non connecté) |
| `/login/` | Page de connexion |
| `/sales/new/` | Kiosk — nouvelle vente |
| `/sales/` | Historique des ventes |
| `/products/` | Catalogue produits |
| `/customers/` | Liste des clients |
| `/cash/` | Tableau de bord caisse |
| `/admin/` | Administration Django |

---

## Stack technique

- **Backend** : Django 5.1, Python 3.13
- **Base de données** : PostgreSQL (prod) / SQLite (dev)
- **Frontend** : Bootstrap 5.3, vanilla JS
- **Exports** : openpyxl (Excel), ReportLab (PDF)
- **Serveur** : Gunicorn + Whitenoise (fichiers statiques)
