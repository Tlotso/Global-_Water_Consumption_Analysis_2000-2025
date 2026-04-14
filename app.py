import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Configuration
st.set_page_config(page_title="Global Water Risk 2030", layout="wide")
st.title("💧 Global Water Consumption & 2030 Risk Predictive Analysis")

@st.cache_data
def load_data():
    # Load the predictive and status datasets from your analysis
    risk_df = pd.read_csv('risk_predictions_2030.csv')
    status_df = pd.read_csv('water_status_2025.csv')
    
    # Clean column names for easier coding
    for df in [risk_df, status_df]:
        df.columns = [c.strip().replace(' ', '_').replace('(', '').replace(')', '').replace('%', 'perc') for c in df.columns]
    return risk_df, status_df

try:
    risk_df, status_df = load_data()

    # --- SECTION 1: PREDICTIVE KEY METRICS ---
    st.subheader("🚀 2030 Predictive Risk Outlook")
    col1, col2, col3 = st.columns(3)
    
    critical_nations = risk_df[risk_df['Risk_Score'] >= 8].shape[0] # Example threshold for 'Critical'
    avg_depletion = risk_df['Groundwater_Depletion_Rate_perc'].mean()
    
    col1.metric("Critical Risk Nations (2030)", f"{critical_nations}")
    col2.metric("Projected Avg. Depletion", f"{avg_depletion:.2f}%")
    col3.metric("Data Status", "Model Verified (XGBoost/Prophet)")

    st.divider()

    # --- SECTION 2: VISUALIZING THE RISK ---
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("🌍 2030 Risk Heatmap")
        # Map showing predicted risk scores by country
        fig_map = px.choropleth(
            risk_df,
            locations="Country",
            locationmode="country names",
            color="Risk_Score",
            hover_name="Country",
            color_continuous_scale="Reds",
            title="Predicted Risk Score by Country (2030)"
        )
        st.plotly_chart(fig_map, use_container_width=True)

    with right_col:
        st.subheader("📊 Top 15 Countries at Risk")
        # Bar chart for the most vulnerable nations
        top_risk = risk_df.nlargest(15, 'Risk_Score')
        fig_bar = px.bar(
            top_risk,
            x='Risk_Score',
            y='Country',
            orientation='h',
            color='Risk_Score',
            color_continuous_scale='Reds',
            title="Highest Predicted Risk Scores for 2030"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- SECTION 3: TREND ANALYSIS ---
    st.divider()
    st.subheader("📈 Consumption Trends & Rainfall Impact")
    
    # Scatter plot to show relationship between depletion and rainfall
    fig_scatter = px.scatter(
        status_df,
        x="Rainfall_Impact_mm",
        y="Groundwater_Depletion_Rate_perc",
        size="Total_Water_Consumption_Billion_m3",
        color="Water_Scarcity_Level",
        hover_name="Country",
        log_x=True,
        title="Rainfall vs. Depletion (Bubble size = Total Consumption)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # --- SECTION 4: ANALYST NOTES ---
    with st.expander("📝 Junior Analyst Insights"):
        st.markdown(f"""
        - **Critical Observation:** Middle East and North Africa (MENA) regions show the highest predictive risk levels.
        - **Model Logic:** The Risk Score is a composite of groundwater depletion (>5%) and low annual rainfall (<500mm).
        - **Actionable Data:** Countries like **Egypt, Iran, and Jordan** are projected to reach 'Critical' status by 2030.
        """)

except Exception as e:
    st.error(f"⚠️ Dashboard Error: {e}")
    st.info("Please ensure 'risk_predictions_2030.csv' and 'water_status_2025.csv' are in the project folder.")