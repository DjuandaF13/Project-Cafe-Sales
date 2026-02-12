# ☕ Cafe Sales Analytics: From Dirty Data to Actionable Insights

![Dashboard Preview](assets/dashboard_final.png)

## 📌 Project Overview
Project ini bertujuan untuk mengubah data transaksi kafe yang kotor dan tidak terstruktur menjadi **dashboard interaktif** yang memberikan wawasan strategis bagi pemilik bisnis. 

Saya mensimulasikan peran sebagai **Data Analyst** yang bertanggung jawab atas proses *End-to-End*:
1.  **Data Cleaning & Recovery:** Menggunakan Python untuk membersihkan data dan memulihkan data yang hilang menggunakan logika bisnis.
2.  **Data Visualization:** Menggunakan Tableau untuk membangun dashboard eksekutif.

**Dataset Source:** [Kaggle - Cafe Sales Dirty Data](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training/data)

---

## 🛠️ The Process: 5-Phase Cleaning Pipeline (Python)

Tantangan terbesar dataset ini adalah kualitas data yang buruk. Saya menerapkan pendekatan berikut di Python:

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
    * **Solusi:** Mengembangkan algoritma logika harga. *Logika: Jika Harga $2.0 selalu merujuk pada "Coffee" di data valid, maka item "Unknown" dengan harga $2.0 dipastikan adalah "Coffee".*
    * **Hasil:** Berhasil memulihkan **~45%** data item yang hilang (Unknown) menjadi data valid.
5.  **Validation & Tableau Compatibility:**
    * Memastikan `Quantity` × `Price` = `Total Spent`.
    * Export ke `.xlsx` menggunakan library `openpyxl` untuk mengatasi isu format regional (koma vs titik) saat import ke Tableau.

---

## 💻 Tech Stack
* **Language:** Python 3.10
* **Libraries:** Pandas, NumPy, OpenPyXL
* **Visualization:** Tableau Public/Desktop
* **Version Control:** Git & GitHub

## 🚀 Project Status
* [x] Data Cleaning & Logic Validation
* [x] Advanced Data Recovery (Imputation)
* [x] Interactive Dashboard in Tableau
* [x] Final Business Analysis & Documentation

## 📊 Executive Summary & Key Insights

Berdasarkan analisis visual dari dashboard final, berikut adalah rangkuman kinerja bisnis dan temuan strategis utama:

### 1. 🗝️ Key Performance Indicators (KPIs)
* **Total Revenue:** **$73,000** (Total Omzet)
* **Total Transactions:** **8,159** (Jumlah Struk)
* **Average Order Value (AOV):** **$8.9** (Rata-rata belanja per transaksi)

### 2. 📈 Sales Performance & Seasonality
* **Mid-Year Peak:** Penjualan mencapai puncaknya di bulan **Juni ($6.4K)**, diikuti oleh Agustus dan Oktober. Ini mengindikasikan adanya tren musiman pertengahan tahun yang kuat.
* **Early Year Slump:** Titik terendah terjadi di bulan **Februari ($5.7K)** dan September ($5.9K). Volatilitas bulanan bergerak di kisaran $5.7K - $6.4K.

### 3. ☕ Product Preferences (The "Healthy" Surprise)
* **Anchor Product:** Sesuai prediksi, **Coffee** adalah produk terlaris (Dominan) dengan total penjualan **3.25K unit**.
* **Health-Conscious Customer Base:** Temuan menarik terlihat pada **Salad (3.14K unit)** yang menempati posisi kedua, mengalahkan *Cake* dan *Juice*.
    * *Insight:* Basis pelanggan kafe ini memiliki preferensi kuat terhadap gaya hidup sehat, bukan sekadar penikmat kopi dan kue.
    * *Action:* Manajemen inventaris harus memprioritaskan kesegaran bahan baku Salad karena perputarannya sangat cepat.

### 4. 💳 Payment Behavior & System Anomaly
* **High Digital Adoption:** Pembayaran non-tunai (*Digital Wallet* + *Credit Card*) mendominasi hampir 50% dari transaksi yang teridentifikasi.
* **Critical System Anomaly:** Terdapat **2.56K transaksi (31%)** dengan metode pembayaran "Unknown".
    * *Warning:* Angka ini sangat tinggi dan berisiko menghambat proses rekonsiliasi keuangan (pencocokan kas). Hal ini mengindikasikan masalah pada sistem POS (*Point of Sales*) atau kelalaian input kasir.

### 5. 💡 Strategic Recommendations
1.  **Preventing the Slump:** Luncurkan kampanye pemasaran khusus (misal: *Valentine's Couple Bundle* atau *Payday Promo*) di bulan **Februari** dan **Mei** untuk mencegah penurunan omzet di periode sepi tersebut.
2.  **Menu Engineering (Bundling):** Produk **Smoothie** berada di posisi penjualan terendah (2.72K). Ada peluang besar untuk membuat paket *bundling* **"Healthy Lunch Set"** (Salad + Smoothie) untuk mendongkrak penjualan kategori minuman tersebut.
3.  **Operational Audit:** Segera lakukan audit teknis pada mesin kasir (POS) dan berikan pelatihan ulang kepada staf untuk meminimalisir input data pembayaran "Unknown".

---
