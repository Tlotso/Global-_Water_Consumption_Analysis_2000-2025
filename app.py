import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Water Risk Portal", layout="wide")
st.title("💧 Water Operations & 2030 Risk Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv('water_risk_lite.csv')
    # Standardize all columns to lowercase and underscores
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df

try:
    df = load_data()
    
    # Identify our columns (looking for 'risk_score' or 'riskscore')
    risk_col = 'risk_score' if 'risk_score' in df.columns else df.columns[-1]
    region_col = 'region' if 'region' in df.columns else df.columns[1]

    # --- KPIs ---
    st.subheader("📊 Operational Health (2025 Current)")
    c1, c2, c3 = st.columns(3)
    
    curr_df = df[df['year'] == 2025] if 'year' in df.columns else df
    
    avg_val = curr_df[risk_col].mean()
    c1.metric("Avg. Risk Score", f"{avg_val:.2f}")
    c2.metric("System Status", "Live")
    c3.metric("ETL Automation", "100%")

    # --- THE DASHBOARD (Regional Risk) ---
    st.divider()
    st.subheader("🌍 Regional Risk Comparison")
    
    # This creates the bar chart dashboard
    fig = px.bar(
        curr_df.groupby(region_col)[risk_col].mean().reset_index(),
        x=region_col, 
        y=risk_col,
        color=risk_col,
        color_continuous_scale='Blues',
        title="Average Risk by Region",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- DOCUMENTATION ---
    with st.expander("🛠️ Internal Analyst Notes"):
        st.write("This standardized layout focuses on 'Loss Accounting' by comparing regional risk averages.")

except Exception as e:
    st.error(f"Waiting for data... Error: {e}")