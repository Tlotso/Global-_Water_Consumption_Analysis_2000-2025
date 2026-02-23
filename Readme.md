# Global Water Consumption Analysis (2000-2025)

## Project Overview
This project analyzes global water consumption patterns across multiple countries from 2000 to 2025. The dataset includes various metrics related to water usage, scarcity, and environmental factors.

## Dataset Description
The dataset contains the following columns:
- **Country**: Name of the country
- **Year**: Year of observation (2000-2025)
- **Total Water Consumption (Billion m3)**: Total water consumed
- **Per Capita Water Use (L/Day)**: Daily water usage per person
- **Agricultural Water Use (%)**: Percentage used for agriculture
- **Industrial Water Use (%)**: Percentage used for industry
- **Household Water Use (%)**: Percentage used for households
- **Rainfall Impact (mm)**: Rainfall measurement
- **Groundwater Depletion Rate (%)**: Rate of groundwater depletion
- **Water Scarcity Level**: Categorical variable (Low/Moderate/High/Critical)

## Key Findings
1. Global water consumption has steadily increased from 2000-2025
2. Agriculture remains the largest water consumer globally
3. Groundwater depletion rates have accelerated in water-scarce regions
4. Significant disparity in per capita water use between developed and developing nations
Key Insights from the Risk Analysis:
6. By 2030, Middle Eastern and North African countries like Egypt, Iran, Jordan, and Saudi Arabia face critical water crises due to         dangerously high groundwater depletion combined with minimal rainfall. Approximately 15-20 nations require immediate international       intervention as compounding risk factors accelerate deterioration faster than previously projected.


## Visualizations
The analysis includes:
- Time series trends of water consumption
- Comparative analysis between countries
- Groundwater depletion patterns
- Rainfall impact analysis
- Water scarcity distribution
- Interactive plots using Plotly
- heatmap on your growth_rates
- Global Water Consumption Growth Rate Map
- Risk Score Distribution
- Risk Categories Pie Chart
- Top 15 Highest Risk Countries
- comprehensive dashboard

## Technologies Used
- Python 3.x
- Pandas for data manipulation
- Matplotlib/Seaborn for static visualizations
- Plotly for interactive visualizations
- Jupyter Notebook

## How to Run
1. Clone this repository
2. Install required packages: `pip install pandas numpy matplotlib seaborn plotly jupyter`
3. Open the Jupyter Notebook: `jupyter notebook water_consumption_analysis.ipynb`
4. Run all cells

## Files in Repository
- `water_consumption_analysis.ipynb`: Main Jupyter Notebook
- `global_water_consumption_2000_2025.csv`: Dataset
- `top_consumers_by_year.csv`: Generated analysis output
- `country_summary_stats.csv`: Generated analysis output
- `README.md`: This file

## Author
Tlotso T Pheto

## License
This project is open source and available under the MIT License.