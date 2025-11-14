import os
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Chemins vers les fichiers clean
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
clients_file = os.path.join(BASE_DIR, "data", "clean", "clients_clean.csv")
catalog_file = os.path.join(BASE_DIR, "data", "clean", "catalog_canonique.csv")
sales_file = os.path.join(BASE_DIR, "data", "clean", "sales_clean.csv")

# -------------------------------
# Vérification existence fichiers
# -------------------------------
for f in [clients_file, catalog_file, sales_file]:
    if not os.path.exists(f):
        raise FileNotFoundError(f"Le fichier attendu est manquant : {f}")

# -------------------------------
# Visualisation 1 : Clients
# -------------------------------
df_clients = pd.read_csv(clients_file)

plt.figure(figsize=(6,4))
df_clients['pays'] = df_clients['pays'].fillna('Unknown')
df_clients['pays'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Répartition des clients par pays")
plt.ylabel("Nombre de clients")
plt.xlabel("Pays")
plt.tight_layout()
plt.show()

# -------------------------------
# Visualisation 2 : Catalogue produits
# -------------------------------
df_catalog = pd.read_csv(catalog_file)

plt.figure(figsize=(8,4))
if 'category_name' in df_catalog.columns:
    df_catalog['category_name'].value_counts().plot(kind='bar', color='lightgreen')
    plt.title("Répartition des produits par catégorie")
    plt.ylabel("Nombre de produits")
    plt.xlabel("Catégorie")
    plt.tight_layout()
    plt.show()
else:
    print("Colonne 'category_name' introuvable dans le catalogue. Pas de graphique produit.")

# -------------------------------
# Visualisation 3 : Ventes quotidiennes
# -------------------------------
df_sales = pd.read_csv(sales_file)

# Conversion des dates
if 'order_date' in df_sales.columns:
    df_sales['order_date'] = pd.to_datetime(df_sales['order_date'], errors='coerce')
else:
    raise KeyError("Colonne 'order_date' introuvable dans les ventes.")

# Conversion des montants en euros (exemple)
def convert_to_eur(amount, currency):
    if currency.upper() in ['USD', '$']:
        return amount * 0.92  # taux fictif USD->EUR
    return amount

df_sales['amount_eur'] = df_sales.apply(lambda x: convert_to_eur(x['amount'], x['currency']), axis=1)

# Chiffre d'affaires 
daily_revenue = df_sales.groupby(df_sales['order_date'].dt.date)['amount_eur'].sum()

plt.figure(figsize=(10,4))
daily_revenue.plot(kind='line', marker='o', color='coral')
plt.title("Chiffre d'affaires(€)")
plt.ylabel("Montant (€)")
plt.xlabel("Date")
plt.tight_layout()
plt.show()
