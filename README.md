# nusamart-sales-intelligence
Sales analytics dashboard with machine learning forecast

# NusaMart Sales Intelligence

NusaMart Sales Intelligence adalah dashboard analitik penjualan yang dibuat untuk mengolah data transaksi menjadi informasi yang dapat digunakan untuk melihat performa penjualan dan membantu pengambilan keputusan bisnis.

Project ini mencakup proses pengolahan data, exploratory data analysis, visualisasi, hingga prediksi revenue menggunakan Machine Learning.

## Live Demo

[Open Dashboard](https://nusamart-sales-intelligence.streamlit.app/)

## Features

- Menampilkan KPI penjualan
- Melihat tren revenue bulanan
- Membandingkan revenue berdasarkan kategori
- Melihat produk dengan revenue tertinggi
- Menganalisis revenue berdasarkan kota
- Melakukan prediksi revenue bulan berikutnya

## Dataset

Dataset yang digunakan merupakan dataset transaksi sintetis dengan **10.000 transaksi** dari Januari 2024 hingga Agustus 2025.

Beberapa informasi yang tersedia:

- Tanggal transaksi
- Produk
- Kategori
- Harga
- Jumlah pembelian
- Customer
- Kota
- Diskon
- Metode pembayaran
- Revenue

> Dataset digunakan untuk keperluan pembelajaran dan portfolio, bukan merupakan data bisnis nyata.

## Exploratory Data Analysis

Analisis yang dilakukan meliputi:

- Total revenue dan jumlah transaksi
- Revenue berdasarkan kategori
- Revenue berdasarkan produk
- Jumlah produk terjual
- Revenue per unit
- Tren revenue bulanan
- Tren quantity bulanan
- Revenue berdasarkan kota

### Beberapa hasil analisis

- **Electronics** menjadi kategori dengan revenue tertinggi.
- **Laptop A** menjadi produk dengan revenue tertinggi.
- **Desember 2024** memiliki revenue bulanan tertinggi, yaitu sekitar **Rp1,69 miliar**.
- Kategori Home memiliki revenue per unit lebih tinggi dibandingkan Fashion meskipun jumlah unit terjual lebih sedikit.

## Sales Forecast

Untuk memprediksi revenue bulan berikutnya, digunakan algoritma **Random Forest Regressor**.

Fitur yang digunakan:

- Revenue 1 bulan sebelumnya
- Revenue 2 bulan sebelumnya
- Revenue 3 bulan sebelumnya
- Bulan
- Tahun

Model menggunakan konfigurasi:

```python
RandomForestRegressor(
    n_estimators=200,
    max_depth=5,
    random_state=42
)

Beberapa konfigurasi fitur dibandingkan menggunakan data historis. Model dengan fitur lag revenue dan fitur waktu memberikan hasil terbaik dari model yang diuji berdasarkan MAE dan RMSE.

Karena dataset yang digunakan merupakan dataset sintetis dengan jumlah data bulanan yang terbatas, hasil forecasting pada project ini digunakan sebagai demonstrasi penerapan Machine Learning.

## Tech Stack
- Python
- Pandas
= Scikit-learn
- Matplotlib
- Streamlit
- GitHub
- Streamlit Community Cloud

## Project Structure
nusamart-sales-intelligence/
│
├── app.py
├── nusamart_sales.csv
├── requirements.txt
└── README.md

```
## Workflow

```Transaction Data
      ↓
Data Processing
      ↓
EDA & Visualization
      ↓
Business Insights
      ↓
Feature Engineering
      ↓
Random Forest
      ↓
Sales Forecast
      ↓
Streamlit Dashboard

## Future Development
Beberapa pengembangan yang masih dapat dilakukan:
- Menambahkan filter berdasarkan tanggal, kategori, produk, dan kota
- Menambahkan analisis customer
- Mencoba model forecasting lainnya
- Menambahkan rekomendasi bisnis berdasarkan hasil analisis
- Meningkatkan tampilan dan interaksi dashboard


## Author
Sifaul Hikmah
S.Kom — Informatics Engineering
Interested in Data, Machine Learning, AI, and Web Development.
