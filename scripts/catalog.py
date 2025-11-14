import pandas as pd
import os
from utils import convert_weight_kg, convert_price_eur

# -----------------------------
# 1. Chemins des fichiers
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

catalog_fr_path = os.path.join(BASE_DIR, "data", "raw", "catalog_fr.csv")
catalog_us_path = os.path.join(BASE_DIR, "data", "raw", "catalog_us.csv")
mapping_path    = os.path.join(BASE_DIR, "data", "raw", "mapping_categories.csv")

output_clean_path = os.path.join(BASE_DIR, "data", "clean", "catalog_canonique.csv")
output_kpi_path   = os.path.join(BASE_DIR, "data", "clean", "kpi_catalog.csv")

# -----------------------------
# 2. Chargement des données
# -----------------------------
print("Chargement des catalogues...")
fr = pd.read_csv(catalog_fr_path)
us = pd.read_csv(catalog_us_path)
mapping = pd.read_csv(mapping_path)

# -----------------------------
# 3. Harmonisation colonnes US
# -----------------------------
us.rename(columns={"currency": "currency_orig"}, inplace=True)

# US → devise USD → conversion en EUR dans price
us["currency"] = "€"

# -----------------------------
# 4. Concat FR + US
# -----------------------------
catalog = pd.concat([fr, us], ignore_index=True)

# -----------------------------
# 5. Conversion poids → kg
# -----------------------------
catalog["weight_kg"] = catalog.apply(
    lambda row: convert_weight_kg(row["weight"], row["weight_unit"]),
    axis=1
)

# -----------------------------
# 6. Conversion prix → euros
# -----------------------------
catalog["price"] = catalog.apply(
    lambda row: convert_price_eur(row["price"], row["currency"]),
    axis=1
)

catalog["currency"] = "€"  # après conversion, tout est en euros

# -----------------------------
# 7. Mapping catégories
# -----------------------------
catalog = catalog.merge(mapping,
                        left_on="category",
                        right_on="source_category",
                        how="left")

catalog["category_name"] = catalog["target_category"]
catalog.drop(columns=["source_category", "target_category"], inplace=True)

# -----------------------------
# 8. Suppression doublons SKU
# -----------------------------
before = catalog.shape[0]
catalog.drop_duplicates(subset=["sku"], keep="first", inplace=True)
after = catalog.shape[0]
print(f"Doublons SKU supprimés : {before - after}")

# -----------------------------
# 9. Colonnes & ordre final
# -----------------------------
catalog_final = catalog[[
    "sku",
    "name",
    "category_name",
    "weight_kg",
    "price",
    "currency"
]]

# -----------------------------
# 10. Export final
# -----------------------------
catalog_final.to_csv(output_clean_path, index=False)
print(f"Catalogue canonique créé → {output_clean_path}")



# -----------------------------
# 11. Génération du KPI 
# -----------------------------
print("Génération des KPI catalogue...")

report_path = os.path.join(BASE_DIR, "data", "reports", "kpi_catalog.csv")
os.makedirs(os.path.dirname(report_path), exist_ok=True)

kpi = {
    "nombre_lignes": len(catalog_final),
    "taux_valeurs_manquantes_%": catalog_final.isna().sum().sum() / catalog_final.size * 100,
    "taux_doublons_sku_%": (1 - catalog_final["sku"].nunique() / len(catalog_final)) * 100,
    "prix_min_eur": catalog_final["price"].min(),
    "prix_max_eur": catalog_final["price"].max(),
    "poids_min_kg": catalog_final["weight_kg"].min(),
    "poids_max_kg": catalog_final["weight_kg"].max(),
}

df_kpi = pd.DataFrame([kpi])
df_kpi.to_csv(report_path, index=False)

print(f"KPI catalogue sauvegardé → {report_path}")
