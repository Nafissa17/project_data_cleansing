
---

# **data_dictionary.md**  

```markdown
# Dictionnaire des données

## CRM : clients_clean.csv
| Colonne | Type | Description | Contraintes |
|---------|------|-------------|-------------|
| id | int | Identifiant unique du client | Unique, obligatoire |
| nom | str | Nom du client | Non vide |
| prenom | str | Prénom du client | Non vide |
| email | str | Email du client | Format standard, unique |
| telephone | str | Téléphone normalisé | Format international +33... |
| pays | str | Pays standardisé | Exemple : France, Belgique, Suisse |
| naissance | date | Date de naissance | YYYY-MM-DD |

---

## Catalogue produit : catalog_canonique.csv
| Colonne | Type | Description | Contraintes |
|---------|------|-------------|-------------|
| sku | str | Code produit unique | Unique, obligatoire |
| name | str | Nom du produit | Non vide |
| category_name | str | Catégorie harmonisée | Selon mapping_categories.csv |
| weight_kg | float | Poids en kg | > 0 |
| price | float | Prix en euros | >= 0 |
| currency | str | Devise finale | Toujours € |

---

## Ventes : sales_clean.csv
| Colonne | Type | Description | Contraintes |
|---------|------|-------------|-------------|
| order_id | str | Identifiant unique commande | Unique |
| date | date | Date transaction (ISO) | YYYY-MM-DD |
| email_client | str | Email client | Correspond à CRM |
| montant | float | Montant de la transaction | >= 0 |
| remboursement | bool | True si remboursement | False sinon |
