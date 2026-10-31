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

    # HOUR FORMATTING (Mengubah format AM/PM ke format 24 jam HH:00)
    df['Time_dt'] = pd.to_datetime(df['Time'], format='%I:%M:%S %p', errors='coerce')
    df['Hour'] = df['Time_dt'].dt.hour
    df['Hour_Label'] = df['Hour'].apply(lambda x: f"{x:02d}:00")
    
    # EXTRACT DAY NAME (Disusun berurutan Senin -> Minggu)
    df['Day_Name'] = df['Date'].dt.day_name()
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Day_Name'] = pd.Categorical(df['Day_Name'], categories=days_order, ordered=True)

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

st.sidebar.markdown("---")
st.sidebar.header("Chart Metric View")
metric_choice = st.sidebar.radio("Display Charts By:", ["Sales ($)", "Quantity (Units)"])
metric_col = "Sales" if metric_choice == "Sales ($)" else "Quantity"

# APPLY ALL FILTERS TO DATAFRAME
df_filtered = df[
    (df['City'].isin(city_filter)) &
    (df['Customer type'].isin(customer_filter)) &
    (df['Gender'].isin(gender_filter)) &
    (df['Payment'].isin(payment_filter))
]

# HELPER FUNCTIONS FOR CONSISTENT CODE AGGREGATION
def get_aggregated_data(df, group_by_col):
    if metric_choice == "Sales ($)":
        res = df.groupby(group_by_col, observed=False)['Sales'].sum().reset_index()
        res.columns = [group_by_col, "Sales ($)"]
        return res, "Sales ($)"
    elif metric_choice == "Quantity (Units)":
        res = df.groupby(group_by_col, observed=False)['Quantity'].sum().reset_index()
        res.columns = [group_by_col, "Quantity (Units)"]
        return res, "Quantity (Units)"
    else:  # Transactions (Count)
        res = df.groupby(group_by_col, observed=False)['Invoice ID'].nunique().reset_index()
        res.columns = [group_by_col, "Transactions"]
        return res, "Transactions"

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
    st.subheader(f"Overview & Product Performance ({metric_choice})")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown(f"**{metric_choice} by City**")
        city_sales = df_filtered.groupby('City')[metric_col].sum().reset_index()
        st.bar_chart(city_sales, x='City', y=metric_col, color='City')

    with col_b:
        st.markdown(f"**{metric_choice} by Product Category**")
        product_sales = df_filtered.groupby('Product line')[metric_col].sum().reset_index()
        st.bar_chart(product_sales, x='Product line', y=metric_col, color='Product line')

    st.markdown("---")
    st.subheader(f"Time Trend Analysis ({metric_choice})")
    col_c, col_d, col_e = st.columns(3)
    
    with col_c:
        st.markdown("**Hourly Trend (Operating Hours 10:00 - 20:00)**")
        # Menggunakan Hour_Label (format HH:00) dan metric_col
        hourly_sales = df_filtered.groupby('Hour_Label')[metric_col].sum().reset_index()
        st.line_chart(hourly_sales, x='Hour_Label', y=metric_col)

    with col_d:
        st.markdown("**Day of Week Trend (Monday - Sunday)**")
        # Menambahkan grafik tren berdasarkan nama hari
        day_sales = df_filtered.groupby('Day_Name', observed=False)[metric_col].sum().reset_index()
        st.bar_chart(day_sales, x='Day_Name', y=metric_col, color='Day_Name')

    with col_e:
        st.markdown("**Daily Timeline Trend**")
        daily_sales = df_filtered.groupby('Date')[metric_col].sum().reset_index()
        st.line_chart(daily_sales, x='Date', y=metric_col)

# TAB 2: DEMOGRAPHICS, CUSTOMER TYPE, & PAYMENTS
with tab2:
    st.subheader(f"Customer Demographics & Payment Preferences ({metric_choice})")
    col_e_1, col_f_1, col_g_1 = st.columns(3)
    
    with col_e_1:
        st.markdown(f"**{metric_choice} by Gender**")
        gender_sales = df_filtered.groupby('Gender')[metric_col].sum().reset_index()
        st.bar_chart(gender_sales, x='Gender', y=metric_col, color='Gender')
        
    with col_f_1:
        st.markdown(f"**{metric_choice} by Customer Type (Member vs Normal)**")
        role_sales = df_filtered.groupby('Customer type')[metric_col].sum().reset_index()
        st.bar_chart(role_sales, x='Customer type', y=metric_col, color='Customer type')

    with col_g_1:
        st.markdown(f"**{metric_choice} by Payment Method**")
        payment_sales = df_filtered.groupby('Payment')[metric_col].sum().reset_index()
        st.bar_chart(payment_sales, x='Payment', y=metric_col, color='Payment')

    st.markdown("---")
    st.markdown(f"**Product Category Choice by Customer Role ({metric_choice})**")
    if metric_choice == "Sales ($)":
        cross_role = df_filtered.groupby(['Product line', 'Customer type'])['Sales'].sum().unstack().fillna(0)
    elif metric_choice == "Quantity (Units)":
        cross_role = df_filtered.groupby(['Product line', 'Customer type'])['Quantity'].sum().unstack().fillna(0)
    else:
        cross_role = df_filtered.groupby(['Product line', 'Customer type'])['Invoice ID'].nunique().unstack().fillna(0)
    st.bar_chart(cross_role)

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
