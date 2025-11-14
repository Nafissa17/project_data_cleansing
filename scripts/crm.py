import pandas as pd
from utils import standardize_email, standardize_country, clean_phone, remove_duplicates, calculate_kpi, parse_date

# Charger le CSV
df = pd.read_csv("../data/raw/clients.csv")

# Renommer les colonnes pour standardiser
df.rename(columns={
    "telephone": "phone",
    "pays": "country",
    "naissance": "signup_date"
}, inplace=True)

# KPI avant nettoyage
kpi_before = calculate_kpi(df, ["email", "country", "phone"])
kpi_before.to_csv("../data/reports/kpi_qualite_clients_before.csv", index=False)

# Nettoyage
df["email"] = df["email"].apply(standardize_email)
df["country"] = df["country"].apply(standardize_country)
df["phone"] = df["phone"].apply(clean_phone)
df["signup_date"] = df["signup_date"].apply(parse_date)

# Suppression doublons sur email + phone
df = remove_duplicates(df, ["email", "phone"])

# KPI après nettoyage
kpi_after = calculate_kpi(df, ["email", "country", "phone"])
kpi_after.to_csv("../data/reports/kpi_qualite_clients_after.csv", index=False)

# Sauvegarde
df.to_csv("../data/clean/clients_clean.csv", index=False)

print("CRM nettoyé ✅")
