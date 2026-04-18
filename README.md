<div align="center">

# Labhyansh Solution

### Financial Business Report & Interactive Dashboard

[![Live Dashboard](https://img.shields.io/badge/Live_Dashboard-View_Now-2ea44f?style=for-the-badge&logo=googlechrome&logoColor=white)](https://aviral022.github.io/Labhyash_Assesment/)
[![Presentation](https://img.shields.io/badge/Presentation-View_Slides-8B5CF6?style=for-the-badge&logo=googlechrome&logoColor=white)](https://aviral022.github.io/Labhyash_Assesment/presentation.html)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)](https://chartjs.org)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

A comprehensive financial analysis built from a **Trial Balance** dataset covering **April to August 2024 (FY 2024-25)**. Raw accounting data is transformed into actionable business insights through data cleaning, financial modeling, and interactive visualizations.

</div>

---

## Live Preview

> **Dashboard:** [aviral022.github.io/Labhyash_Assesment](https://aviral022.github.io/Labhyash_Assesment/)
>
> **Presentation:** [aviral022.github.io/Labhyash_Assesment/presentation.html](https://aviral022.github.io/Labhyash_Assesment/presentation.html)

The interactive dashboard features glassmorphism design, hover enabled Chart.js charts, tab switching between Bar and Line views, scroll animations, and full responsiveness. The presentation is a 13 slide interactive deck with keyboard navigation, interactive charts, and professional dark theme.

---

## Highlights at a Glance

| Metric | Value | Status |
|:-------|------:|:------:|
| Total Revenue (5 months) | Rs. 6.78 Cr | |
| Total Expenses | Rs. 6.11 Cr | |
| **Net Profit** | **Rs. 67.77 L** | Profitable |
| Profit Margin | 10.0% | Moderate |
| Revenue Growth (Apr to Aug) | +40% | Growing |
| Net Assets | Rs. 24.81 Cr | Strong |
| Cash & Bank Reserves | Rs. 4.51 Cr | Healthy |

---

## What's Included

### 1. Interactive Dashboard (`index.html`)
Glassmorphism dark theme with 7 interactive Chart.js visualizations. Hover over any data point for details, switch between Bar and Line views, and explore expense breakdowns, category distributions, and monthly trends. KPI cards, monthly breakdown table, and an insights + risks panel all in one scrollable page.

### 2. Slide Presentation (`report_output/Financial_Report_Presentation.html`)
16 slide presentation with keyboard navigation (arrow keys). Professional dark theme with smooth transitions and all 8 charts embedded. Single HTML file, fully self contained, shareable directly.

### 3. Full Written Report (`report_output/Financial_Business_Report.md`)
12 section comprehensive business report covering data cleaning, KPI summary, category analysis, top accounts, monthly trends, concentration analysis, 7 business insights, and 5 actionable recommendations. Written in plain business language.

### 4. Static Charts (8 PNG files in `report_output/`)
High resolution charts for use in PowerPoint, Word, or any document: KPI table, top debit/credit accounts, monthly trend, category pies, expense breakdown, stacked bar with cumulative P&L, and Pareto concentration chart.

---

## Analysis Performed

| # | Analysis | Description |
|---|----------|-------------|
| 1 | **Data Cleaning** | Removed blanks, summary rows; standardized formats |
| 2 | **Feature Engineering** | Net Balance, Account Classification (Assets / Liabilities / Equity / Revenue / Expenses) |
| 3 | **Financial Summary** | Revenue, Expenses, Profit, Margin calculations |
| 4 | **Category Analysis** | Debit / Credit distribution by financial category |
| 5 | **Top Account Analysis** | Highest debit and credit accounts with business meaning |
| 6 | **Monthly Trends** | Revenue growth, expense tracking, cumulative P&L |
| 7 | **Concentration Analysis** | Pareto 80/20 risk assessment |
| 8 | **Business Insights** | Cash flow, revenue dependency, cost structure, recommendations |

---

## Project Structure

```
Labhyansh Solution/
  index.html                              Interactive Dashboard (GitHub Pages)
  presentation.html                       Interactive Presentation (13 slides)
  Dummy Data for Review.xlsx              Source data (Trial Balance)
  generate_report.py                      Data analysis and chart generation
  create_dashboard.py                     Interactive dashboard generator
  create_presentation.py                  Slide presentation generator
  clean_data.py                           Data cleaning and CSV export pipeline
  README.md                              This file
  cleaned_data/
    fact_transactions.csv                 Main fact table (760 records)
    dim_accounts.csv                      Account dimension (152 accounts)
    dim_calendar.csv                      Calendar dimension (5 months)
    summary_monthly_pl.csv                Monthly P and L summary
    summary_category.csv                  Category level aggregates
    summary_expense_subcats.csv           Expense sub category breakdown
    summary_top_accounts.csv              Top accounts by debit and credit
    summary_balance_sheet.csv             Balance sheet snapshot
    kpi_summary.json                      All KPIs in JSON format
    Analysis_Insights.md                  Comprehensive analysis report
    cleaning_log.txt                      Data cleaning audit trail
  report_output/
    Financial_Dashboard.html              Dashboard (copy of index.html)
    Financial_Report_Presentation.html    16 slide presentation (legacy)
    Financial_Business_Report.md          Full written report
    01_kpi_summary.png                    KPI summary table
    02_top_debit_accounts.png             Top debit accounts chart
    03_top_credit_accounts.png            Top credit accounts chart
    04_monthly_trend.png                  Revenue vs Expenses trend
    05_category_pie.png                   Category distribution
    06_expense_breakdown.png              Expense breakdown
    07_monthly_stacked.png                Monthly stacked and cumulative
    08_concentration_pareto.png           Concentration analysis
```

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Data Processing | Python, openpyxl | Extract and clean Trial Balance data |
| Static Charts | matplotlib | Generate high resolution PNG charts |
| Interactive Charts | Chart.js 4.4 | Hover enabled, togglable browser charts |
| Frontend | HTML5, CSS3, JavaScript | Glassmorphism UI, scroll animations |
| Typography | Inter, JetBrains Mono | Modern readable fonts via Google Fonts |
| Hosting | GitHub Pages | Free, fast, reliable static hosting |

---

## Run Locally

```bash
# Clone the repository
git clone https://github.com/aviral022/Labhyash_Assesment.git
cd Labhyash_Assesment

# Install dependencies
pip install openpyxl matplotlib

# Generate report and static charts
python generate_report.py

# Generate interactive dashboard
python create_dashboard.py

# Generate slide presentation
python create_presentation.py

# Clean data and export CSVs for dashboarding
python clean_data.py

# Open dashboard in browser
start index.html

# Open presentation in browser
start presentation.html
```

---

## Key Business Recommendations

1. **Negotiate Better Purchase Rates** : Purchases are the single largest expense at Rs. 3.02 Cr. A 2 to 3% reduction adds Rs. 6 to 9L to profit.
2. **Diversify Revenue Sources** : Only 5 accounts contribute 80% of all inflows. Customer concentration is a major risk.
3. **Review Workforce Efficiency** : Conduct a productivity audit and consider automation for repetitive tasks.
4. **Build Cash Reserves** : Maintain 2 to 3 months of operating expenses as a safety buffer.
5. **Monthly Financial Reviews** : Use dashboards and trend analysis to catch issues early.

---

## Author

**Aviral Dubey**

---

<div align="center">
<sub>Data integrity notice: No actual financial values were altered during analysis. Only structural cleaning (removing blanks, summary rows) was performed. This report should be used alongside verified financial statements prepared by a qualified Chartered Accountant.</sub>
</div>
