# Executive Supermarket Sales & Customer Analytics Dashboard

An interactive, multi-dimensional Business Intelligence dashboard built with Python and Streamlit to analyze supermarket transaction data, customer behavior, hourly peak traffic, and product profitability.

🔗 **Live Interactive Dashboard:** [https://dashboard-supermarket-7xrwudjfgvvkmghtzgawwr.streamlit.app/]

---

## 1. Business Overview & Objective
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

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SatrioWibowo1512/dashboard-supermarket.git](https://github.com/SatrioWibowo1512/dashboard-supermarket.git)
   cd dashboard-supermarket
   ```
2. **Install dependencies:**
   ```bash
   pip install pandas streamlit
   ```
3. **Run the Streamlit app::**
   ```bash
   streamlit run app.py
   ```
---

## 2. Dashboard Preview

### 1. Key Performance Indicators & Product Sales
![KPI Overview](/documentations/ss_kpi_overview.png)

### 2. Time Series & Operating Hours Analysis
![Time Trend Analysis](/documentations/ss_time_trend.png)

### 3. Customer Demographics & Payment Behavior
![Customer Demographics](/documentations/ss_demographics.png)

### 4. Dynamic Metric Switcher (Sales vs Units vs Transactions)
![Metric Toggle](/documentations/ss_metric_toggle.png)

---

## 3. Executive Summary & Business Insights (Analyst Report)

The following data-driven analytical summary can be presented during job interviews or delivered directly to business stakeholders:

* **Peak Hour Management (*Staffing & Operational Efficiency*):**
  * **Finding:** Transaction spikes occur at two distinct time windows: lunch hour (**13:00**) with 103 transactions and the evening peak (**19:00**) with 113 transactions. Queue traffic drops significantly after 20:00.
  * **Recommendation:** Allocate maximum cashier staffing between **12:30–14:00** and **18:30–20:00**. Adding extra cashiers outside these peak windows is operationally inefficient.

* **Product Strategy (*Revenue vs. Volume Matrix*):**
  * **Finding:** The *Food & Beverages* category leads in total revenue (**$56,144.84**) and gross profit (**$2,673.56**), whereas *Electronic Accessories* moves the highest physical volume (**971 units**). The *Health & Beauty* category ranks lowest in total sales ($49,193.74).
  * **Recommendation:** Position *Health & Beauty* items near the checkout or high-traffic zones to trigger impulse purchases. Implement cross-selling strategies by bundling high-turnover electronics with lifestyle accessories.

* **Sales Day Optimization (*Weekly Promotion*):**
  * **Finding:** **Saturday** records the highest sales revenue (**$56,120.81**), whereas **Monday** experiences a sharp decline (**$37,899.08**).
  * **Recommendation:** Launch targeted Monday promotional campaigns (e.g., *"Monday Madness"* or e-wallet cashback offers) to stimulate foot traffic during slow weekdays.

* **Customer Lifetime Value (*Member Loyalty Value*):**
  * **Finding:** Loyalty membership cardholders (*Members*) generate **$189,694.76** (58.7% of total revenue) compared to non-member shoppers (*Normal*) at **$133,271.99**.
  * **Recommendation:** Strengthen membership signup incentives at checkout, as member retention yields significantly higher revenue stability.

---
