"""
PROJECT: CAFE SALES DATA CLEANING & ANALYSIS
---------------------------------------------
Author      : Fachriza Djuanda
Date        : 2026
Description : Skrip ini bertujuan untuk membersihkan 'Dirty Data' transaksi kafe
              menjadi data yang siap untuk visualisasi (Tableau).
Steps       : Data Loading -> Audit -> Cleaning -> Validation -> Export.
"""

import pandas as pd
import numpy as np

# ==============================================================================
# PHASE 1: DATA LOADING & INITIAL ASSESSMENT
# ==============================================================================

# 1.1 Load Data
# Pastikan path file menggunakan raw string (r"...") agar backslash terbaca benar
file_path = r"D:\Project\Data Analyst\Project Cafe Sales\dirty_cafe_sales.csv"
data = pd.read_csv(file_path)

print("--- 1. INITIAL DATA INSPECTION ---")
# Melihat sampel data teratas untuk gambaran awal struktur tabel
print("HEAD:\n", data.head())

# Mengecek tipe data dan keberadaan nilai null (Info)
print("\nINFO:")
print(data.info())

# Melihat anomali statistik (misal: nilai negatif, outlier ekstrem)
print("\nSTATISTIK DESKRIPTIF:")
print(data.describe(include="all"))

# Mengecek total missing values per kolom
print("\nMISSING VALUES AWAL:")
print(data.isnull().sum())

# Mengecek apakah ada baris yang duplikat total
print(f"\nDUPLIKASI DATA: {data.duplicated().sum()}")


# ==============================================================================
# PHASE 2: DATA CLEANING & PREPROCESSING
# ==============================================================================
print("\n--- 2. STARTING DATA CLEANING ---")

# Membuat copy agar data asli (raw data) tetap aman
df_clean = data.copy()

# 2.1 Standardisasi Nama Kolom
# Mengubah format menjadi snake_case (huruf kecil & underscore) agar konsisten
df_clean.columns = df_clean.columns.str.replace(" ", "_").str.lower()
print(f"Column Names Updated: {df_clean.columns}")

# 2.2 Membersihkan Kolom Numerik (Quantity, Price, Total Spent)
# Masalah: Data terdeteksi sebagai Object karena ada simbol '$' dan ','
nums_cols = ["quantity", "price_per_unit", "total_spent"]

for col in nums_cols:
    df_clean[col] = pd.to_numeric(
        df_clean[col].astype(str).str.replace("$", "").str.replace(",", ""),
        errors="coerce",  # Mengubah text error menjadi NaN
    )

print("\nCek Tipe Data Setelah Cleaning Numerik:")
print(df_clean.info())

# 2.3 Membersihkan Kolom Tanggal
# Mengubah ke format datetime agar bisa dilakukan analisis Time Series
df_clean["transaction_date"] = pd.to_datetime(
    df_clean["transaction_date"], errors="coerce"
)

# 2.4 Handling Missing Values (Strategi Penanganan)
# -> Strategi Kategori: Isi dengan "Unknown" agar data transaksi tetap terekam
cat_cols = ["payment_method", "location", "item"]
for col in cat_cols:
    df_clean[col] = df_clean[col].fillna("Unknown")

# -> Strategi Numerik & Tanggal: Hapus (Drop)
# Alasan: Data tanpa Harga, Jumlah, atau Tanggal tidak valid untuk analisis penjualan
cols_critical = ["quantity", "price_per_unit", "total_spent", "transaction_date"]
df_clean = df_clean.dropna(subset=cols_critical)

# 2.5 Finalisasi Struktur Tabel
# Reset index agar urutan baris kembali rapi setelah penghapusan
df_clean = df_clean.reset_index(drop=True)

print(f"\nSisa Data Valid: {df_clean.shape[0]} baris")
print("Sisa Null Values:", df_clean.isnull().sum().sum())


# ==============================================================================
# PHASE 3: TEXT STANDARDIZATION & ERROR HANDLING
# ==============================================================================
print("\n--- 3. TEXT HANDLING ---")

# 3.1 Standardisasi Text (Title Case)
# Mengatasi duplikasi implisit (e.g., "coffee" vs "Coffee")
text_cols = ["item", "payment_method", "location"]
for col in text_cols:
    df_clean[col] = df_clean[col].str.title()

# 3.2 Label Correction
# Mengganti label "Error" atau variannya menjadi "Unknown"
for col in text_cols:
    df_clean[col] = df_clean[col].replace(
        ["Error", "ERROR", "Unknown", "unknown"], "Unknown"
    )

# 3.3 Verifikasi Nilai Unik
# Memastikan tidak ada lagi label aneh yang tersisa
print("\nCheck Unique Values (Final):")
for col in text_cols:
    print(f"[{col.upper()}]:\n{df_clean[col].value_counts(dropna=False)}")
    print("-" * 15)


# ==============================================================================
# PHASE 4: LOGIC VALIDATION (QUALITY ASSURANCE)
# ==============================================================================
print("\n--- 4. DATA VALIDATION ---")

# 4.1 Math Check: Verifikasi Konsistensi Data
# Rumus: Quantity * Price == Total Spent
df_clean["calculated_total"] = df_clean["quantity"] * df_clean["price_per_unit"]

# Toleransi selisih 0.01 untuk menghindari floating point error
mask_salah_hitung = abs(df_clean["total_spent"] - df_clean["calculated_total"]) > 0.01
jumlah_salah = mask_salah_hitung.sum()

print(f"Jumlah Transaksi dengan Perhitungan Salah: {jumlah_salah}")

if jumlah_salah > 0:
    print("Contoh Data Salah:\n", df_clean[mask_salah_hitung].head())

# 4.2 Cleanup Helper Column
if "calculated_total" in df_clean.columns:
    df_clean = df_clean.drop(columns=["calculated_total"])


# ==============================================================================
# PHASE 5: FINAL INSIGHTS & EXPORT
# ==============================================================================
print("\n--- 5. FINAL REPORT ---")

# 5.1 Quick Insights (Sanity Check)
total_revenue = df_clean["total_spent"].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

print("\nTop 5 Items by Quantity:")
print(df_clean.groupby("item")["quantity"].sum().sort_values(ascending=False).head(5))

print("\nAverage Spend per Payment Method:")
print(df_clean.groupby("payment_method")["total_spent"].mean())

# 5.2 Export Data
output_filename = "cafe_sales_clean.csv"
df_clean.to_csv(output_filename, index=False)
print(
    f"\n✅ SUCCESS: File '{output_filename}' berhasil disimpan dan siap untuk visualisasi."
)

# Tampilkan sampel data akhir
print("\nSample Data Akhir:")
print(df_clean.head(10))
