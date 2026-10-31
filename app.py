import streamlit as st
import pandas as pd
import os

st.title("Dashboard Penjualan Supermarket 🛒")
df = pd.read_csv('SuperMarket Analysis.csv')

# Filter
st.sidebar.header("Filter Data")
pilih_kota = st.sidebar.multiselect("Pilih Kota:", df['City'].unique(), default=df['City'].unique())
df_filter = df[df['City'].isin(pilih_kota)]

# Menampilkan KPI (Angka Penting)
col1, col2 = st.columns(2)
col1.metric("Total Pendapatan", f"${df_filter['Sales'].sum():,.2f}")
col2.metric("Total Transaksi", len(df_filter))

# Grafik
penjualan_cabang = df_filter.groupby('Branch')['Sales'].sum().reset_index()
st.subheader("Pendapatan per Cabang")
st.bar_chart(penjualan_cabang, x='Branch', y='Sales', color='Branch')
