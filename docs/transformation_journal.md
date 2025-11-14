# Journal de transformations

Ce document décrit toutes les modifications appliquées aux données, pourquoi elles ont été faites, et les résultats obtenus.

---

## 1. CRM (clients_clean.csv)

| Transformation | Description | Volume affecté | Exceptions / Notes |
|----------------|------------|----------------|------------------|
| Emails | Standardisation : minuscules, suppression des espaces | Toutes les lignes | Aucun |
| Pays | Harmonisation via mapping (FR → France, BE → Belgique, CH → Suisse, etc.) | Toutes les lignes | Valeurs inconnues conservées sans modification |
| Téléphones | Suppression des caractères non numériques, format international (+33 pour France, etc.) | Lignes avec téléphone renseigné | Téléphones invalides laissés en l'état |
| Dates de naissance | Vérification format ISO YYYY-MM-DD | Toutes les lignes | Dates incorrectes converties en `NaT` |
| Doublons | Suppression sur `email` + `id` | Lignes dupliquées | Aucun |
| KPI calculés | Valeurs manquantes et uniques par colonne avant/après nettoyage | Toutes les colonnes | - |

---

## 2. Catalogue produit unique (catalog_canonique.csv)

| Transformation | Description | Volume affecté | Exceptions / Notes |
|----------------|------------|----------------|------------------|
| Poids | Conversion automatique de g → kg | Toutes les lignes avec unité g | Poids non numériques ignorés |
| Prix | Conversion USD → EUR, € conservé | Toutes les lignes USD | Valeurs non numériques ignorées |
| Catégories | Harmonisation via `mapping_categories.csv` | Toutes les lignes | Catégories non mappées conservées |
| Doublons SKU | Suppression des doublons | Lignes avec SKU identique | - |
| Colonnes finales | Réorganisation et renommage : `sku, name, category_name, weight_kg, price, currency` | Toutes les lignes | - |
| KPI calculés | Valeurs manquantes et uniques par colonne | Toutes les colonnes | - |

---

## 3. Suivi des ventes quotidien (sales_clean.csv)

| Transformation | Description | Volume affecté | Exceptions / Notes |
|----------------|------------|----------------|------------------|
| Dates | Normalisation au format ISO YYYY-MM-DD | Toutes les lignes | Dates invalides converties en `NaT` |
| Montants | Vérification >= 0 | Toutes les lignes | Montants négatifs marqués comme remboursement |
| Remboursements | Séparation dans colonne `remboursement` | Lignes avec montant négatif | - |
| Doublons | Suppression sur `order_id + email_client` | Lignes dupliquées | - |
| KPI calculés | Valeurs manquantes, transactions positives, revenus journaliers | Toutes les colonnes | - |

---

## Notes Générales

- Chaque transformation est appliquée via les scripts Python correspondants (`crm.py`, `catalog.py`, `sales.py`).
- Les volumes affectés sont calculés automatiquement et peuvent être vérifiés via les fichiers de KPI (`kpi_qualite_clients.csv`, `kpi_catalog.csv`, `daily_revenue.csv`).
- Les exceptions recensent les valeurs non conformes ou impossibles à corriger automatiquement.
- Ce journal permet de tracer les étapes du nettoyage pour assurer la reproductibilité et la qualité des données.
