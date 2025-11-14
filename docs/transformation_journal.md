# Journal de transformations

## 1. CRM (clients)
- **Emails** : standardisation (minuscules, suppression espaces)
- **Pays** : harmonisation avec mapping FR/BE/CH etc.
- **Téléphones** : suppression caractères non numériques, format international +33...
- **Dates** : vérification format ISO YYYY-MM-DD
- **Doublons** : suppression sur `email` + `id`
- **KPI calculés** : valeurs manquantes et uniques avant/après nettoyage

---

## 2. Catalogue produit unique
- **Poids** : conversion automatique g → kg
- **Prix** : USD → EUR avec taux fixe, € conservé
- **Catégories** : harmonisation via `mapping_categories.csv`
- **Doublons SKU** : supprimés
- **Colonnes finales** : `sku, name, category_name, weight_kg, price, currency`
- **KPI calculés** : valeurs manquantes et uniques par colonne

---

## 3. Suivi ventes quotidien
- **Dates** : normalisation ISO YYYY-MM-DD
- **Montants** : vérification >= 0
- **Remboursements** : séparés
- **Doublons** : suppression sur `order_id + email_client`
- **KPI calculés** : valeurs manquantes, transactions positives, revenus journaliers
