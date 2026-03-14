# 💧 Global Water Consumption & 2030 Risk Portal

### 🔗 **[View Live Interactive Dashboard](https://your-streamlit-link-here.streamlit.app)** ---

## 📋 Project Overview
This project analyzes global water patterns from 2000–2025 to identify production inefficiencies and predict scarcity risks for 2030. I have transitioned this analysis from a static Jupyter Notebook into an **automated operational dashboard** to help client teams monitor KPIs in real-time.

### 🚀 Efficiency & Operational Improvements
As a junior analyst, I identified and implemented the following optimizations:
* **Automated ETL:** Data connections are cached and automated via Python, eliminating manual monthly CSV processing.
* **Standardized Layouts:** Developed a consistent "Power BI style" design across Streamlit to ensure the team can find Production and Loss metrics instantly.
* **Operational Dashboards:** Delivered specific views for **Production** (Usage), **Loss Accounting** (Depletion), and **Risk KPIs**.
* **Client Training:** Built-in documentation to help non-technical users navigate the 2030 projections.

---

## 🧪 Key Insights from the Risk Analysis
* **Growth Trends:** Global water consumption has shown a steady increase over 25 years, with Agriculture remaining the primary driver.
* **Groundwater Crisis:** Depletion rates have accelerated significantly in water-scarce regions.
* **2030 Projections:** Middle Eastern and North African nations (e.g., Egypt, Iran, Jordan, Saudi Arabia) face critical crises due to low rainfall and high depletion. 
* **Urgent Intervention:** Approximately 15–20 nations are identified as "High Risk," requiring immediate infrastructure intervention.

---

## 📊 Dataset Description
The dataset tracks metrics across 100+ countries, including:
- **Total Water Consumption**: In Billion m3.
- **Per Capita Water Use**: Daily usage per person.
- **Sector Use**: Agricultural, Industrial, and Household percentages.
- **Environmental Factors**: Rainfall Impact and Groundwater Depletion Rate.
- **Risk Score**: A composite metric developed to predict 2030 vulnerability.

---

## 🛠️ Tech Stack
* **Analysis:** Jupyter Notebook (Python)
* **Data Science:** Pandas, NumPy, Scikit-Learn
* **Visualization:** Plotly, Matplotlib, Seaborn
* **App Framework:** Streamlit (For the live dashboard)
* **Version Control:** GitHub

---

## 📂 Repository Structure
* `app.py`: The live Streamlit application code.
* `water_consumption_analysis.ipynb`: The core analytical engine and model development.
* `water_risk_lite.csv`: Optimized, automated dataset for high-speed dashboard loading.
* `global_water_consumption_2000_2025.csv`: Raw historical dataset.

---

## 📖 How to Run Locally
1. Clone this repository.
2. Install dependencies:  
   `pip install pandas numpy matplotlib seaborn plotly streamlit`
3. Launch the dashboard:  
   `streamlit run app.py`

---

## 👷 Author & Analyst
**Tlotso T Pheto** *Junior Data Analyst* *Focused on turning complex environmental data into actionable business tools.*