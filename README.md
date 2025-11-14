# Projet Data Cleansing

## Description générale

Ce projet a pour objectif d'appliquer des techniques de **nettoyage et d'unification de données** sur trois mini-projets :

1. **CRM** : nettoyage des données clients
2. **Catalogue produit unique** : fusion et harmonisation des catalogues FR et US
3. **Suivi des ventes quotidien** : validation et nettoyage des fichiers de ventes

Le projet génère des données **propres**, des **KPI de qualité**, et une documentation complète pour assurer la **reproductibilité**.

---

## Structure du projet


<img width="556" height="454" alt="image" src="https://github.com/user-attachments/assets/b28c2651-1389-4d39-a41c-768b403addf3" />


---


## Instructions pour exécuter les scripts

### 1. Prérequis

- Python 3.10+  
- Packages Python :
```bash
pip install pandas numpy matplotlib seaborn


# Guide d'utilisation des scripts de nettoyage de données

## 2. Nettoyage CRM (clients)

### Étapes d'exécution

1. Placez-vous dans le dossier `scripts` :
```bash
   cd scripts
```

2. Lancez le script :
```bash
   python crm.py
```

### Produits générés

- `data/clean/clients_clean.csv` → clients nettoyés
- `data/reports/kpi_qualite_clients.csv` → KPI avant/après nettoyage

---

## 3. Catalogue produit unique (FR + US)

### Étapes d'exécution

1. Placez-vous dans le dossier `scripts` :
```bash
   cd scripts
```

2. Lancez le script :
```bash
   python catalog.py
```

### Produits générés

- `data/clean/catalog_canonique.csv` → catalogue final harmonisé
- `data/reports/kpi_catalog.csv` → KPI de qualité des produits

---

## 4. Suivi des ventes quotidien

### Étapes d'exécution

1. Placez-vous dans le dossier `scripts` :
```bash
   cd scripts
```

2. Lancez le script :
```bash
   python sales.py
```

### Produits générés

- `data/clean/sales_clean.csv` → ventes nettoyées
- `data/reports/daily_revenue.csv` → chiffre d'affaires journalier
- `data/reports/kpi_sales.csv` → KPI de qualité des ventes


  ---
  

### Visualisations Bonus

Ce script génère des visualisations simples pour vérifier la qualité et l'évolution des données clients, catalogue et ventes.

### Fichiers requis

- `data/clean/clients_clean.csv`
- `data/clean/catalog_canonique.csv`
- `data/clean/sales_clean.csv`

Les fichiers doivent exister avant d'exécuter le script.


### Graphiques générés

1. Répartition des clients par pays
2. Répartition des produits par catégorie
3. Évolution du chiffre d'affaires quotidien

### Exécution

Depuis le dossier racine du projet :
```bash
cd tests
python visualisation_bonus.py
```

Les graphiques s'affichent automatiquement. Fermer chaque fenêtre pour passer au graphique suivant.


---


## Bonnes pratiques

- Les scripts utilisent le dossier `data/raw/` comme source
- Les fichiers nettoyés sont automatiquement créés dans `data/clean/`
- Les KPI et rapports sont automatiquement créés dans `data/reports/`
- Chaque étape est reproductible, aucun traitement manuel nécessaire
- Les colonnes numériques restent numériques pour permettre les calculs futurs (ex : poids, prix, montant)
- Si vous ajoutez de nouveaux fichiers source, il suffit de les placer dans `data/raw/` et de relancer le script correspondant



