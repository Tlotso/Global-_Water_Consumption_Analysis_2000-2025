import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Configuration
st.set_page_config(page_title="Global Water Risk 2030", layout="wide")
st.title("💧 Global Water Consumption & 2030 Risk Predictive Analysis")

@st.cache_data
def load_data():
    risk_df = pd.read_csv('risk_predictions_2030.csv')
    status_df = pd.read_csv('water_status_2025.csv')
    
    # Clean column names
    for df in [risk_df, status_df]:
        df.columns = [
            c.strip()
             .replace(' ', '_')
             .replace('(', '')
             .replace(')', '')
             .replace('%', 'perc') 
            for c in df.columns
        ]
    return risk_df, status_df

try:
    risk_df, status_df = load_data()

    # --- SECTION 1: PREDICTIVE KEY METRICS ---
    st.subheader("🚀 2030 Predictive Risk Outlook")
    col1, col2, col3, col4 = st.columns(4)

    critical_nations = risk_df[risk_df['Risk_Score'] >= 70].shape[0]
    avg_depletion    = risk_df['Avg_Depletion_Rate'].mean()
    highest_risk     = risk_df.loc[risk_df['Risk_Score'].idxmax(), 'Country']
    total_countries  = risk_df.shape[0]

    col1.metric("🔴 Critical Risk Nations (2030)", f"{critical_nations}")
    col2.metric("📉 Avg. Groundwater Depletion", f"{avg_depletion:.2f}%")
    col3.metric("⚠️ Highest Risk Country", highest_risk)
    col4.metric("🌍 Countries Analysed", f"{total_countries}")

    st.divider()

    # --- SECTION 2: RISK MAP & BAR CHART ---
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("🌍 2030 Risk Heatmap")
        fig_map = px.choropleth(
            risk_df,
            locations="Country",
            locationmode="country names",
            color="Risk_Score",
            hover_name="Country",
            hover_data={"Risk_Category": True, "Avg_Depletion_Rate": True},
            color_continuous_scale="Reds",
            title="Predicted Risk Score by Country (2030)"
        )
        fig_map.update_layout(margin=dict(l=0, r=0, t=40, b=0))
        st.plotly_chart(fig_map, use_container_width=True)

    with right_col:
        st.subheader("📊 Top 15 Countries at Risk")
        top_risk = risk_df.nlargest(15, 'Risk_Score').sort_values('Risk_Score')
        fig_bar = px.bar(
            top_risk,
            x='Risk_Score',
            y='Country',
            orientation='h',
            color='Risk_Score',
            color_continuous_scale='Reds',
            hover_data={"Risk_Category": True, "Avg_Depletion_Rate": True},
            title="Highest Predicted Risk Scores for 2030"
        )
        fig_bar.update_layout(yaxis_title="", xaxis_title="Risk Score (0–100)")
        st.plotly_chart(fig_bar, use_container_width=True)

    st.divider()

    # --- SECTION 3: RISK CATEGORY BREAKDOWN ---
    st.subheader("🗂️ Risk Category Distribution")
    cat_col, scatter_col = st.columns(2)

    with cat_col:
        cat_counts = risk_df['Risk_Category'].value_counts().reset_index()
        cat_counts.columns = ['Risk_Category', 'Count']
        category_order = ['Critical', 'High', 'Medium', 'Low']
        color_map = {
            'Critical': '#d62728',
            'High':     '#ff7f0e',
            'Medium':   '#ffdd57',
            'Low':      '#2ca02c'
        }
        fig_pie = px.pie(
            cat_counts,
            names='Risk_Category',
            values='Count',
            color='Risk_Category',
            color_discrete_map=color_map,
            title="Countries by Risk Category (2030)",
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with scatter_col:
        st.subheader("📈 Depletion Rate vs Risk Score")
        fig_scatter2 = px.scatter(
            risk_df,
            x='Avg_Depletion_Rate',
            y='Risk_Score',
            color='Risk_Category',
            color_discrete_map=color_map,
            hover_name='Country',
            size='Risk_Score',
            title="Depletion Rate vs Predicted Risk Score"
        )
        fig_scatter2.update_layout(
            xaxis_title="Avg Groundwater Depletion Rate (%)",
            yaxis_title="Risk Score (0–100)"
        )
        st.plotly_chart(fig_scatter2, use_container_width=True)

    st.divider()

    # --- SECTION 4: CONSUMPTION TRENDS & RAINFALL IMPACT ---
    st.subheader("🌧️ Rainfall vs. Groundwater Depletion (2025 Status)")

    # Check which depletion column exists in status_df
    depletion_col = (
        'Groundwater_Depletion_Rate_perc'
        if 'Groundwater_Depletion_Rate_perc' in status_df.columns
        else 'Groundwater_Depletion_Rate_'
    )
    consumption_col = (
        'Total_Water_Consumption_Billion_m3'
        if 'Total_Water_Consumption_Billion_m3' in status_df.columns
        else [c for c in status_df.columns if 'Consumption' in c][0]
    )

    fig_scatter = px.scatter(
        status_df,
        x="Rainfall_Impact_mm",
        y=depletion_col,
        size=consumption_col,
        color="Water_Scarcity_Level",
        hover_name="Country",
        log_x=True,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="Rainfall vs. Depletion Rate (Bubble size = Total Consumption)"
    )
    fig_scatter.update_layout(
        xaxis_title="Rainfall Impact (mm, log scale)",
        yaxis_title="Groundwater Depletion Rate (%)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.divider()

    # --- SECTION 5: DATA EXPLORER ---
    st.subheader("🔍 Country Risk Explorer")
    search_col, filter_col = st.columns([2, 1])

    with filter_col:
        selected_category = st.selectbox(
            "Filter by Risk Category",
            options=["All"] + category_order
        )

    filtered_df = (
        risk_df if selected_category == "All"
        else risk_df[risk_df['Risk_Category'] == selected_category]
    )

    with search_col:
        search = st.text_input("Search for a country", "")
    if search:
        filtered_df = filtered_df[
            filtered_df['Country'].str.contains(search, case=False, na=False)
        ]

    display_cols = [
        'Country', 'Risk_Score', 'Risk_Category',
        'Avg_Depletion_Rate', 'Avg_Scarcity_Score',
        'Predicted_Consumption_2030', 'Dominant_Scarcity_Level'
    ]
    # Only show columns that exist
    display_cols = [c for c in display_cols if c in filtered_df.columns]

    st.dataframe(
        filtered_df[display_cols].sort_values('Risk_Score', ascending=False),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --- SECTION 6: ANALYST NOTES ---
    with st.expander("📝 Junior Analyst Insights"):
        st.markdown(f"""
        **Key Findings from the 2030 Predictive Model:**

        - 🔴 **{critical_nations} nations** are projected to reach Critical or High risk status by 2030.
        - 📍 **MENA Region** (Middle East & North Africa) shows the highest concentration of at-risk countries,
          driven by low rainfall (<500mm/year) and agricultural water demand above 75%.
        - 🌊 **Groundwater depletion** is the strongest predictor — countries exceeding **5% depletion rate**
          consistently score in the High or Critical risk bands.
        - 🏆 **Highest risk:** {highest_risk} leads the risk index based on combined scarcity and depletion trends.
        - ✅ **Model used:** Composite risk scoring using XGBoost-derived feature weights
          (depletion 40%, scarcity level 40%, consumption volume 20%).

        *Data covers {total_countries} countries, 2000–2025. Projections extrapolated to 2030.*
        """)

except Exception as e:
    st.error(f"⚠️ Dashboard Error: {e}")
    st.info("Please ensure 'risk_predictions_2030.csv' and 'water_status_2025.csv' are in the project folder.")
    st.code(str(e))