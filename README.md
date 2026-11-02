# Executive Supermarket Sales & Customer Analytics Dashboard

An interactive, multi-dimensional Business Intelligence dashboard built with Python and Streamlit to analyze supermarket transaction data, customer behavior, hourly peak traffic, and product profitability.

🔗 **Live Interactive Dashboard:** [https://dashboard-supermarket-7xrwudjfgvvkmghtzgawwr.streamlit.app/]

---

## Business Overview & Objective
Supermarkets handle vast transaction data daily, but raw numbers rarely explain *why* sales fluctuate. This project bridges data engineering and analytical decision-making by transforming raw transaction logs into an executive-grade dashboard.

Key objectives:
1. Identify high-revenue vs. high-volume product categories.
2. Track customer foot traffic patterns across hourly and daily cycles.
3. Compare purchasing power across customer roles (Member vs. Normal) and payment preferences.

---

## Tech Stack & Libraries
- **Language:** Python 3.10+
- **Data Manipulation:** Pandas
- **Interactive Web Framework:** Streamlit
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

---

## Key Features
- **Dynamic Global Filters:** Filter data by City, Customer Type (Member/Normal), Gender, and Payment Method.
- **Multi-Metric Lens Toggle:** Instantly switch all dashboard charts between **Sales ($)**, **Quantity (Units)**, and **Transaction Count**.
- **Time-Series Analysis:** 24-hour peak hour tracking (`10:00` - `20:00`) and ordered weekday trend analysis (`Monday` - `Sunday`).
- **Financial Breakdown:** Direct comparison between Cost of Goods Sold (COGS), Gross Income, and Customer Satisfaction Ratings.

---

## Key Business Insights
- **Peak Operational Hours:** Foot traffic peaks twice a day—first at **13:00** (103 transactions) and highest at **19:00** (113 transactions).
- **Product Revenue vs. Volume:** *Food & Beverages* generated the highest total revenue (**$56,144.84**), whereas *Electronic Accessories* moved the highest volume (**971 units**).
- **Member Contribution:** Loyalty Members generate **~58.7%** of total revenue ($189.69K from 565 transactions), significantly outperforming non-member shoppers.
- **Weekly Traffic:** **Saturday** is the highest volume sales day ($56,120.81), while **Monday** is the quietest ($37,899.08).

---

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/USERNAME/dashboard-supermarket.git](https://github.com/USERNAME/dashboard-supermarket.git)
   cd dashboard-supermarket
   ```
2. **Install dependencies:
   ```bash
   pip install pandas streamlit
   ```
3. **Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Executive Summary & Business Insights

* **Staffing & Operational Efficiency:**
  * **Temuan:** Lonjakan transaksi terjadi di dua titik waktu: jam makan siang (**13:00**) dengan 103 transaksi dan puncak tertinggi pada malam hari (**19:00**) dengan 113 transaksi. Antrean mendadak sepi setelah pukul 20:00.
  * **Rekomendasi:** Alokasikan jumlah staf kasir maksimum pada rentang pukul **12:30–14:00** dan **18:30–20:00**. Penambahan kasir di luar jam ini tidak efisien secara biaya operasional.

* **Strategi Produk (*Revenue vs Volume Matrix*):**
  * **Temuan:** Kategori *Food & Beverages* memimpin total omzet (**$56,144.84**) dan profit kotor (**$2,673.56**), sedangkan *Electronic Accessories* unggul dari segi kuantitas barang keluar (**971 unit**). Kategori *Health & Beauty* berada di posisi paling buncit ($49,193.74).
  * **Rekomendasi:** Letakkan produk *Health & Beauty* di dekat kasir atau area lalu lintas tinggi sebagai barang impulsif (*impulse buying*). Lakukan *cross-selling* dengan memasangkan barang elektronik cepat laku bersama perlengkapan gaya hidup.

* **Optimasasi Hari Penjualan (*Weekly Promotion*):**
  * **Temuan:** **Sabtu** mencatat penjualan tertinggi (**$56,120.81**), sementara **Senin** mengalami penurunan drastis (**$37,899.08**).
  * **Rekomendasi:** Buat kampanye diskon khusus hari Senin (*"Monday Madness"* atau promo *cashback* e-wallet) untuk memicu kedatangan pembeli di hari sepi.

* **Nilai Pelanggan (*Member Loyalty Value*):**
  * **Temuan:** Pemegang kartu keanggotaan (*Member*) menyumbang **$189,694.76** (58.7% dari total pendapatan) dibanding pelanggan biasa (*Normal*) sebesar **$133,271.99**.
  * **Rekomendasi:** Perkuat program insentif pendaftaran *Member* di kasir saat checkout, karena retensi *Member* terbukti memberikan kepastian pendapatan yang jauh lebih tinggi.

---

## 3. Draft Post LinkedIn (Portfolio Showcase)

Copy-paste draf berikut ke LinkedIn milikmu, dan jangan lupa lampirkan *screenshot* visual *dashboard*-mu:

```text
🚀 Excited to share my latest End-to-End Data Analytics Project: Executive Supermarket Analytics Dashboard!

As a Data Analyst, visualizing data is only half the job—the real value lies in converting raw metrics into actionable business strategy.

Using Python, Pandas, and Streamlit, I built an interactive executive dashboard analyzing over 1,000 transaction records to evaluate revenue patterns, foot traffic, and customer behavior.

💡 Key Business Insights Discovered:
1️⃣ Operational Peak Traffic: Customer transactions hit peak volume at 19:00 (113 transactions) and 13:00 (103 transactions), highlighting exact time windows for optimized cashier staffing.
2️⃣ Volume vs Revenue Discrepancy: Food & Beverages drove the highest total revenue ($56.1K), while Electronic Accessories led in physical volume sold (971 units).
3️⃣ Loyalty Value: Members contributed ~58.7% of total revenue ($189.6K), proving the high ROI of customer retention programs.
4️⃣ Day-of-Week Variation: Saturday generates peak weekly sales ($56.1K), whereas Monday experiences a ~32% dip in overall traffic.

🛠️ Tech Stack: Python | Pandas | Streamlit | Streamlit Cloud | Git & GitHub

🔗 Live Dashboard Demo: [PASTE LINK STREAMLIT CLOUD KAMU DI SINI]
📁 GitHub Repository: [PASTE LINK GITHUB KAMU DI SINI]

I’d love to hear your thoughts and feedback! How does your team handle staffing adjustments based on peak hour transaction trends?

#DataAnalytics #Python #Streamlit #BusinessIntelligence #DataScience #Dashboard #Portfolio #Analytics
