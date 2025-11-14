import pandas as pd
import re

# -------------------------
# Fonctions de nettoyage CRM
# -------------------------
def standardize_email(email):
    if pd.isna(email):
        return None
    return email.strip().lower()

def standardize_country(country):
    if pd.isna(country):
        return None
    mapping = {"FR": "France", "USA": "United States", "DE": "Germany", "UK": "United Kingdom"}
    return mapping.get(country.upper(), country.title())

def clean_phone(phone):
    if pd.isna(phone):
        return None
    phone = re.sub(r'\D', '', str(phone))
    if len(phone) == 10:
        return f"+33{phone[1:]}"  # exemple France
    return phone

def remove_duplicates(df, subset_cols):
    return df.drop_duplicates(subset=subset_cols, keep='first')

def calculate_kpi(df, column_list):
    rows = []
    for col in column_list:
        rows.append({
            "column": col,
            "missing": df[col].isna().sum(),
            "unique": df[col].nunique()
        })
    return pd.DataFrame(rows)

# -------------------------
# Fonctions catalogue 
# -------------------------
def convert_weight_kg(weight, unit):
    if pd.isna(weight):
        return None
    try:
        weight = float(weight)
    except:
        return None
    unit = str(unit).lower()
    if unit in ['g', 'gramme', 'grams']:
        return round(weight / 1000, 3)
    elif unit in ['kg']:
        return weight
    elif unit in ['lb', 'lbs']:
        return round(weight * 0.453592, 3)
    elif unit in ['oz']:
        return round(weight * 0.0283495, 3)
    else:
        return weight  # si unité inconnue, on laisse tel quel

def convert_price_eur(price, currency):
    if pd.isna(price):
        return None
    try:
        price = float(price)
    except:
        return None
    currency = str(currency).upper()
    if currency in ['$', 'USD']:
        return round(price * 0.92, 2)  # taux fictif USD->EUR
    elif currency in ['EUR', '€']:
        return price
    else:
        return price  # si devise inconnue, on laisse tel quel


# -------------------------
# Fonctions ventes
# -------------------------
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
    except:
        return pd.NaT
