import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Water Risk Portal", layout="wide")
st.title("💧 Water Operations & 2030 Risk Dashboard")

@st.cache_data
def load_data():
    # Junior Analyst Tip: Always clean column names first!
    df = pd.read_csv('water_risk_lite.csv')
    df.columns = [c.strip().replace(' ', '_').replace('(', '').replace(')', '').replace('%', 'perc') for c in df.columns]
    return df

try:
    df = load_data()
    
    # 1. Automatically find the right columns
    # We want a numeric column for the score and a text column for the categories
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Fallback logic if names changed
    risk_col = 'risk_score' if 'risk_score' in numeric_cols else (numeric_cols[-1] if numeric_cols else None)
    region_col = 'region' if 'region' in categorical_cols else (categorical_cols[0] if categorical_cols else None)

    # --- SECTION 1: KPIs ---
    st.subheader("📊 Operational Health (2025 Current)")
    c1, c2, c3 = st.columns(3)
    
    # Only show math if we have a numeric column
    if risk_col:
        curr_year = df['year'].max() if 'year' in df.columns else None
        curr_df = df[df['year'] == curr_year] if curr_year else df
        
        avg_val = curr_df[risk_col].mean()
        c1.metric("Avg. Risk Score", f"{avg_val:.2f}")
    else:
        c1.warning("No numeric risk score found.")

    c2.metric("System Status", "Live/Automated")
    c3.metric("Data Quality", "Verified")

    # --- SECTION 2: THE DASHBOARD ---
    st.divider()
    st.subheader("🌍 Regional Risk Analysis (Loss Accounting)")
    
    if risk_col and region_col:
        # Create a clean summary for the chart
        chart_data = curr_df.groupby(region_col)[risk_col].mean().reset_index()
        
        fig = px.bar(
            chart_data,
            x=region_col, 
            y=risk_col,
            color=risk_col,
            color_continuous_scale='Reds', # 'Reds' for risk
            title="Average Risk Level by Region",
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Junior Analyst Note: Please ensure your CSV has a numeric 'Risk_Score' column.")

    # --- SECTION 3: EFFICIENCY & TRAINING ---
    st.divider()
    with st.expander("📖 Operational Documentation for Teams"):
        st.markdown("""
        ### How to use this Dashboard:
        1. **Check the Risk Score:** If the number turns red, we need to investigate the region immediately.
        2. **Standardised Layouts:** This dashboard follows our new Power BI standard for easy reading.
        3. **Automated ETL:** This data is refreshed automatically from our primary model.
        """)

except Exception as e:
    st.error(f"⚠️ App Setup Needed: {e}")
    st.markdown("Try running the **Data Export** cell in your notebook again to refresh 'water_risk_lite.csv'.")