# Labhyansh Solution — Financial Business Report

## Overview

A comprehensive financial analysis and interactive dashboard built from a **Trial Balance** dataset (April 2024 - August 2024). This project transforms raw accounting data into actionable business insights through data cleaning, financial modeling, and professional visualizations.

**Live Dashboard:** [View Interactive Dashboard](https://aviral022.github.io/Labhyash_Assesment/)

---

## Key Findings

| Metric | Value |
|--------|-------|
| Total Revenue (5 months) | Rs. 6.78 Cr |
| Total Expenses | Rs. 6.11 Cr |
| Net Profit | Rs. 67.77 L |
| Profit Margin | 10.0% |
| Revenue Growth | +40% (Apr to Aug) |
| Net Assets | Rs. 24.81 Cr |

---

## Project Structure

```
├── index.html                          # Interactive Dashboard (GitHub Pages)
├── Dummy Data for Review.xlsx          # Source data (Trial Balance)
├── generate_report.py                  # Data analysis & chart generation
├── create_dashboard.py                 # Interactive dashboard generator
├── create_presentation.py              # Slide presentation generator
└── report_output/
    ├── Financial_Dashboard.html        # Dashboard (copy of index.html)
    ├── Financial_Report_Presentation.html  # 16-slide presentation
    ├── Financial_Business_Report.md    # Full written report
    ├── 01_kpi_summary.png             # KPI summary table
    ├── 02_top_debit_accounts.png      # Top debit accounts chart
    ├── 03_top_credit_accounts.png     # Top credit accounts chart
    ├── 04_monthly_trend.png           # Revenue vs Expenses trend
    ├── 05_category_pie.png            # Category distribution
    ├── 06_expense_breakdown.png       # Expense breakdown
    ├── 07_monthly_stacked.png         # Monthly stacked + cumulative
    └── 08_concentration_pareto.png    # Concentration analysis
```

---

## What's Included

### 1. Interactive Dashboard (`index.html`)
- Glassmorphism dark-themed UI
- 7 interactive charts (Chart.js) — hover for details, switch between Bar/Line views
- KPI cards, monthly breakdown table, insights panel
- Fully responsive, works on all screen sizes

### 2. Slide Presentation (`report_output/Financial_Report_Presentation.html`)
- 16-slide presentation with keyboard navigation
- Professional dark theme with smooth transitions
- All charts embedded — single file, no dependencies

### 3. Written Report (`report_output/Financial_Business_Report.md`)
- 12-section comprehensive business report
- Data cleaning, KPI summary, category analysis, monthly trends
- 7 business insights and 5 actionable recommendations

---

## Analysis Performed

1. **Data Cleaning** — Removed blanks, summary rows; standardized formats
2. **Feature Engineering** — Net Balance, Account Classification (Assets/Liabilities/Equity/Revenue/Expenses)
3. **Financial Summary** — Revenue, Expenses, Profit, Margin calculations
4. **Category Analysis** — Debit/Credit distribution by financial category
5. **Top Account Analysis** — Highest debit and credit accounts
6. **Monthly Trends** — Revenue growth, expense tracking, cumulative P&L
7. **Concentration Analysis** — Pareto/80-20 risk assessment
8. **Business Insights** — Cash flow, revenue dependency, cost structure

---

## Tech Stack

- **Python** — Data extraction and analysis (openpyxl, matplotlib)
- **Chart.js** — Interactive browser-based charts
- **HTML/CSS/JS** — Glassmorphism dashboard, no framework dependencies
- **GitHub Pages** — Hosting

---

## How to Run Locally

```bash
# Install dependencies
pip install openpyxl matplotlib

# Generate report and charts
python generate_report.py

# Generate interactive dashboard
python create_dashboard.py

# Generate slide presentation
python create_presentation.py

# Open dashboard
start report_output/Financial_Dashboard.html
```

---

## Author

**Aviral Dubey**

---

*Data integrity notice: No actual financial values were altered during analysis. Only structural cleaning (removing blanks, summary rows) was performed.*
