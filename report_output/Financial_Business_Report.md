# 📊 FINANCIAL BUSINESS REPORT

## Trial Balance Analysis — Labhyansh Solution

**Report Generated:** April 2026
**Data Period:** April 2024 – August 2024 (FY 2024-25, Q1 & Q2)
**Data Source:** Trial Balance (Dummy Data for Review.xlsx)
**Prepared by:** Data Analytics Division

---

## 1. 🧹 Data Cleaning Summary

Before performing the analysis, the following cleaning steps were carried out to ensure data quality:

1. Removed 3 blank/empty rows from the dataset.
2. Removed 2 summary/total rows ('Profit & Loss A/c', 'Grand Total') to prevent double-counting.
3. No duplicate account entries found.
4. Standardized column names to: Account, Month, Debit, Credit, NetBalance, Category, SubCategory, StatementType.
5. Converted data from wide (pivot) format to long (flat) format for analysis.

> **Note:** No actual financial values were changed or manipulated. Only structural cleaning was done.

---

## 2. 📋 Data Understanding

### What is a Trial Balance?

A **Trial Balance** is a financial statement that lists all the accounts of a company along with their debit and credit balances at a specific point in time. It is used to:

- ✅ Verify that total debits equal total credits (basic accounting check)
- ✅ Serve as the foundation for preparing Profit & Loss and Balance Sheet statements
- ✅ Help identify any errors in bookkeeping

### Dataset Overview

| Metric | Value |
|--------|-------|
| Total Unique Accounts | 152 |
| Time Period | April 2024 – August 2024 (5 months) |
| Financial Year | FY 2024-25 |
| Quarters Covered | Q1 (Apr-Jun) and Q2 (Jul-Aug) |
| Total Data Records (after unpivoting) | 760 |

---

## 3. 🔧 Feature Creation

The following new fields were created to enable deeper analysis:

| Feature | Formula / Logic | Purpose |
|---------|-----------------|---------|
| **Net Balance** | Debit − Credit | Shows whether an account has a debit or credit balance |
| **Balance Type** | If Net > 0 → Debit, If Net < 0 → Credit | Quick classification of account direction |
| **Category** | Manual mapping | Groups accounts into: Assets, Liabilities, Equity, Revenue, Expenses |
| **SubCategory** | Manual mapping | Further grouping (e.g., Fixed Assets, Employee Expenses, Sales) |
| **Statement Type** | Manual mapping | Identifies if account belongs to Balance Sheet or P&L |

---

## 4. 💰 Key Financial Summary

![KPI Summary](report_output/01_kpi_summary.png)

### What These Numbers Mean

- **Total Revenue (₹67,828,095.32):** This is the total income the company has earned over 5 months from sales and other sources. Think of this as the total money coming into the business.

- **Total Expenses (₹61,051,045.52):** This is everything the company has spent — on raw materials (purchases), salaries, rent, utilities, transportation, and other operating costs.

- **Net Profit (₹6,777,049.80):** 🟢 The company is **profitable**. After paying all costs, ₹6,777,049.80 remains. The profit margin is **10.0%**, meaning for every ₹100 earned, ₹10.0 is profit.

- **Assets (₹248,069,021.26):** What the company owns — factory equipment, vehicles, bank balance, investments, receivables from customers.

- **Liabilities (₹49,065,883.78):** What the company owes to others — loans, taxes payable, creditor dues, employee dues.

- **Equity (₹149,802,350.12):** The owner's stake in the business — capital invested plus retained profits.

---

## 5. 📊 Category Analysis

![Category Split](report_output/05_category_pie.png)

### Category-wise Totals

