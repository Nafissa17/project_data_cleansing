# Projet Data Cleansing

## Description générale

Ce projet a pour objectif d'appliquer des techniques de **nettoyage et d'unification de données** sur trois mini-projets :

1. **CRM** : nettoyage des données clients
2. **Catalogue produit unique** : fusion et harmonisation des catalogues FR et US
3. **Suivi des ventes quotidien** : validation et nettoyage des fichiers de ventes

Le projet génère des données **propres**, des **KPI de qualité**, et une documentation complète pour assurer la **reproductibilité**.

---

## Structure du projet


<img width="673" height="462" alt="image" src="https://github.com/user-attachments/assets/303f5a29-fb6d-4af1-a9ed-9e01fd4a7d78" />


---


## Instructions pour exécuter les scripts

### 1. Prérequis

- Python 3.10+  
- Packages Python :
```bash
pip install pandas numpy


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

## Bonnes pratiques

- Les scripts utilisent le dossier `data/raw/` comme source
- Les fichiers nettoyés sont automatiquement créés dans `data/clean/`
- Les KPI et rapports sont automatiquement créés dans `data/reports/`
- Chaque étape est reproductible, aucun traitement manuel nécessaire
- Les colonnes numériques restent numériques pour permettre les calculs futurs (ex : poids, prix, montant)
- Si vous ajoutez de nouveaux fichiers source, il suffit de les placer dans `data/raw/` et de relancer le script correspondant
