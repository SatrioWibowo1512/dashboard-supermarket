import streamlit as st
import pandas as pd
import os

st.title("Dashboard Penjualan Supermarket 🛒")

lokasi_file = '/SuperMarket Analysis.csv'
if not os.path.exists(lokasi_file):
    lokasi_file = '/content/SuperMarket Analysis.csv'
if not os.path.exists(lokasi_file):
    lokasi_file = 'SuperMarket Analysis.csv'

try:
    df = pd.read_csv(lokasi_file)
    
    with st.expander("Klik untuk lihat sampel data mentah"):
        st.table(df.head())

    # Baris ini yang mengubah Branch menjadi kolom utuh agar bisa diwarnai
    penjualan_cabang = df.groupby('Branch')['Sales'].sum().reset_index()
    
    st.subheader("Total Pendapatan per Cabang")
    st.bar_chart(penjualan_cabang, x='Branch', y='Sales', color='Branch')
    
except FileNotFoundError:
    st.error("File CSV tidak terbaca.")
