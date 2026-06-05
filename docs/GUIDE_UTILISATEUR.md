# Guide utilisateur — Coop POS

Application de caisse enregistreuse pour coopérative.

---

## Rôles

| Rôle | Accès |
|------|-------|
| 🟦 **Caissier** | Vente, historique (lecture), catalogue (lecture + ajout stock), clients (lecture), caisse, exports |
| 🔴 **Admin** | Tout ce que fait le Caissier + créer/modifier/supprimer produits, clients, ventes, utilisateurs |

Les fonctionnalités réservées aux Admins sont signalées par 🔴 dans ce guide. Les boutons correspondants sont **invisibles** pour les Caissiers.

---

## Table des matières

**Commun aux deux rôles**
1. [Connexion / Déconnexion](#1-connexion--déconnexion)
2. [Thème clair / sombre](#2-thème-clair--sombre)
3. [Tableau de bord](#3-tableau-de-bord)
4. [Faire une vente](#4-faire-une-vente)
5. [Historique des ventes](#5-historique-des-ventes)
6. [Gérer les dettes](#6-gérer-les-dettes)
7. [Catalogue produits](#7-catalogue-produits)
8. [Clients](#8-clients)
9. [Caisse](#9-caisse)
10. [Exports](#10-exports)

**Réservé Admin 🔴**

11. [Supprimer / vider des données](#11-supprimer--vider-des-données-)
12. [Réglages utilisateurs](#12-réglages-utilisateurs-)

---

---

# Partie Caissier 🟦

---

## 1. Connexion / Déconnexion

Ouvrez l'application dans votre navigateur. Saisissez votre **nom d'utilisateur** et votre **mot de passe**, puis cliquez sur **Se connecter**.

Pour vous déconnecter : cliquez sur votre nom en haut à droite → **Déconnexion**.

---

## 2. Thème clair / sombre

Cliquez sur l'icône **lune** ou **soleil** dans la barre de navigation pour basculer entre thème clair et sombre. Le choix est mémorisé dans votre navigateur.

---

## 3. Tableau de bord

![Tableau de bord](screenshots/01_dashboard.png)

Vue d'ensemble de l'activité, par défaut sur **le mois en cours** :

- **Ventes**, **panier moyen**, **nombre de transactions**, **clients actifs**
- **Graphique des ventes** jour par jour sur le mois
- **Top 5 produits** vendus et **Top 5 clients** (CA)
- **Alertes stock bas** — produits sous leur seuil minimum
- **Top clients endettés**, **Plus gros paniers**, **Ventes récentes**

**Changer la période** : boutons **Jour / Semaine / Mois / Année** en haut à droite.

---

## 4. Faire une vente

![Kiosk de vente avec panier](screenshots/03_kiosk_panier.png)

### Étape 1 — Choisir les produits

- Les produits sont affichés en grille, regroupés par **catégorie**.
- **Cliquez** sur une carte pour l'ajouter au panier.
- Une fois ajouté, un **bandeau bleu [−] quantité [+]** apparaît en bas de la carte — ajustez directement sans toucher au tableau panier.
- Utilisez la **barre de recherche** ou les **filtres par catégorie** pour trouver rapidement un article.
- Le **stock disponible** est affiché sous chaque prix. Les articles en rupture (stock = 0) sont grisés et non cliquables.
- Le bouton **Vider** (à gauche de "Valider panier") efface tout le panier en un clic.

### Étape 2 — Sélectionner le client

Tapez le nom dans le champ **Client** — les suggestions apparaissent immédiatement. Cliquez pour sélectionner. **Le client est obligatoire** pour valider.

### Étape 3 — Note (optionnel)

Cliquez sur **Ajouter une note** pour dérouler un champ de note libre.

### Étape 4 — Valider le panier

Cliquez sur **Valider panier**. La fenêtre de paiement s'ouvre.

### Étape 5 — Paiement

| Mode | Comment faire |
|------|--------------|
| **Espèces** | Onglet Espèce → cliquez sur les billets/pièces remis → le **rendu monnaie** se calcule automatiquement |
| **Chèque** | Onglet Chèque → saisissez le montant |
| **Autre** | Onglet Autre → saisissez le montant |
| **À crédit (dette)** | Cliquez **Encaisser** sans saisir de montant — le solde reste dû |

> Si le stock d'un article est insuffisant au moment d'encaisser, un message d'erreur s'affiche et les boutons disparaissent. Fermez la fenêtre et corrigez le panier.

### Étape 6 — Reçu

Le reçu s'affiche automatiquement. Téléchargeable en **PDF**. Le panier est vidé pour la vente suivante.

---

## 5. Historique des ventes

![Historique des ventes](screenshots/04_historique.png)

Liste de toutes les ventes avec filtre par client et statut.

| Bouton | Accès | Description |
|--------|-------|-------------|
| **Détails** | Tous | Affiche le reçu complet en fenêtre |
| **Régulariser** | Tous | Enregistre un paiement sur une vente impayée |
| **Régler les dettes** | Tous | Paiement groupé sur toutes les dettes d'un client |
| **Supprimer** | 🔴 Admin | Supprime la vente avec options |
| **Vider l'historique** | 🔴 Admin | Supprime toutes les ventes |

---

## 6. Gérer les dettes

### Régler une dette individuelle

Historique → **Régulariser** (sur la vente concernée) → saisissez le montant et la méthode → **Valider**.

### Règlement groupé par client

**Régler les dettes** (en haut de l'historique) → sélectionnez le client → saisissez le montant global. Le système répartit automatiquement du plus ancien au plus récent.

---

## 7. Catalogue produits

![Catalogue produits](screenshots/05_catalogue.png)

| Action | Accès | Description |
|--------|-------|-------------|
| **+ Stock** | Tous | Ajoute une quantité au stock existant |
| **Historique stock** | Tous | Journal de tous les mouvements |
| **Ajuster stock** | 🔴 Admin | Delta +/− avec note obligatoire |
| **Modifier / Supprimer** | 🔴 Admin | Édite ou supprime le produit |
| **+ Produit** | 🔴 Admin | Crée un nouveau produit |
| **Catégories** | 🔴 Admin | Gère les catégories |

---

## 8. Clients

![Clients](screenshots/07_clients.png)

| Action | Accès | Description |
|--------|-------|-------------|
| Cliquer sur un nom | Tous | Fiche client : ventes, total acheté, dette |
| **Nouveau client** | Tous | Crée un client |
| **Modifier** | 🔴 Admin | Modifie le nom du client |
| **Supprimer** (icône) | 🔴 Admin | Supprime un client (ventes conservées) |
| **Supprimer tous les clients** | 🔴 Admin | Supprime toute la liste (irréversible) |

---

## 9. Caisse

![Caisse](screenshots/06_caisse.png)

### Ce que vous voyez

- **Espèces courantes** : détail par billet/pièce, mis à jour à chaque vente
- **Chèques** : total encaissé sur la session
- **Total global** : espèces + chèques
- **Mouvements récents** : les 25 derniers mouvements

### Initialiser le fond de caisse

**Réinitialiser** → saisissez les quantités de chaque billet/pièce → **Valider**.
Ferme l'ancienne session et ouvre une nouvelle. À faire en début de journée.

### Remise de caisse

**Remise** → saisissez les billets/pièces retirés → **Valider**.
Enregistre un retrait d'espèces (versement en banque, coffre…).

---

## 10. Exports

Tous les exports sont au format Excel (`.xlsx`).

| Export | Depuis |
|--------|--------|
| Ventes | Page historique des ventes |
| Clients endettés | Page historique des ventes |
| Catalogue produits | Page catalogue |
| Mouvements caisse | Page caisse |

**Reçu PDF** : dans la fenêtre de détail d'une vente → bouton **PDF**.

---

---

# Partie Admin 🔴

*Toutes les fonctionnalités Caissier + les suivantes.*

---

## 11. Supprimer / vider des données 🔴

### Supprimer une vente

Historique des ventes → icône poubelle → une fenêtre s'ouvre avec deux options :

| Option | Effet |
|--------|-------|
| **Remettre les produits en stock** | Les quantités achetées sont réintégrées au catalogue |
| **Annuler les mouvements de caisse** | Le comptage caisse revient à l'état avant la vente |

Les deux options sont **activées par défaut**. Décochez selon votre situation.

### Vider tout l'historique des ventes

Historique → **Vider l'historique** → confirmer. Les stocks ne sont **pas** remis à jour automatiquement.

### Supprimer un client

Clients → icône poubelle sur la ligne → confirmer. Les ventes de ce client sont conservées.

### Supprimer tous les clients

Clients → **Supprimer tous les clients** → modale de confirmation → **Tout supprimer**.
Les ventes sont conservées mais ne seront plus rattachées à un client.

### Supprimer / modifier un produit

Catalogue → menu déroulant (flèche à droite de "+ Stock") → **Modifier** ou **Supprimer**.

---

## 12. Réglages utilisateurs 🔴

Accessible via le menu utilisateur (haut droite) → **Réglages utilisateurs**.

### Créer un utilisateur

**Nouvel utilisateur** → renseignez prénom, nom, nom d'utilisateur, mot de passe et rôle → **Créer**.

### Modifier un utilisateur

**Modifier** → changez le nom, le rôle ou le mot de passe (laisser le champ mot de passe vide pour ne pas le changer) → **Enregistrer**.

### Supprimer un utilisateur

Icône poubelle → confirmer. Il est impossible de supprimer son propre compte.

### Rôles disponibles

| Rôle | Description |
|------|-------------|
| **Admin** | Accès complet à toutes les fonctionnalités |
| **Caissier** | Ventes, caisse, catalogue (lecture + ajout stock), clients (lecture), exports |
