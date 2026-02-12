# ☕ Cafe Sales Analysis: From Dirty Data to Insights

## 📌 Project Overview
Project ini bertujuan untuk mengubah data transaksi kafe yang kotor dan tidak terstruktur menjadi *actionable insights* bagi pemilik bisnis. Saya mensimulasikan peran sebagai Data Analyst yang bertanggung jawab atas proses *End-to-End*, mulai dari Data Cleaning (Python) hingga pembuatan Dashboard (Tableau).

**Dataset Source:** [Kaggle - Cafe Sales Dirty Data](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training/data)

## 🛠️ Tech Stack
* **Python:** Data Cleaning & Manipulation
* **Pandas & NumPy:** Data Analysis Library
* **Tableau:** Data Visualization (In Progress)

## 🧹 Data Cleaning & Recovery Process (Python)
Saya melakukan proses pembersihan data yang komprehensif dengan pendekatan **5-Phase Pipeline**:

1.  **Handling Wrong Data Types:** * Mengonversi `Transaction Date` ke format Datetime.
    * Membersihkan karakter non-numerik ($, ,) pada kolom `Quantity`, `Price`, dan `Total`.
2.  **Handling Missing Values:**
    * Mengisi kekosongan pada kategori (Location, Payment) dengan label "Unknown".
    * Menghapus data transaksi yang tidak memiliki informasi krusial (Tanggal/Harga).
3.  **Text Standardization:**
    * Mengatasi inkonsistensi teks (e.g., "coffee" vs "Coffee") menggunakan Title Casing.
    * Mengubah label "Error" menjadi "Unknown".
4.  **🕵️ Advanced Data Recovery (Deductive Imputation):**
    * **Masalah:** Banyak item berlabel "Unknown" meskipun memiliki harga yang valid.
    * **Solusi:** Saya mengembangkan algoritma untuk memetakan pola `Harga Unik` ke `Nama Item`.
    * **Logika:** Jika Harga $X *selalu* merujuk pada Item Y dalam data valid, maka Item "Unknown" dengan harga $X dipastikan adalah Item Y.
    * **Hasil:** Berhasil memulihkan **~45%** data item yang hilang (Unknown) menjadi data valid, meningkatkan akurasi analisis Best Seller.
5.  **Validation & Export:**
    * Memastikan `Quantity` × `Price` = `Total Spent` (Math Check).
    * **Tableau Compatibility:** Mengekspor data ke format `.xlsx` (Excel) menggunakan library `openpyxl` untuk memastikan format angka dan desimal terbaca sempurna oleh Tableau (mengatasi isu Regional Settings).

## 🛠️ Tech Stack Updated
* **Python:** Pandas, NumPy
* **Library Tambahan:** `openpyxl` (untuk export Excel)
* **Tableau:** Data Visualization

## 📊 Key Findings (Pre-Visualization)
Berdasarkan analisis Python awal:
* **Total Revenue:** ~$72,704
* **Top Best Seller:** Coffee (~2,968 terjual)
* **Insight:** Metode pembayaran tidak mempengaruhi rata-rata nilai belanja (Rata-rata ~$9 per transaksi).

## 🚀 Next Steps
* [x] Data Cleaning & Validation
* [x] Export Clean Data
* [ ] Build Interactive Dashboard in Tableau (Sales Trend, Best Sellers, Buying Habits)

