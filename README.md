# ☕ Cafe Sales Analysis: From Dirty Data to Insights

## 📌 Project Overview
Project ini bertujuan untuk mengubah data transaksi kafe yang kotor dan tidak terstruktur menjadi *actionable insights* bagi pemilik bisnis. Saya mensimulasikan peran sebagai Data Analyst yang bertanggung jawab atas proses *End-to-End*, mulai dari Data Cleaning (Python) hingga pembuatan Dashboard (Tableau).

**Dataset Source:** [Kaggle - Cafe Sales Dirty Data](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training/data)

## 🛠️ Tech Stack
* **Python:** Data Cleaning & Manipulation
* **Pandas & NumPy:** Data Analysis Library
* **Tableau:** Data Visualization (In Progress)

## 🧹 Data Cleaning Process (Python)
Data mentah memiliki banyak masalah kualitas. Berikut adalah langkah perbaikan yang saya lakukan:

1.  **Handling Wrong Data Types:** Mengubah kolom `Date` yang terbaca string menjadi `Datetime`, dan membersihkan simbol mata uang pada kolom angka (`Quantity`, `Price`, `Total`).
2.  **Handling Missing Values:**
    * Mengisi data kategori yang kosong (Location, Payment Method) dengan label "Unknown" untuk menjaga integritas jumlah transaksi.
    * Menghapus (Drop) data tanggal yang kosong (~4%) karena krusial untuk analisis *Time Series*.
3.  **Standardizing Labels:**
    * Memperbaiki format teks (Title Case) agar "coffee" dan "Coffee" dianggap satu produk.
    * Membersihkan label "Error" menjadi "Unknown".
4.  **Logic Validation (Quality Assurance):**
    * Memverifikasi keakuratan matematika: `Quantity` × `Price` = `Total Spent`.
    * Hasil: Data keuangan valid dan siap divisualisasikan.

## 📊 Key Findings (Pre-Visualization)
Berdasarkan analisis Python awal:
* **Total Revenue:** ~$72,704
* **Top Best Seller:** Coffee (~2,968 terjual)
* **Insight:** Metode pembayaran tidak mempengaruhi rata-rata nilai belanja (Rata-rata ~$9 per transaksi).

## 🚀 Next Steps
* [x] Data Cleaning & Validation
* [x] Export Clean Data
* [ ] Build Interactive Dashboard in Tableau (Sales Trend, Best Sellers, Buying Habits)

