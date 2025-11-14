import pandas as pd
import os

# -------------------------
# CHEMINS DE FICHIERS
# -------------------------
RAW_DATA_PATH = "../data/raw/sales.csv"
CLEAN_DATA_PATH = "../data/clean/sales_clean.csv"
REFUNDS_PATH = "../data/reports/refunds.csv"
REPORT_PATH = "../data/reports/daily_revenue.csv"

# Créer les dossiers de sortie si nécessaire
os.makedirs(os.path.dirname(CLEAN_DATA_PATH), exist_ok=True)
os.makedirs(os.path.dirname(REFUNDS_PATH), exist_ok=True)
os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

# -------------------------
# FONCTION DE CHARGEMENT
# -------------------------
def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Le fichier source n'existe pas: {path}")
    df = pd.read_csv(path)
    print(f"{len(df)} lignes chargées depuis {path}")
    return df

# -------------------------
# PIPELINE DE NETTOYAGE
# -------------------------
def clean_sales_data(df):
    # Convertir les dates et les montants
    df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True, errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    
    # Supprimer les lignes invalides
    df = df.dropna(subset=["order_date", "amount"])
    
    # Trier et supprimer les doublons
    df = df.sort_values("amount", ascending=False)
    df = df.drop_duplicates(subset=["order_id","customer_email"])
    
    # Séparer ventes et remboursements
    df_clean = df[df["amount"] >= 0]
    refunds = df[df["amount"] < 0]
    
    return df_clean, refunds

# -------------------------
# RAPPORT JOURNALIER
# -------------------------
def generate_daily_report(df_clean):
    report = (df_clean
              .groupby(df_clean["order_date"].dt.date)["amount"]
              .sum()
              .reset_index(name="daily_revenue"))
    return report

# -------------------------
# MAIN
# -------------------------
def main():
    df = load_data(RAW_DATA_PATH)
    
    df_clean, refunds = clean_sales_data(df)
    
    # Sauvegarder les fichiers nettoyés
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)
    refunds.to_csv(REFUNDS_PATH, index=False)
    
    report = generate_daily_report(df_clean)
    report.to_csv(REPORT_PATH, index=False)
    
    print("\nTraitement terminé !")
    print(f"  Ventes nettoyées : {CLEAN_DATA_PATH}")
    print(f"  Remboursements : {REFUNDS_PATH}")
    print(f"  Rapport journalier : {REPORT_PATH}")

if __name__ == "__main__":
    main()
