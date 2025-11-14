# Dictionnaire des données

Ce document décrit les colonnes des fichiers nettoyés, les types, contraintes et correspondances.

---

## CRM : clients_clean.csv

| Colonne   | Type   | Description                     | Contraintes / Correspondances |
|-----------|--------|---------------------------------|------------------------------|
| id        | int    | Identifiant unique du client    | Unique, obligatoire          |
| nom       | str    | Nom du client                   | Non vide                     |
| prenom    | str    | Prénom du client                | Non vide                     |
| email     | str    | Email du client                 | Format standard, unique, normalisé en minuscules |
| telephone | str    | Téléphone normalisé             | Format international (+33 pour France, etc.) |
| pays      | str    | Pays du client                  | Standardisé via mapping (ex: "FR" → "France") |
| naissance | date   | Date de naissance               | Format ISO YYYY-MM-DD, âge plausible (0-120 ans) |

---

## Catalogue produit : catalog_canonique.csv

| Colonne       | Type   | Description                       | Contraintes / Correspondances |
|---------------|--------|-----------------------------------|------------------------------|
| sku           | str    | Code produit unique               | Unique, obligatoire          |
| name          | str    | Nom du produit                    | Non vide                     |
| category_name | str    | Catégorie harmonisée              | Correspond au mapping_categories.csv |
| weight_kg     | float  | Poids du produit en kilogrammes  | > 0, converti depuis g/lb si nécessaire |
| price_eur     | float  | Prix du produit en euros          | ≥ 0, conversion USD → EUR appliquée |
| currency      | str    | Devise finale                     | Toujours €                   |

---

## Ventes : sales_clean.csv

| Colonne         | Type   | Description                           | Contraintes / Correspondances |
|-----------------|--------|---------------------------------------|------------------------------|
| order_id        | str    | Identifiant unique de la commande     | Unique, obligatoire          |
| date            | date   | Date de la transaction (ISO)          | Format YYYY-MM-DD            |
| email_client    | str    | Email du client                        | Correspond à CRM             |
| montant         | float  | Montant de la transaction             | ≥ 0, remboursé indiqué par remboursement |
| remboursement   | bool   | True si remboursement, False sinon    | Déduit du montant négatif ou du champ spécifique |
| channel         | str    | Canal de vente                         | Exemple : store, mobile, web |

---

## Notes

- Tous les fichiers ont été nettoyés pour supprimer les doublons et harmoniser les formats.
- Les correspondances de valeurs (ex: pays, catégories, devises) sont appliquées via les mappings fournis.
- Les conversions sont normalisées pour assurer une boutique internationale cohérente.
