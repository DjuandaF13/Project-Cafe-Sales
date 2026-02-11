import pandas as pd
import numpy as np

# Import data from CSV
data = pd.read_csv("D:\Project\Data Analyst\Project Cafe Sales\dirty_cafe_sales.csv")

# Cek 5 Baris Teratas
print(data.head())

# Cek Info Data
print(data.info())

# Cek Deskripsi Statistik
print(data.describe(include="all"))

# Cek Missing Values
print(data.isnull().sum())

# Cek Duplikasi Data
print(data.duplicated().sum())

# Tahap Normalisasi dan Data Cleaning
df_clean = data.copy()

# Merapikan nama kolom (ganti spasi dengan underscore dan huruf kecil)
df_clean.columns = df_clean.columns.str.replace(" ", "_").str.lower()
print(df_clean.columns)

# Membersihkan data numerik (Quantity, Price, Total Spent)

# Hapus simbol '$' atau ',' jika ada, lalu ubah ke numerik
# errors='coerce' akan mengubah text seperti 'ERROR' atau 'Unknown' menjadi NaN
nums_cols = ["quantity", "price_per_unit", "total_spent"]
for col in nums_cols:
    df_clean[col] = pd.to_numeric(
        df_clean[col].astype(str).str.replace("$", "").str.replace(",", ""),
        errors="coerce",
    )

# Cek hasil pembersihan data numerik
print(df_clean.info())

# membersihkan data tanggal (transaction_date)
# Ubah ke format datetime, errors='coerce' akan mengubah format yang tidak sesuai
df_clean["transaction_date"] = pd.to_datetime(
    df_clean["transaction_date"], errors="coerce"
)
# Cek hasil pembersihan data tanggal
print(df_clean.info())

# Handling the missing values
# Isi data kategori yang kosong dengan "Unknown"
cat_cols = ["payment_method", "location", "item"]
for col in cat_cols:
    df_clean[col] = df_clean[col].fillna("Unknown")

# Khusus data numerik: Karena kita butuh akurasi penjualan,
# baris yang Quantity ATAU Price-nya kosong (NaN) lebih baik kita hapus (drop)
# karena kita tidak bisa menebak berapa duit yang masuk.
df_clean = df_clean.dropna(subset=["quantity", "price_per_unit", "total_spent"])
print("Sisa data setelah drop missing values pada kolom numerik:", df_clean.shape)
# Cek kembali missing values setelah pembersihan
print(df_clean.isnull().sum())

# handling missing dates
# Drop baris dengan tanggal transaksi yang kosong
df_clean = df_clean.dropna(subset=["transaction_date"])

# reset index setelah drop rows
df_clean = df_clean.reset_index(drop=True)

# Cek ulang data bersih dari null
print("Sisa Null : ", df_clean.isnull().sum())
print("total data setelah cleaning : ", df_clean.shape)


# -- HANDLING DUPLIKASI DATA --
# Cek duplikasi data
duplicates = df_clean.duplicated()
print("Jumlah duplikasi sebelum dihapus : ", duplicates.sum())
# Tidak ada yang perlu dihapus karena tidak ada duplikasi

# Standarisasi format teks
# Standardisasi Teks (Semua jadi huruf kapital awal - Title Case)
# Agar "coffee" dan "Coffee" dianggap barang yang sama
df_clean["item"] = df_clean["item"].str.title()
df_clean["payment_method"] = df_clean["payment_method"].str.title()
df_clean["location"] = df_clean["location"].str.title()

# Cek data bersih akhir
print("Info Final : ", df_clean.info())
# contoh data bersih
print(df_clean.head(13))

# pembersihan lanjutan
# cek value distinct pada kolom item, payment_method, location
cols_to_check = ["item", "payment_method", "location"]
for col in cols_to_check:
    print(f"\n--- NILAI UNIK DI KOLOM: {col.upper()} ---")
    # Kita pakai value_counts() agar terlihat juga jumlah datanya
    # dropna=False agar kalau ada NaN yang tersisa, dia muncul
    print(df_clean[col].value_counts(dropna=False))
    print("-" * 15)

# Mengganti semua label error menjadi unknown
cols_to_fix = ["item", "payment_method", "location"]
for cols in cols_to_fix:
    df_clean[cols] = df_clean[cols].replace(
        ["Error", "ERROR", "Unknown", "unknown"], "Unknown"
    )

# Cek ulang value distinct setelah pembersihan lanjutan
for col in cols_to_check:
    print(
        f"\n--- NILAI UNIK DI KOLOM: {col.upper()} (SETELAH PEMBERSIHAN LANJUTAN) ---"
    )
    print(df_clean[col].value_counts(dropna=False))
    print("-" * 15)

# Validasi logika matematika ( Math check)
# hitung ulang total seharusnya
df_clean["calculated_total"] = df_clean["quantity"] * df_clean["price_per_unit"]

# Cari selisih (toleransi o.01)
mask_salah_hitung = abs(df_clean["total_spent"] - df_clean["calculated_total"]) > 0.01
jumlah_salah = mask_salah_hitung.sum()
print(f"Jumlah transaksi dengan hitungan salah: {jumlah_salah}")

print(df_clean.head(50))

# Final Check
# apus kolom bantuan 'calculated_total' (karena isinya sama persis dengan total_spent)
if "calculated_total" in df_clean.columns:
    df_clean = df_clean.drop(columns=["calculated_total"])

# Cek insight sederhana
# memastikan angka masuk akal
print("--- TOTAL PENDAPATAN (REVENUE) ---")
print(f"${df_clean['total_spent'].sum():,.2f}")

print("\n--- TOP 5 ITEM TERLARIS (Quantity) ---")
print(df_clean.groupby("item")["quantity"].sum().sort_values(ascending=False).head(5))

print("\n--- RATA-RATA TRANSAKSI PER METODE BAYAR ---")
print(df_clean.groupby("payment_method")["total_spent"].mean())

# XPORT KE CSV BARU
df_clean.to_csv("cafe_sales_clean.csv", index=False)
print("\n✅ File 'cafe_sales_clean.csv' berhasil disimpan!")