| Category | Total Debit | Total Credit | Net Balance | Dominant Side |
|----------|-------------|-------------|-------------|---------------|
| Assets | ₹250,059,230.64 | ₹1,990,209.38 | ₹248,069,021.26 | Debit |
| Liabilities | ₹19,139,592.58 | ₹68,205,476.36 | ₹-49,065,883.78 | Credit |
| Equity | ₹0.00 | ₹149,802,350.12 | ₹-149,802,350.12 | Credit |
| Revenue | ₹2,500.00 | ₹67,830,595.32 | ₹-67,828,095.32 | Credit |
| Expenses | ₹61,315,605.34 | ₹264,559.82 | ₹61,051,045.52 | Debit |

### What This Means

- **Assets** show a **debit balance** — this is expected as assets are debit-nature accounts.
- **Liabilities & Equity** show **credit balances** — this means the company has obligations and capital on the books.
- **Revenue** shows a **credit balance** — income naturally sits on the credit side.
- **Expenses** show a **debit balance** — costs are debit-nature entries.

![Expense Breakdown](report_output/06_expense_breakdown.png)

### Top Expense Sub-Categories

| Rank | Sub-Category | Amount | % of Total Expenses |
|------|-------------|--------|---------------------|
| 1 | Purchases | ₹30,194,798.51 | 49.2% |
| 2 | Direct Expenses | ₹17,310,718.80 | 28.2% |
| 3 | Indirect Expenses | ₹5,574,570.57 | 9.1% |
| 4 | Employee Expenses | ₹4,805,463.00 | 7.8% |
| 5 | Rent | ₹1,553,029.75 | 2.5% |
| 6 | Repairs & Maintenance | ₹1,121,241.80 | 1.8% |
| 7 | Purchases - Discount | ₹260,047.89 | 0.4% |
| 8 | Admin & Professional | ₹148,509.44 | 0.2% |
| 9 | Other Expenses | ₹124,686.99 | 0.2% |
| 10 | Vehicle & Travel | ₹107,517.80 | 0.2% |

---

## 6. 🏆 Top Account Analysis

### Top 10 Accounts by Debit Amount

![Top Debit](report_output/02_top_debit_accounts.png)

These accounts had the **highest outflows** (debits) over the 5-month period:

| Rank | Account | Debit Total | Category | What It Means |
|------|---------|-------------|----------|---------------|
| 1 | Current Assets | ₹89,126,918.55 | Assets | Money invested in assets or receivables |
| 2 | Sundry Debtors | ₹30,958,286.23 | Assets | Money invested in assets or receivables |
| 3 | ADVANCE TAX | ₹23,894,750.00 | Assets | Money invested in assets or receivables |
| 4 | Fixed Assets | ₹22,514,484.50 | Assets | Money invested in assets or receivables |
| 5 | Bank Accounts | ₹22,478,549.92 | Assets | Money invested in assets or receivables |
| 6 | HDFC BANK | ₹22,478,549.92 | Assets | Money invested in assets or receivables |
| 7 | MACHINERY IGST 18% | ₹15,468,491.50 | Assets | Money invested in assets or receivables |
| 8 | Purchase Accounts | ₹15,227,423.20 | Expenses | Operating cost — money spent on business operations |
| 9 | PURCHASE IGST 5% | ₹12,658,843.60 | Expenses | Operating cost — money spent on business operations |
| 10 | Expenses (Direct) (Direct Expenses) | ₹8,655,359.40 | Expenses | Operating cost — money spent on business operations |

### Top 10 Accounts by Credit Amount

![Top Credit](report_output/03_top_credit_accounts.png)

These accounts had the **highest inflows** (credits) over the 5-month period:

