import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Water Risk Command Center", layout="wide")

st.title("💧 Water Operations & 2030 Risk Dashboard")
st.markdown("*Opportunities Identified: Automated ETL, Standardized Reporting, and Predictive Loss Accounting.*")

# 2. Robust Data Loading
@st.cache_data
def load_data():
    df = pd.read_csv('water_risk_lite.csv')
    # Standardize column names to prevent KeyErrors
    df.columns = [c.strip().replace(' ', '_') for c in df.columns]
    return df

try:
    df = load_data()
    
    # --- SECTION 1: OPERATIONAL KPIs ---
    # Ensure this subheader is indented exactly 4 spaces from the 'try'
    st.subheader("📊 Operational Health (2025 Current)")
    
    kpi1, kpi2, kpi3 = st.columns(3)
    curr_df = df[df['Year'] == 2025]
    
    # We use .get() or a check to ensure the metric doesn't crash if column is missing
    avg_risk = curr_df['Risk_Score'].mean() if 'Risk_Score' in curr_df.columns else 0
    
    kpi1.metric("Avg. Risk Score", f"{avg_risk:.2f}")
    kpi2.metric("System Status", "Live")
    kpi3.metric("ETL Automation", "100%")

    st.divider()

    # --- SECTION 2: REGIONAL ANALYSIS ---
    st.write("### 🌍 Regional Risk Comparison")
    if 'Region' in df.columns and 'Risk_Score' in df.columns:
        fig_bar = px.bar(curr_df.groupby('Region')['Risk_Score'].mean().reset_index(), 
                         x='Region', y='Risk_Score', color='Risk_Score',
                         color_continuous_scale='Reds', template="simple_white")
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- SECTION 3: TRAINING ---
    with st.expander("🛠️ Internal Analyst Notes"):
        st.write("This layout is standardized across all operational dashboards to ensure consistent KPI tracking.")

except Exception as e:
    st.error(f"Configuration Error: {e}")
    st.info("Junior Analyst Tip: Check if 'water_risk_lite.csv' is uploaded to GitHub correctly.")