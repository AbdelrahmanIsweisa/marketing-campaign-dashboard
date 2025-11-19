# 📊 Marketing Campaign Performance Dashboard

> End-to-end data analysis identifying $229K budget waste and projecting 15% ROI improvement

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-9.3-orange?logo=mysql)
![Excel](https://img.shields.io/badge/Excel-Analysis-green?logo=microsoft-excel)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-blue?logo=tableau)

---

🎯 Project Overview

Analyzed **5,856 marketing campaigns** across **12 channels** over 16 months (July 2024 - October 2025) to optimize a $3.9M advertising budget and maximize return on ad spend (ROAS).

Key Business Impact
- 💰 Identified $229K in wasted spend on Display Ads (1.74x ROAS)
- 📈 Recommended reallocation** to Email Marketing (288x ROAS) and Referral (64x ROAS)
- 🎯 Projected 15% ROI improvement (+$15M revenue potential)
- ⚡ Budget-neutral strategy - reallocate existing budget, no additional spend needed

---

🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python 3.11** | Data generation, preprocessing, automation |
| **MySQL 9.3** | Database design, complex queries with CTEs |
| **Microsoft Excel** | Financial modeling, pivot tables, what-if scenarios |
| **Tableau Public** | Interactive data visualizations |
| **Git/GitHub** | Version control and documentation |

**Python Libraries:** pandas, numpy, sqlalchemy, plotly

---

📈 Key Findings

🏆 Top Performing Channels

| Channel | ROAS | CAC | Budget Action |
|---------|------|-----|---------------|
| **Email Marketing** | 288.57x | $0.47 | 🟢 Increase 100% (+$92K) |
| **Referral Program** | 64.39x | $2.32 | 🟢 Increase 100% (+$57K) |
| **Affiliate Marketing** | 11.13x | $11.31 | 🟢 Increase 50% (+$112K) |

📉 Underperforming Channels

| Channel | ROAS | Current Spend | Issue |
|---------|------|---------------|-------|
| **Display Ads** | 1.74x | $458,688 | 🔴 Cut 50% (-$229K) |
| **Twitter Ads** | 2.11x | $270,660 | ⚠️ Declining performance |
| **LinkedIn Ads** | 2.38x | $612,393 | Expensive CAC ($114.25) |

📊 Conversion Funnel Analysis
```
73.4M Impressions (100%)
    ↓ 6.0% CTR
4.4M Clicks
    ↓ 10.0% Conversion Rate
441K Conversions
```

**Insight:** Email Marketing achieves 10.85% conversion rate vs. Display Ads at only 3.33%

---

💡 Strategic Recommendations

Immediate Actions (Week 1)
1. 🔴 **Cut Display Ads budget by 50%** → Save $229K
2. 📊 **Pause campaigns with ROAS < 1.5x**
3. 🔍 **Audit creative assets** for underperforming channels

Scale Winners (Weeks 2-3)
1. 🟢 **Double Email Marketing budget** → Projected +$26M revenue
2. 🟢 **Double Referral Program investment** → Expand incentive structure
3. 🟢 **Increase Affiliate Marketing by 50%** → Onboard new partners

Long-Term Optimization
- **A/B test email subject lines** (current 24% open rate baseline)
- **Invest in SEO** to boost Organic Search (currently 98K free conversions)
- **Implement lead scoring** for LinkedIn campaigns (high B2B conversion)
- **Set ROAS minimum threshold** of 2.0x for all paid channels

---

🗂️ Project Structure
```
marketing-campaign-dashboard/
├── data/
│   ├── marketing_campaigns.csv          # 5,856 rows, 14 columns
│   └── Marketing_analysis.db            # MySQL database
├── dashboards/
│   └── (Tableau workbook)
├── generate_marketing_data.py           # Data generation script
├── sql_analysis.py                      # SQL query automation
├── create_dashboard.py                  # Plotly visualizations
├── Marketing_Campaign_Analysis.xlsx     # Excel financial model
└── README.md                            # Project documentation
```

---

🚀 How to Run This Project

Prerequisites
```bash
# Python 3.8+
python --version

# Install dependencies
pip install pandas numpy sqlalchemy plotly
```

 Steps
```bash
# 1. Generate marketing data
python generate_marketing_data.py

# 2. Run SQL analysis
python sql_analysis.py

# 3. Create visualizations
python create_dashboard.py

# 4. Open Excel for financial modeling
open Marketing_Campaign_Analysis.xlsx
```

---

## 📊 Sample SQL Query

### Budget Optimization with CTE
```sql
WITH channel_performance AS (
    SELECT 
        channel,
        ROUND(SUM(spend), 2) as current_spend,
        ROUND(SUM(revenue), 2) as revenue,
        ROUND(SUM(revenue) / NULLIF(SUM(spend), 0), 2) as roas
    FROM campaigns
    WHERE spend > 0
    GROUP BY channel
)
SELECT 
    channel,
    current_spend,
    revenue,
    roas,
    CASE 
        WHEN roas < 2.0 THEN 'CUT BUDGET 50%'
        WHEN roas > 20.0 THEN 'INCREASE BUDGET 100%'
        WHEN roas > 10.0 THEN 'INCREASE BUDGET 50%'
        ELSE 'MAINTAIN'
    END as recommendation
FROM channel_performance
ORDER BY roas DESC;
```

---

🎓 Skills Demonstrated

✅ **Data Analysis** - Multi-channel campaign analysis with cohort segmentation  
✅ **SQL Proficiency** - Complex queries using CTEs, window functions, and aggregations  
✅ **Data Visualization** - Interactive Tableau dashboards and Excel charts  
✅ **Financial Modeling** - ROI projections and budget optimization scenarios  
✅ **Business Intelligence** - Actionable insights with measurable impact  
✅ **Technical Documentation** - Clear communication of methodology and findings

---

📬 Connect With Me

**Abdelrahman Isweisa**

- 💼 **LinkedIn:** [linkedin.com/in/abdelrahmanisweisa](https://linkedin.com/in/abdelrahmanisweisa)
- 💻 **GitHub:** [github.com/AbdelrahmanIsweisa](https://github.com/AbdelrahmanIsweisa)
- 📧 **Email:** abdelrahman_isweisa@student.uml.edu

---

📜 License

This project is open source and available under the MIT License.

---

⭐ If you found this project helpful, please consider starring the repository!**

---

*This portfolio project demonstrates end-to-end data analysis capabilities for marketing analytics and business intelligence roles.*
