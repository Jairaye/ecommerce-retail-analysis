# E-Commerce Retail Analytics Project

**Comprehensive retail analytics demonstrating marketing efficiency measurement, customer segmentation, and performance optimization**

---

## Project Overview

This project analyzes retail e-commerce data to identify revenue optimization opportunities, measure marketing return on investment (ROAS), and provide actionable insights for strategic decision-making. The analysis focuses on category performance, regional trends, customer behavior, and marketing efficiency—key metrics for commerce analytics teams.

**Key Analysis Areas:**
- Marketing efficiency & ROAS measurement by category
- Regional performance gap analysis
- Customer lifetime value & retention metrics
- Device usage & conversion optimization
- Revenue forecasting & trend analysis

---

## Business Context

This analysis simulates the work of a **Commerce Insights & Analytics** role, where the goal is to:
- Track media effectiveness and ROAS across product categories
- Identify correlations between marketing investment and sales performance
- Support campaign measurement and test-and-learn programs
- Translate data into clear, actionable recommendations
- Optimize marketing spend allocation for maximum ROI

---

## Key Findings

### Marketing Efficiency Insights

**Overall Performance:**
- Total Revenue: $1.44M
- Total Marketing Spend: $273.7K
- **Overall ROAS: 5.28x** (28% above break-even)

**Category Performance:**
- **Beauty**: 30.5x ROAS (lowest marketing spend, highest efficiency)
- **Electronics**: 4.1x ROAS (48% of revenue, highest marketing investment)
- **Sports**: 4.1x ROAS (high competition category)

**Recommendation:** Reallocate 15-20% of Electronics marketing budget to Beauty and Fashion categories to improve overall portfolio ROAS.

---

### Regional Performance Gaps

**Top Performers:**
- New York: +24% above average revenue per customer
- Chicago: +19% above average
- Houston: +12% above average

**Underperformers:**
- **Dallas: -40% below average** (Critical issue)
- Philadelphia: -29% below average
- Los Angeles: -2% below average

**Root Cause Hypotheses:**
1. Logistics/delivery challenges
2. Lower brand awareness
3. Competitive pressure from local retailers
4. Pricing misalignment with regional demographics

**Recommendation:** Conduct deep-dive analysis on Dallas market including delivery times, customer satisfaction scores, and competitive benchmarking.

---

### Customer Behavior Insights

**Customer Retention Value:**
- Returning customers spend **83% more** per transaction ($89.51 vs $48.91)
- Returning customers represent **88% of transactions**
- Customer retention is a key revenue driver

**Device Performance:**
- Mobile: 56% of transactions, $79.23 avg transaction
- Desktop: 34% of transactions, **$95.34 avg transaction (+20%)**
- Tablet: 10% of transactions, $78.93 avg transaction

**Recommendation:** 
1. Implement retention program targeting first-time buyers
2. Optimize mobile checkout experience to increase AOV
3. Test desktop-specific promotions for higher-value items

---

## Technical Skills Demonstrated

### **Languages & Tools:**
- **Python**: pandas, NumPy, matplotlib, seaborn
- **Jupyter Notebook**: Exploratory data analysis & visualization
- **Data Manipulation**: ETL, data cleaning, feature engineering
- **Statistical Analysis**: Correlation analysis, trend identification

### **Analytics Capabilities:**
- Marketing measurement (ROAS, CAC, LTV)
- Customer segmentation & cohort analysis
- Time series analysis & forecasting
- A/B test design and measurement
- Business intelligence reporting

### **Visualization:**
- Multi-panel dashboards
- Executive summary reports
- Interactive charts with actionable insights
- Professional presentation-ready graphics

---

## Project Structure

```
ecommerce-retail-analytics/
├── data/
│   ├── raw/                      # Original dataset
│   └── processed/                # Cleaned and transformed data
├── notebooks/
│   ├── 01_data_exploration.ipynb # Initial analysis & insights
│   ├── 02_predictive_modeling.ipynb  # Customer segmentation & forecasting
│   └── 03_ab_test_analysis.ipynb     # Marketing campaign testing
├── visualizations/
│   ├── category_performance.png
│   ├── regional_performance.png
│   ├── marketing_efficiency.png
│   ├── customer_segmentation.png
│   ├── time_series_analysis.png
│   └── executive_summary.png
├── src/
│   └── utils.py                  # Helper functions
└── README.md
```

---

## How to Run This Project

### Prerequisites
```bash
Python 3.8+
pandas
numpy
matplotlib
seaborn
jupyter
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/ecommerce-retail-analytics.git

# Navigate to project directory
cd ecommerce-retail-analytics

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

### Run Analysis
Open `notebooks/01_data_exploration.ipynb` and run all cells to reproduce the analysis.

---

## Sample Visualizations

### Marketing Efficiency Dashboard
![Marketing Efficiency](visualizations/marketing_efficiency.png)

*Analysis of ROAS by category, showing Beauty and Fashion as high-efficiency opportunities*

### Regional Performance
![Regional Performance](visualizations/regional_performance.png)

*Revenue comparison across major cities, highlighting Dallas underperformance*

### Customer Segmentation
![Customer Segmentation](visualizations/customer_segmentation.png)

*Breakdown of customer types and device usage patterns*

---

## Business Impact & Recommendations

### Immediate Actions (0-30 days):
1. **Reallocate Marketing Budget**: Shift $40K from Electronics to Beauty/Fashion
   - Expected impact: +$200K revenue, +15% portfolio ROAS
2. **Dallas Market Investigation**: Deploy survey + logistics audit
   - Goal: Identify root cause of 40% underperformance
3. **Mobile Optimization Sprint**: A/B test simplified checkout flow
   - Target: Increase mobile AOV by 10% ($79 → $87)

### Strategic Initiatives (30-90 days):
1. **Retention Program Launch**: Email campaign targeting first-time buyers
   - Target: Convert 20% to returning customers (+$450K annual revenue)
2. **Desktop Experience Enhancement**: Premium product recommendations
   - Leverage 20% higher AOV on desktop traffic
3. **Regional Marketing Customization**: Localized campaigns for underperforming cities

---

## Key Learnings

1. **ROAS varies dramatically by category** - Not all revenue is created equal when accounting for acquisition cost
2. **Geographic performance gaps can be massive** - Dallas underperforms by 40%, indicating systemic issues beyond normal variance
3. **Customer retention drives profitability** - Returning customers are 83% more valuable, justifying significant retention investment
4. **Device optimization matters** - Desktop users spend 20% more; mobile UX improvements could unlock significant revenue

---

## About Me

**Joshua Adams**  
Business Intelligence Analyst | Python | SQL | Tableau

I specialize in translating complex data into actionable business insights. My background spans procurement analytics, pricing optimization, and marketing measurement, but I've also done supply chain optimization, sports insights, and statistical inquiries to prove or disprove memes. I'm passionate about using data to drive strategic decision-making and improve ROI.

Contact: [ada.jos@outlook.com](mailto:ada.jos@outlook.com)  
LinkedIn: [LinkedIn](https://www.linkedin.com/in/jradams11/)  
GitHub: [GitHub](https://github.com/jairaye)

---

## License

This project is for portfolio demonstration purposes.

---

## Acknowledgments

- Dataset: Transformed from Turkish e-commerce data to US retail context
- Tools: Python data science ecosystem (pandas, matplotlib, seaborn)
- Inspiration: Real-world commerce analytics use cases

---

**If you found this analysis valuable, please star this repository!**