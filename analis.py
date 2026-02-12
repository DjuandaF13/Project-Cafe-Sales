"""
PROJECT: CAFE SALES DATA CLEANING & ANALYSIS
---------------------------------------------
Author      : Fachriza Djuanda
Date        : 2026
Description : Skrip ini bertujuan untuk membersihkan 'Dirty Data' transaksi kafe
              menjadi data yang siap untuk visualisasi (Tableau).
Steps       : Data Loading -> Audit -> Cleaning -> Advanced Recovery -> Export.
"""

import pandas as pd
import numpy as np

# ==============================================================================
# PHASE 1: DATA LOADING & INITIAL ASSESSMENT
# ==============================================================================
print("--- 1. INITIAL DATA INSPECTION ---")

# 1.1 Load Data
# Menggunakan raw string (r"...") untuk path file windows
file_path = r"D:\Project\Data Analyst\Project Cafe Sales\dirty_cafe_sales.csv"
data = pd.read_csv(file_path)

# 1.2 Audit Awal
print("HEAD (Sampel Data):\n", data.head())
print("\nINFO (Tipe Data & Null):")
print(data.info())
print("\nSTATISTIK DESKRIPTIF (Cek Anomali):")
print(data.describe(include="all"))
print("\nMISSING VALUES AWAL:")
print(data.isnull().sum())
print(f"\nDUPLIKASI DATA: {data.duplicated().sum()}")


# ==============================================================================
# PHASE 2: BASIC DATA CLEANING & PREPROCESSING
# ==============================================================================
print("\n--- 2. STARTING DATA CLEANING ---")

# Buat copy agar data asli aman
df_clean = data.copy()

# 2.1 Standardisasi Nama Kolom (Snake Case)
df_clean.columns = df_clean.columns.str.replace(" ", "_").str.lower()
print(f"Column Names Updated: {df_clean.columns}")

# 2.2 Membersihkan Kolom Numerik
# Menghapus simbol '$' dan ',' lalu convert ke Float/Int
nums_cols = ["quantity", "price_per_unit", "total_spent"]
for col in nums_cols:
    df_clean[col] = pd.to_numeric(
        df_clean[col].astype(str).str.replace("$", "").str.replace(",", ""),
        errors="coerce",  # Ubah text error jadi NaN
    )

# 2.3 Membersihkan Kolom Tanggal
df_clean["transaction_date"] = pd.to_datetime(
    df_clean["transaction_date"], errors="coerce"
)

# 2.4 Handling Missing Values (Basic Strategy)
# -> Kategori: Isi dengan "Unknown"
cat_cols = ["payment_method", "location", "item"]
for col in cat_cols:
    df_clean[col] = df_clean[col].fillna("Unknown")

# -> Numerik & Tanggal: Drop (Hapus) baris yang kosong
cols_critical = ["quantity", "price_per_unit", "total_spent", "transaction_date"]
df_clean = df_clean.dropna(subset=cols_critical)

# 2.5 Finalisasi Index
df_clean = df_clean.reset_index(drop=True)

print(f"\nSisa Data Valid setelah Basic Cleaning: {df_clean.shape[0]} baris")


# ==============================================================================
# PHASE 3: TEXT STANDARDIZATION
# ==============================================================================
print("\n--- 3. TEXT HANDLING ---")

# 3.1 Title Casing (Agar 'coffee' == 'Coffee')
text_cols = ["item", "payment_method", "location"]
for col in text_cols:
    df_clean[col] = df_clean[col].str.title()

# 3.2 Label Correction (Error -> Unknown)
for col in text_cols:
    df_clean[col] = df_clean[col].replace(
        ["Error", "ERROR", "Unknown", "unknown"], "Unknown"
    )

print("Text Standardization Complete.")


# ==============================================================================
# PHASE 4: ADVANCED VALIDATION & DATA RECOVERY
# ==============================================================================
print("\n--- 4. ADVANCED VALIDATION & RECOVERY ---")

# 4.1 Math Check (Validasi Logika)
# Rumus: Quantity * Price harus sama dengan Total Spent
df_clean["calculated_total"] = df_clean["quantity"] * df_clean["price_per_unit"]
mask_salah_hitung = abs(df_clean["total_spent"] - df_clean["calculated_total"]) > 0.01
jumlah_salah = mask_salah_hitung.sum()

print(f"Validasi Matematika - Jumlah Transaksi Salah Hitung: {jumlah_salah}")

# Cleanup kolom bantuan
if "calculated_total" in df_clean.columns:
    df_clean = df_clean.drop(columns=["calculated_total"])

# 4.2 Deductive Imputation (Misi Penyelamatan Data Unknown)
# Logika: Jika Harga $X selalu merujuk pada Item Y, maka Item Unknown dengan Harga $X pasti Item Y.

print("\n--- MENJALANKAN MISI PENYELAMATAN DATA ---")
# Buat Peta Harga dari data yang valid
price_map = (
    df_clean[df_clean["item"] != "Unknown"].groupby("price_per_unit")["item"].unique()
)
mapping_dict = {}

for price, items in price_map.items():
    if len(items) == 1:
        # HOKI! 1 Harga = 1 Item
        mapping_dict[price] = items[0]

# Eksekusi Pengisian Unknown
unknown_awal = (df_clean["item"] == "Unknown").sum()


def fill_unknown_items(row):
    if row["item"] == "Unknown" and row["price_per_unit"] in mapping_dict:
        return mapping_dict[row["price_per_unit"]]
    return row["item"]


df_clean["item"] = df_clean.apply(fill_unknown_items, axis=1)
unknown_akhir = (df_clean["item"] == "Unknown").sum()

print(f"Item 'Unknown' Awal  : {unknown_awal}")
print(f"Item 'Unknown' Akhir : {unknown_akhir}")
print(f"✅ Data Berhasil Diselamatkan : {unknown_awal - unknown_akhir} baris")


# ==============================================================================
# PHASE 5: FINAL INSIGHTS & EXPORT
# ==============================================================================
print("\n--- 5. FINAL REPORT & EXPORT ---")

# 5.1 Quick Insights
total_revenue = df_clean["total_spent"].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

print("\nTop 5 Items by Quantity (Final):")
print(df_clean.groupby("item")["quantity"].sum().sort_values(ascending=False).head(5))

# 5.2 Export Data (CSV & Excel)
# Export CSV
csv_filename = "cafe_sales_clean.csv"
df_clean.to_csv(csv_filename, index=False)
print(f"\n✅ CSV Saved: '{csv_filename}'")

# Export Excel (Recommended for Tableau to fix decimal issues)
xlsx_filename = "cafe_sales_final.xlsx"
df_clean.to_excel(xlsx_filename, index=False)
print(f"✅ Excel Saved: '{xlsx_filename}' (Gunakan file ini untuk Tableau)")

print("\nSample Data Akhir:")
print(df_clean.head(10))