| Rank | Account | Credit Total | Category | What It Means |
|------|---------|-------------|----------|---------------|
| 1 | Capital Account | ₹74,901,175.06 | Equity | Capital contributed by owner |
| 2 | MEHTA CAPITAL ACCOUNT | ₹64,924,115.06 | Equity | Capital contributed by owner |
| 3 | Sales Accounts | ₹33,740,842.16 | Revenue | Income earned from sales or other sources |
| 4 | Un Exempt Sales A/c | ₹33,740,842.16 | Revenue | Income earned from sales or other sources |
| 5 | Current Liabilities | ₹27,502,112.94 | Liabilities | Amount owed to vendors, employees, or government |
| 6 | Sundry Creditors | ₹18,091,146.90 | Liabilities | Amount owed to vendors, employees, or government |
| 7 | MY FACTORY (DELHI)`2 | ₹9,972,680.00 | Equity | Capital contributed by owner |
| 8 | Provisions | ₹7,535,746.00 | Liabilities | Amount owed to vendors, employees, or government |
| 9 | MANUFACTURING EXPENSES PAYABLE | ₹2,598,900.00 | Liabilities | Amount owed to vendors, employees, or government |
| 10 | PROVISION FOR EXPENSES | ₹2,359,692.00 | Liabilities | Amount owed to vendors, employees, or government |

---

## 7. 📈 Monthly Trend Analysis

![Monthly Trend](report_output/04_monthly_trend.png)

### Month-by-Month Performance

| Month | Revenue | Expenses | Net P&L | Status |
|-------|---------|----------|---------|--------|
| April 2024 | ₹10,518,281.14 | ₹11,023,812.16 | ₹-505,531.02 | 🔴 Loss |
| May 2024 | ₹13,834,280.66 | ₹13,140,551.46 | ₹693,729.20 | 🟢 Profit |
| June 2024 | ₹14,160,070.50 | ₹11,611,010.06 | ₹2,549,060.44 | 🟢 Profit |
| July 2024 | ₹14,580,549.38 | ₹13,128,650.00 | ₹1,451,899.38 | 🟢 Profit |
| August 2024 | ₹14,734,913.64 | ₹12,147,021.84 | ₹2,587,891.80 | 🟢 Profit |

### Trend Observations

- 📈 **Revenue is trending UPWARD** — growing from ₹1.05 Cr to ₹1.47 Cr
- 📈 **Expenses are trending UPWARD** — growing from ₹1.10 Cr to ₹1.21 Cr
- 🏆 **Best month:** August 2024 (Net: ₹2,587,891.80)
- ⚠️ **Weakest month:** April 2024 (Net: ₹-505,531.02)

![Monthly Stacked](report_output/07_monthly_stacked.png)

The **cumulative P&L** chart above shows how profits have been building up (or eroding) over the 5-month period. The final cumulative position is **₹6,777,049.80**.

---

## 8. 🎯 Concentration Analysis

![Concentration](report_output/08_concentration_pareto.png)

### Debit Concentration

- Out of **94** accounts with debit activity, just **11 accounts** (top 12%) account for **80% of all debit transactions**.

  ✅ Debit activity is reasonably distributed across accounts.

### Credit Concentration

- Out of **41** accounts with credit activity, just **5 accounts** (top 12%) account for **80% of all credit transactions**.

  ⚠️ **Revenue dependency risk:** Revenue is concentrated in very few accounts/sources. Losing any of these could severely impact income.

### What This Means for the Business

- If your **largest customer stops buying**, or your **biggest supplier raises prices**, the impact on the business would be disproportionately large.
- **Diversification** of both revenue sources and suppliers would reduce this risk.

---

## 9. 💡 Business Insights

Based on the detailed analysis, here are the most important insights for business stakeholders:

### 1. ✅ The Company is Profitable
- Net profit of **₹6,777,049.80** over 5 months with a margin of **10.0%**.
- The margin is **moderate** — there's room for improvement through cost optimization.

### 2. 📦 Purchases Dominate Expenses
- **Purchases** account for **49.2%** of total expenses (₹30,194,798.51).
- This is typical for a manufacturing/trading business, but negotiating better rates with suppliers could significantly improve margins.

### 3. 👥 Employee Costs
- Employee-related expenses (salary, EPF, ESIC, bonuses) total **₹4,805,463.00** (7.8% of expenses).
- This is within a reasonable range for the business size.

### 4. 🏭 Asset-Heavy Structure
- The company holds **₹248,069,021.26** in net assets, including factory machinery, vehicles, and equipment.
- This is typical for a **manufacturing business** — but it also means high depreciation costs and maintenance expenses.

### 5. 💵 Cash & Bank Position
- Net cash and bank position: **₹45,133,267.84**
- The company has positive cash reserves, which is healthy for meeting short-term obligations.

### 6. 🎯 Revenue Concentration Risk
- Only **5** accounts contribute 80% of all credit (revenue + other inflows).
- If the main sales channel or key customers are disrupted, the impact would be severe.
- **Recommendation:** Diversify customer base and explore new revenue streams.

### 7. 🏛️ Tax & Compliance
- Tax-related transactions (GST, TDS, Income Tax) total **₹38,259,433.94** on the debit side.
- The company is managing multiple tax components (CGST, SGST, IGST, TDS) — proper compliance requires diligent tracking.

---

## 10. 📸 Visual Summary Index

All charts generated as part of this report:

| # | Chart | Description |
|---|-------|-------------|
| 1 | KPI Summary Table | Key financial metrics at a glance |
| 2 | Top 10 Debit Accounts | Accounts with highest debit (outflow) amounts |
| 3 | Top 10 Credit Accounts | Accounts with highest credit (inflow) amounts |
| 4 | Monthly P&L Trend (Line) | Revenue vs Expenses over 5 months |
| 5 | Category Pie Charts | Distribution of debits and credits by category |
| 6 | Expense Breakdown (Bar) | Detailed breakdown of all expense sub-categories |
| 7 | Monthly Stacked Bar + Cumulative | Side-by-side revenue/expense comparison with cumulative P&L |
| 8 | Concentration / Pareto (Bar + Line) | Shows how few accounts dominate the totals |

---

## 11. 🏁 Final Conclusion

### Overall Financial Health Assessment

**Overall Status:** 🟢 GOOD

**Summary:** The company is profitable with a reasonable margin.

### Key Strengths

- ✅ Company is profitable and generating positive cash flow
- ✅ Strong asset base indicating long-term investment in the business
- ✅ Positive cash & bank position for meeting short-term needs
- ✅ Diverse expense structure across multiple categories
- ✅ Regular tax compliance (GST, TDS) indicates good governance

### Key Risks

- ⚠️ **Thin profit margin** (10.0%) — vulnerable to cost increases
- ⚠️ **Revenue concentration** — too dependent on a few sources
- ⚠️ **Asset-heavy structure** — high depreciation and maintenance overhead
- ⚠️ **No long-term debt visible** — may limit growth capacity if external funding is ever needed

---

## 12. 📋 Business Recommendations

Based on the analysis, here are **actionable recommendations** for the management:

### Recommendation 1: 🔄 Negotiate Better Purchase Rates
- Purchases are the **single largest expense** at ₹30,194,798.51.
- Even a 2–3% reduction in purchase costs through bulk deals or alternate suppliers could add significantly to the bottom line.

### Recommendation 2: 👥 Review Workforce Efficiency
- Employee costs total ₹4,805,463.00.
- Conduct a productivity audit — ensure the headcount is aligned with output needs. Consider automation for repetitive tasks.

### Recommendation 3: 🎯 Diversify Revenue Sources
- Revenue is concentrated in a few accounts/sales channels.
- Explore new markets, product lines, or distribution channels to reduce dependency risk.

### Recommendation 4: 💰 Build Cash Reserves
- Maintain at least 2-3 months of operating expenses as cash reserves.
- This provides a safety buffer against temporary disruptions in sales or unexpected costs.

### Recommendation 5: 📊 Implement Monthly Financial Reviews
- Use this type of analysis every month to track trends early.
- Set up KPI dashboards (as built with Power BI) for real-time monitoring.
- Identify problems **before** they become crises.

---

## Disclaimer

*This report has been prepared based on the Trial Balance data provided. No actual financial values were altered during analysis. The classifications and insights are based on standard accounting principles and the account structure observed in the dataset. This report should be used in conjunction with verified financial statements prepared by a qualified Chartered Accountant.*

---

**End of Report**