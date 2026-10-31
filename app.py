import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermarket Dashboard", layout="wide")
st.title("Sales Dashboard and Customer Behavior")

# LOAD AND DATA CLEANING
df = pd.read_csv('SuperMarket Analysis.csv')

# FORMATING DATE TO DATETIME
df['Date'] = pd.to_datetime(df['Date'])

# MAKE HOUR AND DAY COLUMN
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
df['Day'] = df['Date'].dt.day_name()


# SIDEBAR FILTER
st.sidebar.header("Analysis Filter")
city_choice = st.sidebar.multiselect("City:", df['City'].unique(), default=df['City'].unique())
gender_choice = st.sidebar.multiselect("Gender:", df['Gender'].unique(), default=df['Gender'].unique())

# APPLY FILTER TO DATAFRAME
df_filter = df[(df['City'].isin(city_choice)) & (df['Gender'].isin(gender_choice))]

# KEY PERFORMANCE INDICATOR (KPI)
col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"${df_filter['Sales'].sum():,.2f}")
col2.metric("Total Profit Clean", f"${df_filter['gross income'].sum():,.2f}")
col3.metric("Average Rating", f"{df_filter['Rating'].mean():.1f} / 10")

st.markdown("---")

# VISUAL ANALYSIS
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Revenue by Produck Category")
    product_sales = df_filter.groupby('Product line')['Sales'].sum().reset_index()
    st.bar_chart(product_sales, x='Product line', y='Sales', color='Product line')

with right_col:
    st.subheader("Peak Hour Trends")
    # Calculate the number of transactions for each hour
    hour_transactions = df_filter.groupby('Hour')['Invoice ID'].count().reset_index()
    st.line_chart(hour_transactions, x='Hour', y='Invoice ID')
