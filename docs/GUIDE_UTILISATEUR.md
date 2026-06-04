# Guide utilisateur — Coop POS

Application de caisse enregistreuse pour coopérative. Ce guide couvre toutes les fonctionnalités accessibles depuis l'interface web.

---

## Table des matières

1. [Connexion / Déconnexion](#1-connexion--déconnexion)
2. [Tableau de bord](#2-tableau-de-bord)
3. [Faire une vente (kiosk)](#3-faire-une-vente-kiosk)
4. [Historique des ventes](#4-historique-des-ventes)
5. [Gérer les dettes](#5-gérer-les-dettes)
6. [Catalogue produits](#6-catalogue-produits)
7. [Gérer les clients](#7-gérer-les-clients)
8. [Caisse](#8-caisse)
9. [Exports](#9-exports)
10. [Gestion des comptes (Admin)](#10-gestion-des-comptes-admin)

---

## 1. Connexion / Déconnexion

### Se connecter

1. Ouvrez l'application dans votre navigateur.
2. Vous êtes automatiquement redirigé vers la page `/login/`.
3. Saisissez votre **nom d'utilisateur** et votre **mot de passe**.
4. Cliquez sur **Se connecter**.

### Se déconnecter

1. Cliquez sur votre nom en haut à droite de la barre de navigation.
2. Cliquez sur **Déconnexion**.

> **Rôles** : les utilisateurs ont soit le rôle **Admin** (accès complet) soit le rôle **Caissier** (accès limité). Les boutons et actions non autorisés ne sont pas affichés pour les Caissiers.

---

## 2. Tableau de bord

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

Utilisez les boutons **Aujourd'hui / 7 jours / Ce mois / Cette année** ou sélectionnez une plage personnalisée via les champs de date.

---

## 3. Faire une vente (kiosk)

**URL** : `/sales/new/`

### Étape 1 — Sélectionner les produits

- Les produits sont affichés en grille, regroupés par catégorie.
- Cliquez sur un produit pour l'ajouter au panier (quantité 1 par clic).
- Utilisez la barre de recherche en haut pour filtrer rapidement.
- Dans le panier (côté droit), modifiez la quantité ou supprimez un article.

### Étape 2 — Sélectionner le client

- Cliquez sur **Choisir un client** et tapez le nom dans le champ de recherche.
- Le client est obligatoire pour valider la vente.
- Vous pouvez créer un nouveau client directement depuis ce champ.

### Étape 3 — Choisir le mode de paiement

**Espèces** :
1. Sélectionnez l'onglet **Espèces**.
2. Cliquez sur les billets/pièces remis par le client.
3. Le montant encaissé et le rendu monnaie sont calculés automatiquement.

**Chèque ou Autre** :
1. Sélectionnez l'onglet correspondant.
2. Saisissez le montant encaissé.

> Laissez le montant à 0 pour enregistrer une vente à crédit (dette).

### Étape 4 — Valider

Cliquez sur **Valider la vente**. Un reçu s'affiche en modale avec le détail de la vente et le rendu monnaie.

---

## 4. Historique des ventes

**URL** : `/sales/`

Liste paginée de toutes les ventes avec filtres par client et statut (payé / non payé).

### Actions disponibles

| Bouton | Description |
|--------|-------------|
| **Détails** | Affiche le reçu complet en modale |
| **Régulariser** | Enregistre un paiement complémentaire (si solde > 0) |
| **Supprimer** *(Admin)* | Supprime la vente et remet les articles en stock |
| **Régler les dettes** | Ouvre la sélection de client pour un paiement groupé |
| **Exporter clients endettés** | Télécharge un fichier Excel des débiteurs |
| **Vider l'historique** *(Admin)* | Supprime toutes les ventes (irréversible) |

---

## 5. Gérer les dettes

**URL** : `/debts/` ou depuis l'historique des ventes

Liste de toutes les ventes avec solde impayé.

### Régler une dette

**Depuis l'historique** :
1. Cliquez sur **Régulariser** sur la ligne de la vente concernée.
2. Saisissez le montant et la méthode de paiement.
3. Cliquez sur **Valider**.

**Règlement groupé par client** :
1. Cliquez sur **Régler les dettes** (en haut de la page historique).
2. Sélectionnez le client dans la liste.
3. Saisissez le montant global et la méthode.
4. Le système répartit automatiquement du plus ancien au plus récent.

---

## 6. Catalogue produits

**URL** : `/products/`

### Ajouter du stock

1. Sur la ligne du produit, cliquez sur **+ Stock**.
2. Saisissez la quantité à ajouter.
3. Cliquez sur **Ajouter**.

### Ajuster le stock manuellement *(Admin)*

Permet d'augmenter ou réduire le stock d'un montant quelconque (correction d'inventaire) :

1. Cliquez sur le menu déroulant (flèche) à droite du produit.
2. Cliquez sur **Ajuster stock**.
3. Saisissez le delta (positif pour augmenter, négatif pour réduire) et une note.
4. Cliquez sur **Appliquer**.

### Créer un produit *(Admin)*

1. Cliquez sur **+ Produit** en haut de page.
2. Renseignez le nom, la catégorie, le prix, le stock initial et le seuil d'alerte.
3. Ajoutez une photo (recadrage disponible via l'outil intégré).
4. Cliquez sur **Enregistrer**.

### Modifier / Supprimer *(Admin)*

Utilisez le menu déroulant sur chaque ligne produit.

### Gérer les catégories *(Admin)*

Cliquez sur **Catégories** en haut de page pour créer, modifier ou supprimer des catégories.

### Historique des mouvements de stock

Cliquez sur **Historique stock** dans le menu déroulant d'un produit, ou accédez à `/stocks/movements/`.

---

## 7. Gérer les clients

**URL** : `/customers/`

### Créer un client

Cliquez sur **+ Nouveau client** et renseignez le nom et prénom.

### Fiche client

Cliquez sur le nom d'un client pour voir :
- Toutes ses ventes
- Total acheté, total payé, dette totale

### Modifier / Supprimer *(Admin)*

Depuis la liste ou la fiche client.

---

## 8. Caisse

**URL** : `/cash/`

### Initialiser le fond de caisse

1. Cliquez sur **Initialiser la caisse** (ou **Nouveau fond**).
2. Saisissez les quantités de chaque billet/pièce présent en caisse.
3. Cliquez sur **Valider**.

### Remise de caisse

Enregistre un retrait d'espèces (versement en banque, etc.) :
1. Cliquez sur **Remise**.
2. Saisissez les quantités retirées.
3. Cliquez sur **Valider**.

### Tableau de bord caisse

Affiche :
- Le détail des espèces actuellement en caisse (billets et pièces)
- Le total espèces + chèques
- Les 25 derniers mouvements

---

## 9. Exports

Tous les exports sont au format Excel (`.xlsx`).

| Export | Accès |
|--------|-------|
| Ventes | `/exports/sales.xlsx` |
| Dettes | `/exports/debts.xlsx` |
| Clients endettés | `/exports/debtors.xlsx` |
| Catalogue produits | `/exports/products.xlsx` |
| Mouvements de caisse | `/cash/exports/movements.xlsx` |

Les boutons d'export sont accessibles depuis les pages correspondantes.

**Reçus PDF** : dans la modale de détail d'une vente, cliquez sur l'icône PDF pour télécharger le ticket au format 80mm.

---

## 10. Gestion des comptes (Admin)

**URL** : `/admin/`

Accessible uniquement aux superusers.

### Créer un compte utilisateur

1. Allez sur `/admin/` → **Utilisateurs** → **Ajouter un utilisateur**.
2. Saisissez le nom d'utilisateur et le mot de passe.
3. Dans la section **Permissions**, assignez le groupe **Admin** ou **Caissier**.
4. Cliquez sur **Enregistrer**.

### Modifier le mot de passe d'un utilisateur

1. Allez sur `/admin/` → **Utilisateurs** → cliquez sur l'utilisateur.
2. Cliquez sur **Ce formulaire** dans la section mot de passe.
3. Saisissez le nouveau mot de passe et confirmez.

### Groupes et permissions

- **Admin** : accès complet (création/modification/suppression de tout, vider l'historique)
- **Caissier** : ventes, paiements, ajout de stock, exports — pas de suppression ni de création de produits/catégories
