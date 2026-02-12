# ☕ Cafe Sales Analytics: From Dirty Data to Actionable Insights

![Dashboard Preview](assets/dashboard_final.png)
*(Pastikan Anda mengupload screenshot dashboard ke folder 'assets' dan sesuaikan nama filenya)*

## 📌 Project Overview
Project ini bertujuan untuk mengubah data transaksi kafe yang kotor dan tidak terstruktur menjadi **dashboard interaktif** yang memberikan wawasan strategis bagi pemilik bisnis. 

Saya mensimulasikan peran sebagai **Data Analyst** yang bertanggung jawab atas proses *End-to-End*:
1.  **Data Cleaning & Recovery:** Menggunakan Python untuk membersihkan data dan memulihkan data yang hilang menggunakan logika bisnis.
2.  **Data Visualization:** Menggunakan Tableau untuk membangun dashboard eksekutif.

**Dataset Source:** [Kaggle - Cafe Sales Dirty Data](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training/data)

---

## 📊 Executive Summary (Dashboard Insights)

Berdasarkan analisis visual dari dashboard final, berikut adalah kinerja bisnis secara keseluruhan:

### 1. Key Performance Indicators (KPIs)
* **Total Revenue:** **$73,000** (Omzet Total)
* **Total Transactions:** **8,159** (Jumlah Struk)
* **Average Order Value (AOV):** **$8.9** (Rata-rata belanja per orang)

### 2. Tren Penjualan & Musiman
* **Volatilitas Bulanan:** Penjualan bergerak fluktuatif antara **$5.7K - $6.4K**.
* **Peak Performance:** Bulan **Juni ($6.4K)** mencatat penjualan tertinggi, diikuti Agustus dan Oktober.
* **Low Performance:** Penurunan signifikan terjadi di bulan **Februari ($5.7K)**. Diperlukan strategi pemasaran khusus (misal: Promo Valentine) untuk mencegah penurunan di periode ini tahun depan.

### 3. Produk Terlaris (Product Mix)
* **Anchor Product:** **Coffee (3.25K unit)** adalah produk paling dominan.
* **Health Conscious Customers:** Menariknya, **Salad (3.14K unit)** berada di posisi kedua, mengalahkan *Cake* dan *Juice*. Ini menunjukkan segmen pelanggan kafe ini sangat peduli kesehatan.
* **Bundling Opportunity:** *Smoothie* berada di posisi terbawah (2.72K). Ada peluang besar untuk membuat paket *bundling* "Healthy Lunch" (Salad + Smoothie) untuk mendongkrak penjualan Smoothie.

### 4. Anomali Sistem Pembayaran
* Meskipun pembayaran Cash, Credit Card, dan Digital Wallet terdistribusi merata (~1.8K transaksi masing-masing), terdapat **2.56K transaksi (31%)** yang tercatat sebagai "Unknown".
* **Rekomendasi:** Perlu dilakukan audit pada sistem POS (Point of Sales) atau pelatihan kasir, karena data pembayaran yang hilang ini menghambat rekonsiliasi keuangan yang akurat.

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

Berdasarkan analisis visual dari dashboard final, berikut adalah temuan strategis utama untuk kinerja bisnis kafe:

### 1. 📈 Sales Performance & Seasonality
* **Total Revenue:** Mencapai **$73,000** dengan total **8,159 transaksi**.
* **Mid-Year Peak:** Penjualan mencapai puncaknya di bulan **Juni ($6.4K)**, diikuti oleh Agustus dan Oktober. Ini mengindikasikan adanya tren musiman pertengahan tahun yang kuat.
* **Early Year Slump:** Titik terendah terjadi di bulan **Februari ($5.7K)**.
    * *Rekomendasi:* Diperlukan strategi promosi khusus (misal: *Valentine's Bundle* atau *Payday Promo*) di bulan Februari dan Mei untuk mencegah penurunan omzet di tahun berikutnya.

### 2. ☕ Product Preferences (The "Healthy" Surprise)
* **Coffee is King:** Seperti yang diprediksi, **Coffee** adalah produk terlaris dengan **3.25K terjual**.
* **Health-Conscious Customers:** Temuan menarik terlihat pada **Salad (3.14K)** yang menempati posisi kedua, mengalahkan *Cake* dan *Juice*.
    * *Insight:* Basis pelanggan kafe ini memiliki preferensi kuat terhadap makanan sehat.
    * *Action:* Stok bahan baku segar untuk Salad harus menjadi prioritas manajemen inventaris.

### 3. 💳 Payment Behavior & Operational Risks
* **Digital Adoption:** Pembayaran non-tunai (*Digital Wallet* + *Credit Card*) mendominasi hampir 50% dari transaksi yang teridentifikasi.
* **System Anomaly (Critical):** Terdapat **2.56K transaksi (31%)** dengan metode pembayaran "Unknown".
    * *Warning:* Angka ini sangat tinggi dan berisiko bagi rekonsiliasi keuangan.
    * *Action:* Manajemen perlu segera melakukan audit pada sistem POS (*Point of Sales*) atau memberikan pelatihan ulang kepada kasir untuk meminimalisir input data yang kosong.

### 4. 💡 Strategic Opportunities
* **Bundling Strategy:** Produk **Smoothie** berada di posisi terendah (2.72K). Ada peluang besar untuk membuat paket *bundling* **"Healthy Lunch Set"** (Salad + Smoothie) untuk mendongkrak penjualan kategori minuman sehat tersebut.

---
*Connect with me on LinkedIn to discuss more about Data Analysis!*