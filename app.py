import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermarket Dashboard", layout="wide")
st.title("Executive Supermarket Sales and Customer Analytics")
st.markdown("Comprehensive analysis of sales performance, customer demographics, financials, and ratings.")

# LOAD DATA AND PREPROCESSING
@st.cache_data
def load_data():
    df = pd.read_csv('SuperMarket Analysis.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    # Hour and Date Extract
    df['Hour'] = df['Time'].str.split(':').str[0].astype(int)
    df['Day_Name'] = df['Date'].dt.day_name()
    return df

df = load_data()

# SIDEBAR FILTER
st.sidebar.header("Global Filters")

city_filter = st.sidebar.multiselect(
    "Select City:", 
    options=df['City'].unique(), 
    default=df['City'].unique()
)

customer_filter = st.sidebar.multiselect(
    "Select Customer Type:", 
    options=df['Customer type'].unique(), 
    default=df['Customer type'].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender:", 
    options=df['Gender'].unique(), 
    default=df['Gender'].unique()
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Method:", 
    options=df['Payment'].unique(), 
    default=df['Payment'].unique()
)

# APPLY ALL FILTERS TO DATAFRAME
df_filtered = df[
    (df['City'].isin(city_filter)) &
    (df['Customer type'].isin(customer_filter)) &
    (df['Gender'].isin(gender_filter)) &
    (df['Payment'].isin(payment_filter))
]

# EXECUTIVE KEY PERFORMANCE INDICATOR METRICS (COMBINE)
st.subheader("Key Performance Indicators (KPI)")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Revenue", f"${df_filtered['Sales'].sum():,.2f}")
col2.metric("Total COGS", f"${df_filtered['cogs'].sum():,.2f}")
col3.metric("Gross Income (Profit)", f"${df_filtered['gross income'].sum():,.2f}")
col4.metric("Total Transactions", f"{len(df_filtered):,}")
col5.metric("Avg Rating", f"{df_filtered['Rating'].mean():.2f} / 10")

st.markdown("---")

# NAVIGATION TAB NAVIGATION FOR MULTI-GRAPHICS
tab1, tab2, tab3 = st.tabs([
    "Sales & Product Breakdown", 
    "Demographics & Customer Behavior", 
    "Financials & Rating Analysis"
])

# TAB 1: SALES, CITY, CATEGORY, & TIME
with tab1:
    st.subheader("Overview & Product Performance")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("Sales Revenue by City")
        city_sales = df_filtered.groupby('City')['Sales'].sum().reset_index()
        st.bar_chart(city_sales, x='City', y='Sales', color='City')

    with col_b:
        st.markdown("**Sales Revenue by Product Category**")
        product_sales = df_filtered.groupby('Product line')['Sales'].sum().reset_index()
        st.bar_chart(product_sales, x='Product line', y='Sales', color='Product line')

    st.markdown("---")
    st.subheader("Time Trend Analysis")
    col_c, col_d = st.columns(2)
    
    with col_c:
        st.markdown("Hourly Sales Trend (Peak Hours)")
        hourly_sales = df_filtered.groupby('Hour')['Sales'].sum().reset_index()
        st.line_chart(hourly_sales, x='Hour', y='Sales')

    with col_d:
        st.markdown("**Daily Sales Trend**")
        daily_sales = df_filtered.groupby('Date')['Sales'].sum().reset_index()
        st.line_chart(daily_sales, x='Date', y='Sales')

# TAB 2: DEMOGRAPHICS, CUSTOMER TYPE, & PAYMENTS
with tab2:
    st.subheader("Customer Demographics & Payment Preferences")
    col_e, col_f, col_g = st.columns(3)
    
    with col_e:
        st.markdown("Sales by Gender")
        gender_sales = df_filtered.groupby('Gender')['Sales'].sum().reset_index()
        st.bar_chart(gender_sales, x='Gender', y='Sales', color='Gender')
        
    with col_f:
        st.markdown("Sales by Customer Type (Member vs Normal)")
        role_sales = df_filtered.groupby('Customer type')['Sales'].sum().reset_index()
        st.bar_chart(role_sales, x='Customer type', y='Sales', color='Customer type')

    with col_g:
        st.markdown("Sales by Payment Method")
        payment_sales = df_filtered.groupby('Payment')['Sales'].sum().reset_index()
        st.bar_chart(payment_sales, x='Payment', y='Sales', color='Payment')

    st.markdown("---")
    st.markdown("Product Category Choice by Customer Role")
    cross_role_prod = df_filtered.groupby(['Product line', 'Customer type'])['Sales'].sum().unstack().fillna(0)
    st.bar_chart(cross_role_prod)

# TAB 3: FINANCIALS & RATING
with tab3:
    st.subheader("Financial Performance & Customer Satisfaction")
    col_h, col_i = st.columns(2)
    
    with col_h:
        st.markdown("COGS vs Gross Income by Product Category")
        fin_product = df_filtered.groupby('Product line')[['cogs', 'gross income']].sum()
        st.bar_chart(fin_product)
        
    with col_i:
        st.markdown("Average Customer Rating by Product Category")
        rating_product = df_filtered.groupby('Product line')['Rating'].mean().reset_index()
        st.bar_chart(rating_product, x='Product line', y='Rating', color='Product line')

    st.markdown("---")
    col_j, col_k = st.columns(2)
    
    with col_j:
        st.markdown("Average Rating by City")
        rating_city = df_filtered.groupby('City')['Rating'].mean().reset_index()
        st.bar_chart(rating_city, x='City', y='Rating', color='City')
        
    with col_k:
        st.markdown("Gross Margin Percentage Overview")
        avg_margin = df_filtered['gross margin percentage'].mean()
        st.info(f"Average Gross Margin Percentage: `{avg_margin:.2f}%` (Fixed margin applied across all transaction lines).")
        
        # TABLE SUMMARY
        fin_summary = df_filtered.groupby('City')[['Sales', 'cogs', 'gross income']].sum().reset_index()
        st.dataframe(fin_summary, use_container_width=True)
