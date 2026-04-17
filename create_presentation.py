#!/usr/bin/env python3
"""
Generate a professional HTML presentation from the financial report data.
Embeds all charts as base64 images so the HTML file is fully self-contained.
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import base64
import os

OUTPUT_DIR = "report_output"
PRESENTATION_FILE = os.path.join(OUTPUT_DIR, "Financial_Report_Presentation.html")

# ── Load all chart images as base64 ─────────────────────────────
def img_to_base64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

charts = {}
chart_files = [
    '01_kpi_summary.png',
    '02_top_debit_accounts.png',
    '03_top_credit_accounts.png',
    '04_monthly_trend.png',
    '05_category_pie.png',
    '06_expense_breakdown.png',
    '07_monthly_stacked.png',
    '08_concentration_pareto.png',
]

for cf in chart_files:
    path = os.path.join(OUTPUT_DIR, cf)
    if os.path.exists(path):
        charts[cf] = img_to_base64(path)
        print(f"  ✓ Loaded {cf}")
    else:
        print(f"  ✗ Missing {cf}")
        charts[cf] = ""

# ── Build the HTML Presentation ─────────────────────────────────

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Financial Business Report — Labhyansh Solution</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --primary: #0F172A;
    --primary-light: #1E293B;
    --accent: #3B82F6;
    --accent-glow: #60A5FA;
    --green: #10B981;
    --green-bg: rgba(16, 185, 129, 0.1);
    --red: #EF4444;
    --red-bg: rgba(239, 68, 68, 0.1);
    --amber: #F59E0B;
    --amber-bg: rgba(245, 158, 11, 0.1);
    --purple: #8B5CF6;
    --text: #F8FAFC;
    --text-muted: #94A3B8;
    --card-bg: rgba(30, 41, 59, 0.6);
    --card-border: rgba(59, 130, 246, 0.15);
    --glass: rgba(15, 23, 42, 0.85);
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--primary);
    color: var(--text);
    overflow: hidden;
    height: 100vh;
    width: 100vw;
  }}

  /* ── SLIDE SYSTEM ─────────────────────────────── */
  .slide {{
    position: absolute;
    top: 0; left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px 60px;
    opacity: 0;
    transform: translateX(60px);
    transition: opacity 0.5s ease, transform 0.5s ease;
    pointer-events: none;
    overflow-y: auto;
    background: var(--primary);
  }}

  .slide.active {{
    opacity: 1;
    transform: translateX(0);
    pointer-events: all;
  }}

  .slide.exit {{
    opacity: 0;
    transform: translateX(-60px);
  }}

  /* ── NAVIGATION ─────────────────────────────── */
  .nav-bar {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: var(--glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-top: 1px solid var(--card-border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 30px;
    z-index: 1000;
  }}

  .nav-btn {{
    background: transparent;
    border: 1px solid rgba(59, 130, 246, 0.3);
    color: var(--accent-glow);
    padding: 8px 24px;
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
  }}

  .nav-btn:hover {{
    background: rgba(59, 130, 246, 0.15);
    border-color: var(--accent);
    transform: translateY(-1px);
  }}

  .nav-btn:disabled {{
    opacity: 0.3;
    cursor: not-allowed;
    transform: none;
  }}

  .slide-counter {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--text-muted);
  }}

  .progress-bar {{
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent), var(--purple));
    transition: width 0.5s ease;
    z-index: 1001;
    border-radius: 0 2px 2px 0;
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
  }}

  /* ── TYPOGRAPHY ─────────────────────────────── */
  .slide-title {{
    font-size: 2.8em;
    font-weight: 800;
    background: linear-gradient(135deg, #F8FAFC, #94A3B8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
    text-align: center;
    line-height: 1.2;
  }}

  .slide-subtitle {{
    font-size: 1.15em;
    color: var(--text-muted);
    font-weight: 400;
    text-align: center;
    margin-bottom: 40px;
  }}

  .section-badge {{
    display: inline-block;
    padding: 6px 16px;
    background: rgba(59, 130, 246, 0.15);
    border: 1px solid rgba(59, 130, 246, 0.25);
    border-radius: 20px;
    font-size: 0.8em;
    font-weight: 600;
    color: var(--accent-glow);
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 16px;
  }}

  /* ── CARDS ─────────────────────────────── */
  .card-grid {{
    display: grid;
    gap: 20px;
    width: 100%;
    max-width: 1200px;
  }}

  .card-grid-2 {{ grid-template-columns: 1fr 1fr; }}
  .card-grid-3 {{ grid-template-columns: 1fr 1fr 1fr; }}
  .card-grid-4 {{ grid-template-columns: 1fr 1fr 1fr 1fr; }}

  .card {{
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 16px;
    padding: 24px;
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease, border-color 0.3s ease;
  }}

  .card:hover {{
    transform: translateY(-3px);
    border-color: rgba(59, 130, 246, 0.35);
  }}

  .card-label {{
    font-size: 0.8em;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
    margin-bottom: 8px;
  }}

  .card-value {{
    font-size: 1.8em;
    font-weight: 700;
    margin-bottom: 4px;
    font-family: 'JetBrains Mono', monospace;
  }}

  .card-desc {{
    font-size: 0.85em;
    color: var(--text-muted);
    line-height: 1.4;
  }}

  .green {{ color: var(--green); }}
  .red {{ color: var(--red); }}
  .amber {{ color: var(--amber); }}
  .blue {{ color: var(--accent-glow); }}
  .purple {{ color: var(--purple); }}

  /* ── KPI HIGHLIGHT ─────────────────────────── */
  .kpi-hero {{
    display: flex;
    align-items: center;
    gap: 32px;
    max-width: 1200px;
    width: 100%;
  }}

  .kpi-big {{
    flex: 0 0 320px;
    text-align: center;
    padding: 40px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(59, 130, 246, 0.08));
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 20px;
  }}

  .kpi-big .big-number {{
    font-size: 3.2em;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    color: var(--green);
    line-height: 1;
    margin-bottom: 8px;
  }}

  .kpi-big .big-label {{
    font-size: 1em;
    color: var(--text-muted);
    font-weight: 500;
  }}

  /* ── CHART IMAGE ─────────────────────────── */
  .chart-container {{
    max-width: 1100px;
    width: 100%;
    text-align: center;
  }}

  .chart-container img {{
    max-width: 100%;
    max-height: 55vh;
    border-radius: 12px;
    border: 1px solid var(--card-border);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  }}

  .chart-caption {{
    margin-top: 16px;
    font-size: 0.95em;
    color: var(--text-muted);
    text-align: center;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.5;
  }}

  /* ── TABLE ─────────────────────────────── */
  .styled-table {{
    width: 100%;
    max-width: 1100px;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--card-border);
    font-size: 0.95em;
  }}

  .styled-table thead th {{
    background: rgba(59, 130, 246, 0.15);
    color: var(--accent-glow);
    padding: 14px 18px;
    text-align: left;
    font-weight: 600;
    font-size: 0.85em;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    border-bottom: 1px solid var(--card-border);
  }}

  .styled-table tbody td {{
    padding: 12px 18px;
    border-bottom: 1px solid rgba(59, 130, 246, 0.08);
    color: var(--text);
  }}

  .styled-table tbody tr {{
    transition: background 0.2s ease;
  }}

  .styled-table tbody tr:hover {{
    background: rgba(59, 130, 246, 0.06);
  }}

  .styled-table tbody tr:last-child td {{
    border-bottom: none;
  }}

  .mono {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9em;
  }}

  /* ── BULLET LIST ─────────────────────────── */
  .bullet-list {{
    max-width: 900px;
    width: 100%;
    list-style: none;
  }}

  .bullet-list li {{
    padding: 14px 20px;
    margin-bottom: 10px;
    background: var(--card-bg);
    border-left: 3px solid var(--accent);
    border-radius: 0 12px 12px 0;
    font-size: 1em;
    line-height: 1.6;
    color: #CBD5E1;
    transition: transform 0.2s ease;
  }}

  .bullet-list li:hover {{
    transform: translateX(6px);
  }}

  .bullet-list li strong {{
    color: var(--text);
  }}

  .bullet-list li.green-border {{ border-left-color: var(--green); }}
  .bullet-list li.red-border {{ border-left-color: var(--red); }}
  .bullet-list li.amber-border {{ border-left-color: var(--amber); }}
  .bullet-list li.purple-border {{ border-left-color: var(--purple); }}

  /* ── TAG / PILL ─────────────────────────── */
  .tag {{
    display: inline-block;
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 0.8em;
    font-weight: 600;
  }}

  .tag-green {{ background: var(--green-bg); color: var(--green); }}
  .tag-red {{ background: var(--red-bg); color: var(--red); }}
  .tag-amber {{ background: var(--amber-bg); color: var(--amber); }}

  /* ── COVER SLIDE ─────────────────────────── */
  .cover-slide {{
    background: linear-gradient(135deg, #0F172A 0%, #1a1f3a 40%, #162044 100%);
    text-align: center;
  }}

  .cover-slide::before {{
    content: '';
    position: absolute;
    top: -200px;
    right: -200px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
    border-radius: 50%;
  }}

  .cover-slide::after {{
    content: '';
    position: absolute;
    bottom: -150px;
    left: -150px;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.06) 0%, transparent 70%);
    border-radius: 50%;
  }}

  .cover-logo {{
    font-size: 4.5em;
    margin-bottom: 16px;
  }}

  .cover-title {{
    font-size: 3.5em;
    font-weight: 900;
    background: linear-gradient(135deg, #FFFFFF, #60A5FA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 12px;
    line-height: 1.15;
  }}

  .cover-sub {{
    font-size: 1.3em;
    color: var(--text-muted);
    font-weight: 300;
    margin-bottom: 40px;
  }}

  .cover-meta {{
    display: flex;
    gap: 40px;
    justify-content: center;
  }}

  .cover-meta-item {{
    text-align: center;
  }}

  .cover-meta-item .label {{
    font-size: 0.75em;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
  }}

  .cover-meta-item .value {{
    font-size: 1em;
    color: var(--accent-glow);
    font-weight: 600;
  }}

  /* ── END SLIDE ─────────────────────────── */
  .end-slide {{
    background: linear-gradient(135deg, #0F172A, #1a1f3a);
    text-align: center;
  }}

  /* ── INSIGHT CARD ─────────────────────────── */
  .insight-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    max-width: 1100px;
    width: 100%;
  }}

  .insight-card {{
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 20px 24px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
    transition: transform 0.2s ease;
  }}

  .insight-card:hover {{ transform: translateY(-2px); }}

  .insight-icon {{
    font-size: 1.6em;
    flex-shrink: 0;
    width: 40px;
    text-align: center;
  }}

  .insight-text h4 {{
    font-size: 0.95em;
    font-weight: 700;
    margin-bottom: 4px;
    color: var(--text);
  }}

  .insight-text p {{
    font-size: 0.85em;
    color: var(--text-muted);
    line-height: 1.5;
  }}

  /* ── RECOMMENDATION CARD ───────────────── */
  .rec-card {{
    display: flex;
    gap: 20px;
    max-width: 1000px;
    width: 100%;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 14px;
    align-items: flex-start;
    transition: transform 0.2s, border-color 0.2s;
  }}

  .rec-card:hover {{
    transform: translateX(6px);
    border-color: rgba(59, 130, 246, 0.3);
  }}

  .rec-num {{
    flex-shrink: 0;
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, var(--accent), var(--purple));
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1.1em;
    color: white;
  }}

  .rec-content h4 {{
    font-size: 1.05em;
    font-weight: 700;
    margin-bottom: 6px;
  }}

  .rec-content p {{
    font-size: 0.9em;
    color: var(--text-muted);
    line-height: 1.5;
  }}

  /* ── STATUS INDICATORS ───────────────── */
  .status-row {{
    display: flex;
    gap: 10px;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(59, 130, 246, 0.08);
  }}

  .status-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }}

  .status-dot.good {{ background: var(--green); box-shadow: 0 0 8px rgba(16, 185, 129, 0.4); }}
  .status-dot.warn {{ background: var(--amber); box-shadow: 0 0 8px rgba(245, 158, 11, 0.4); }}
  .status-dot.bad {{ background: var(--red); box-shadow: 0 0 8px rgba(239, 68, 68, 0.4); }}

  /* ── KEYBOARD HINT ───────────────── */
  .kb-hint {{
    position: fixed;
    bottom: 70px;
    right: 30px;
    font-size: 0.75em;
    color: rgba(148, 163, 184, 0.4);
    z-index: 1001;
  }}

  kbd {{
    background: rgba(59, 130, 246, 0.1);
    border: 1px solid rgba(59, 130, 246, 0.2);
    border-radius: 4px;
    padding: 2px 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9em;
  }}

  @media print {{
    .nav-bar, .progress-bar, .kb-hint {{ display: none; }}
    .slide {{ position: relative; page-break-after: always; opacity: 1; transform: none; pointer-events: all; overflow: visible; height: auto; min-height: 100vh; }}
  }}
</style>
</head>
<body>

<div class="progress-bar" id="progressBar"></div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 1: COVER -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide cover-slide active" id="slide-0">
  <div class="cover-logo">📊</div>
  <h1 class="cover-title">Financial Business Report</h1>
  <p class="cover-sub">Trial Balance Analysis — Labhyansh Solution</p>
  <div class="cover-meta">
    <div class="cover-meta-item">
      <div class="label">Period</div>
      <div class="value">Apr – Aug 2024</div>
    </div>
    <div class="cover-meta-item">
      <div class="label">Financial Year</div>
      <div class="value">FY 2024-25</div>
    </div>
    <div class="cover-meta-item">
      <div class="label">Accounts Analyzed</div>
      <div class="value">152</div>
    </div>
    <div class="cover-meta-item">
      <div class="label">Data Records</div>
      <div class="value">760</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 2: DATA CLEANING -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-1">
  <span class="section-badge">Section 1</span>
  <h2 class="slide-title">Data Cleaning & Preparation</h2>
  <p class="slide-subtitle">What was done before the analysis to ensure data quality</p>

  <ul class="bullet-list">
    <li class="green-border"><strong>Removed 3 blank rows</strong> — Empty rows that had no account name or values were excluded</li>
    <li class="green-border"><strong>Removed 2 summary rows</strong> — "Profit &amp; Loss A/c" and "Grand Total" rows were excluded to prevent double-counting</li>
    <li class="green-border"><strong>No duplicates found</strong> — All 152 account entries were unique</li>
    <li class="green-border"><strong>Converted to numeric</strong> — All Debit/Credit fields were standardized to numbers (some had formulas)</li>
    <li class="green-border"><strong>Unpivoted data</strong> — Transformed from wide format (5 month columns) to long format (760 individual records)</li>
    <li class="purple-border"><strong>Created new features</strong> — Net Balance, Balance Type, Category, SubCategory, Statement Type</li>
  </ul>

  <p style="margin-top: 20px; color: var(--text-muted); font-size: 0.9em; text-align: center;">
    ⚠️ <em>No actual financial values were changed or manipulated. Only structural cleaning was performed.</em>
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 3: KPI SUMMARY -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-2">
  <span class="section-badge">Section 2</span>
  <h2 class="slide-title">Key Financial Indicators</h2>
  <p class="slide-subtitle">The most important numbers at a glance (April – August 2024)</p>

  <div class="kpi-hero">
    <div class="kpi-big">
      <div class="big-number">₹67.77L</div>
      <div class="big-label">Net Profit (5 months)</div>
      <div style="margin-top: 12px;">
        <span class="tag tag-green">10.0% Margin</span>
      </div>
    </div>
    <div class="card-grid card-grid-2" style="flex: 1;">
      <div class="card">
        <div class="card-label">Total Revenue</div>
        <div class="card-value green mono">₹6.78Cr</div>
        <div class="card-desc">Income from sales & other sources</div>
      </div>
      <div class="card">
        <div class="card-label">Total Expenses</div>
        <div class="card-value red mono">₹6.11Cr</div>
        <div class="card-desc">Purchases, salaries, operations</div>
      </div>
      <div class="card">
        <div class="card-label">Net Assets</div>
        <div class="card-value blue mono">₹24.81Cr</div>
        <div class="card-desc">What the company owns</div>
      </div>
      <div class="card">
        <div class="card-label">Owner's Equity</div>
        <div class="card-value purple mono">₹14.98Cr</div>
        <div class="card-desc">Capital invested in business</div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 4: KPI TABLE (CHART) -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-3">
  <span class="section-badge">Section 2</span>
  <h2 class="slide-title">KPI Summary Table</h2>
  <p class="slide-subtitle">Detailed view of all key metrics with business explanations</p>
  <div class="chart-container">
    <img src="data:image/png;base64,{charts['01_kpi_summary.png']}" alt="KPI Summary Table">
  </div>
  <p class="chart-caption">
    The company earned ₹6.78 Cr in revenue and spent ₹6.11 Cr, resulting in a 10% profit margin. 
    For every ₹100 earned, ₹10 remains as profit after all costs are paid.
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 5: CATEGORY ANALYSIS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-4">
  <span class="section-badge">Section 3</span>
  <h2 class="slide-title">Category Analysis</h2>
  <p class="slide-subtitle">How the financial categories are distributed across debits and credits</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['05_category_pie.png']}" alt="Category Pie Charts">
  </div>
  <p class="chart-caption">
    <strong>Debit side:</strong> Assets dominate (75.7%) — the company has heavy investments in assets.<br>
    <strong>Credit side:</strong> Equity leads (52.0%) — strong owner investment, followed by Revenue (23.5%).
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 6: CATEGORY TABLE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-5">
  <span class="section-badge">Section 3</span>
  <h2 class="slide-title">Category-wise Financial Summary</h2>
  <p class="slide-subtitle">Debit vs Credit breakdown for each financial category</p>

  <table class="styled-table">
    <thead>
      <tr>
        <th>Category</th>
        <th>Total Debit</th>
        <th>Total Credit</th>
        <th>Net Balance</th>
        <th>Side</th>
        <th>Meaning</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Assets</strong></td>
        <td class="mono">₹25.01 Cr</td>
        <td class="mono">₹19.90 L</td>
        <td class="mono green">₹24.81 Cr</td>
        <td><span class="tag tag-green">Debit</span></td>
        <td>What the company owns</td>
      </tr>
      <tr>
        <td><strong>Liabilities</strong></td>
        <td class="mono">₹1.91 Cr</td>
        <td class="mono">₹6.82 Cr</td>
        <td class="mono red">-₹4.91 Cr</td>
        <td><span class="tag tag-red">Credit</span></td>
        <td>What the company owes</td>
      </tr>
      <tr>
        <td><strong>Equity</strong></td>
        <td class="mono">₹0.00</td>
        <td class="mono">₹14.98 Cr</td>
        <td class="mono" style="color:var(--purple)">-₹14.98 Cr</td>
        <td><span class="tag tag-red">Credit</span></td>
        <td>Owner's capital</td>
      </tr>
      <tr>
        <td><strong>Revenue</strong></td>
        <td class="mono">₹2,500</td>
        <td class="mono">₹6.78 Cr</td>
        <td class="mono green">-₹6.78 Cr</td>
        <td><span class="tag tag-green">Credit</span></td>
        <td>Income earned</td>
      </tr>
      <tr>
        <td><strong>Expenses</strong></td>
        <td class="mono">₹6.13 Cr</td>
        <td class="mono">₹2.65 L</td>
        <td class="mono red">₹6.11 Cr</td>
        <td><span class="tag tag-red">Debit</span></td>
        <td>Costs incurred</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 7: EXPENSE BREAKDOWN -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-6">
  <span class="section-badge">Section 4</span>
  <h2 class="slide-title">Expense Breakdown</h2>
  <p class="slide-subtitle">Where the company's money is being spent</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['06_expense_breakdown.png']}" alt="Expense Breakdown">
  </div>
  <p class="chart-caption">
    <strong>Purchases (49.2%)</strong> and <strong>Direct Expenses (28.2%)</strong> together make up 77.4% of all costs.
    Negotiating even 2–3% better rates on purchases could add ₹6–9 Lakhs to profit.
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 8: TOP DEBIT ACCOUNTS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-7">
  <span class="section-badge">Section 5</span>
  <h2 class="slide-title">Top 10 Accounts — Debit (Outflows)</h2>
  <p class="slide-subtitle">Accounts with the highest debit activity over 5 months</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['02_top_debit_accounts.png']}" alt="Top Debit Accounts">
  </div>
  <p class="chart-caption">
    Asset accounts dominate the debit side — Current Assets (₹8.91 Cr), Sundry Debtors (₹3.10 Cr), and Fixed Assets (₹2.25 Cr) 
    reflect significant investment in business infrastructure and customer receivables.
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 9: TOP CREDIT ACCOUNTS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-8">
  <span class="section-badge">Section 5</span>
  <h2 class="slide-title">Top 10 Accounts — Credit (Inflows)</h2>
  <p class="slide-subtitle">Accounts with the highest credit activity over 5 months</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['03_top_credit_accounts.png']}" alt="Top Credit Accounts">
  </div>
  <p class="chart-caption">
    Capital accounts (₹7.49 Cr + ₹6.49 Cr) lead the credit side, followed by Sales (₹3.37 Cr). 
    This shows the business is primarily funded by owner capital and sustained by sales revenue.
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 10: MONTHLY TREND -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-9">
  <span class="section-badge">Section 6</span>
  <h2 class="slide-title">Monthly Revenue vs Expenses</h2>
  <p class="slide-subtitle">5-month performance trend — April to August 2024</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['04_monthly_trend.png']}" alt="Monthly Trend">
  </div>
  <p class="chart-caption">
    📈 Revenue grew <strong>40%</strong> from April (₹1.05 Cr) to August (₹1.47 Cr).
    After an initial loss in April, the company has been <strong>consistently profitable</strong> for 4 straight months.
  </p>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 11: MONTHLY TABLE + CUMULATIVE -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-10">
  <span class="section-badge">Section 6</span>
  <h2 class="slide-title">Monthly P&L + Cumulative Profit</h2>
  <p class="slide-subtitle">Side-by-side comparison with cumulative profitability trend</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['07_monthly_stacked.png']}" alt="Monthly Stacked">
  </div>

  <table class="styled-table" style="margin-top: 20px; max-width: 900px;">
    <thead>
      <tr><th>Month</th><th>Revenue</th><th>Expenses</th><th>Net P&L</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr><td>April 2024</td><td class="mono">₹1.05 Cr</td><td class="mono">₹1.10 Cr</td><td class="mono red">-₹5.06 L</td><td><span class="tag tag-red">Loss</span></td></tr>
      <tr><td>May 2024</td><td class="mono">₹1.38 Cr</td><td class="mono">₹1.31 Cr</td><td class="mono green">₹6.94 L</td><td><span class="tag tag-green">Profit</span></td></tr>
      <tr><td>June 2024</td><td class="mono">₹1.42 Cr</td><td class="mono">₹1.16 Cr</td><td class="mono green">₹25.49 L</td><td><span class="tag tag-green">Profit</span></td></tr>
      <tr><td>July 2024</td><td class="mono">₹1.46 Cr</td><td class="mono">₹1.31 Cr</td><td class="mono green">₹14.52 L</td><td><span class="tag tag-green">Profit</span></td></tr>
      <tr><td>August 2024</td><td class="mono">₹1.47 Cr</td><td class="mono">₹1.21 Cr</td><td class="mono green">₹25.88 L</td><td><span class="tag tag-green">Profit</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 12: CONCENTRATION ANALYSIS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-11">
  <span class="section-badge">Section 7</span>
  <h2 class="slide-title">Concentration Analysis</h2>
  <p class="slide-subtitle">Are too few accounts controlling too much of the financials?</p>

  <div class="chart-container">
    <img src="data:image/png;base64,{charts['08_concentration_pareto.png']}" alt="Concentration Pareto">
  </div>

  <div class="card-grid card-grid-2" style="max-width: 900px; margin-top: 20px;">
    <div class="card">
      <div class="card-label">Debit Concentration</div>
      <div class="card-value amber mono">11 / 94</div>
      <div class="card-desc">Just 11 accounts (12%) control 80% of all debit transactions. Moderately distributed.</div>
    </div>
    <div class="card" style="border-left: 3px solid var(--red);">
      <div class="card-label">Credit Concentration ⚠️</div>
      <div class="card-value red mono">5 / 41</div>
      <div class="card-desc">Only 5 accounts control 80% of all credit inflows. High revenue dependency risk!</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 13: BUSINESS INSIGHTS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-12">
  <span class="section-badge">Section 8</span>
  <h2 class="slide-title">Business Insights</h2>
  <p class="slide-subtitle">Key findings from the financial analysis</p>

  <div class="insight-grid">
    <div class="insight-card">
      <div class="insight-icon">✅</div>
      <div class="insight-text">
        <h4>Company is Profitable</h4>
        <p>Net profit of ₹67.77L with 10% margin. Consistently profitable after April.</p>
      </div>
    </div>
    <div class="insight-card">
      <div class="insight-icon">📦</div>
      <div class="insight-text">
        <h4>Purchases Dominate (49%)</h4>
        <p>Nearly half of all expenses. Better supplier rates could boost margins significantly.</p>
      </div>
    </div>
    <div class="insight-card">
      <div class="insight-icon">👥</div>
      <div class="insight-text">
        <h4>Reasonable Employee Costs</h4>
        <p>₹48.05L (7.8% of expenses) — within healthy range for the business size.</p>
      </div>
    </div>
    <div class="insight-card">
      <div class="insight-icon">🏭</div>
      <div class="insight-text">
        <h4>Asset-Heavy Structure</h4>
        <p>₹24.81 Cr in net assets. Typical for manufacturing, but means high depreciation costs.</p>
      </div>
    </div>
    <div class="insight-card">
      <div class="insight-icon">💵</div>
      <div class="insight-text">
        <h4>Strong Cash Position</h4>
        <p>₹4.51 Cr in cash & bank — healthy reserve for meeting short-term obligations.</p>
      </div>
    </div>
    <div class="insight-card">
      <div class="insight-icon">⚠️</div>
      <div class="insight-text">
        <h4>Revenue Concentration Risk</h4>
        <p>Only 5 accounts = 80% of credit. Losing even one could severely impact income.</p>
      </div>
    </div>
    <div class="insight-card" style="grid-column: span 2;">
      <div class="insight-icon">📈</div>
      <div class="insight-text">
        <h4>Strong Growth Trajectory</h4>
        <p>Revenue grew 40% from April to August. The company recovered from an initial loss month and has been building cumulative profit steadily. If this trend continues, annual revenue could exceed ₹16 Cr.</p>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 14: OVERALL HEALTH -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-13">
  <span class="section-badge">Section 9</span>
  <h2 class="slide-title">Overall Financial Health</h2>
  <p class="slide-subtitle">Comprehensive assessment of strengths and risks</p>

  <div style="text-align: center; margin-bottom: 30px;">
    <div style="display: inline-block; padding: 12px 40px; background: var(--green-bg); border: 2px solid var(--green); border-radius: 16px;">
      <span style="font-size: 1.5em; font-weight: 800; color: var(--green);">🟢 GOOD</span>
    </div>
  </div>

  <div class="card-grid card-grid-2" style="max-width: 1000px;">
    <div class="card" style="border-top: 3px solid var(--green);">
      <h3 style="color: var(--green); margin-bottom: 16px; font-size: 1.1em;">✅ Key Strengths</h3>
      <div class="status-row"><span class="status-dot good"></span> Profitable — 10% margin, 4/5 months profitable</div>
      <div class="status-row"><span class="status-dot good"></span> Revenue growing — +40% over 5 months</div>
      <div class="status-row"><span class="status-dot good"></span> Strong cash position — ₹4.51 Cr available</div>
      <div class="status-row"><span class="status-dot good"></span> Solid asset base — ₹24.81 Cr</div>
      <div class="status-row" style="border: none;"><span class="status-dot good"></span> Regular tax compliance — GST, TDS in order</div>
    </div>
    <div class="card" style="border-top: 3px solid var(--amber);">
      <h3 style="color: var(--amber); margin-bottom: 16px; font-size: 1.1em;">⚠️ Key Risks</h3>
      <div class="status-row"><span class="status-dot warn"></span> Thin margin (10%) — vulnerable to cost rises</div>
      <div class="status-row"><span class="status-dot warn"></span> Revenue concentration — 5 accounts = 80%</div>
      <div class="status-row"><span class="status-dot warn"></span> High purchase costs — 49% of expenses</div>
      <div class="status-row"><span class="status-dot warn"></span> Asset-heavy — high depreciation overhead</div>
      <div class="status-row" style="border: none;"><span class="status-dot warn"></span> No visible long-term debt — may limit growth</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 15: RECOMMENDATIONS -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide" id="slide-14">
  <span class="section-badge">Section 10</span>
  <h2 class="slide-title">Business Recommendations</h2>
  <p class="slide-subtitle">Actionable steps for the management team</p>

  <div style="max-width: 1000px; width: 100%;">
    <div class="rec-card">
      <div class="rec-num">1</div>
      <div class="rec-content">
        <h4>🔄 Negotiate Better Purchase Rates</h4>
        <p>Purchases are the largest expense at ₹3.02 Cr. A 2–3% reduction through bulk deals or alternate suppliers adds ₹6–9L+ to profit.</p>
      </div>
    </div>
    <div class="rec-card">
      <div class="rec-num">2</div>
      <div class="rec-content">
        <h4>👥 Review Workforce Efficiency</h4>
        <p>Conduct a productivity audit. Ensure headcount aligns with output needs. Consider automation for repetitive tasks.</p>
      </div>
    </div>
    <div class="rec-card">
      <div class="rec-num">3</div>
      <div class="rec-content">
        <h4>🎯 Diversify Revenue Sources</h4>
        <p>Revenue is concentrated in few accounts. Explore new markets, product lines, or channels to reduce dependency risk.</p>
      </div>
    </div>
    <div class="rec-card">
      <div class="rec-num">4</div>
      <div class="rec-content">
        <h4>💰 Build Cash Reserves</h4>
        <p>Maintain 2–3 months of operating expenses (~₹3.5 Cr) as a safety buffer against disruptions.</p>
      </div>
    </div>
    <div class="rec-card">
      <div class="rec-num">5</div>
      <div class="rec-content">
        <h4>📊 Monthly Financial Reviews</h4>
        <p>Use this analysis monthly to spot trends early. Set up KPI dashboards (Power BI) for real-time monitoring.</p>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- SLIDE 16: THANK YOU -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="slide end-slide" id="slide-15">
  <div class="cover-logo" style="font-size: 5em;">🎯</div>
  <h2 class="cover-title" style="font-size: 3em;">Thank You</h2>
  <p class="cover-sub" style="max-width: 600px;">
    This report was generated from the Trial Balance data of Labhyansh Solution.
    No financial values were altered during analysis.
  </p>
  <div style="margin-top: 30px; padding: 20px 40px; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 16px; text-align: center;">
    <p style="color: var(--text-muted); font-size: 0.9em; margin-bottom: 8px;">Prepared by</p>
    <p style="font-size: 1.2em; font-weight: 700; color: var(--accent-glow);">Aviral Dubey</p>
    <p style="color: var(--text-muted); font-size: 0.85em; margin-top: 8px;">FY 2024-25 | Q1 & Q2 Analysis</p>
  </div>
</div>


<!-- ═══════════════════════════════════════════════════════════ -->
<!-- NAVIGATION BAR -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div class="nav-bar">
  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">← Previous</button>
  <span class="slide-counter" id="slideCounter">1 / 16</span>
  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Next →</button>
</div>

<div class="kb-hint">
  Use <kbd>←</kbd> <kbd>→</kbd> arrow keys or click buttons to navigate
</div>

<script>
  const totalSlides = 16;
  let currentSlide = 0;

  function changeSlide(dir) {{
    const next = currentSlide + dir;
    if (next < 0 || next >= totalSlides) return;

    const current = document.getElementById('slide-' + currentSlide);
    const target = document.getElementById('slide-' + next);

    current.classList.remove('active');
    current.classList.add(dir > 0 ? 'exit' : '');

    setTimeout(() => {{
      current.classList.remove('exit');
      current.style.transform = dir > 0 ? 'translateX(60px)' : 'translateX(-60px)';
    }}, 500);

    target.style.transform = dir > 0 ? 'translateX(60px)' : 'translateX(-60px)';
    target.offsetHeight; // force reflow
    target.classList.add('active');

    currentSlide = next;
    updateNav();
  }}

  function updateNav() {{
    document.getElementById('slideCounter').textContent = (currentSlide + 1) + ' / ' + totalSlides;
    document.getElementById('prevBtn').disabled = currentSlide === 0;
    document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
    document.getElementById('progressBar').style.width = ((currentSlide + 1) / totalSlides * 100) + '%';
  }}

  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight' || e.key === ' ') changeSlide(1);
    if (e.key === 'ArrowLeft') changeSlide(-1);
  }});

  updateNav();
</script>

</body>
</html>"""

# Write the presentation
with open(PRESENTATION_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

file_size = os.path.getsize(PRESENTATION_FILE) / (1024 * 1024)
print(f"\n  ✅ Presentation saved: {PRESENTATION_FILE}")
print(f"  📦 File size: {file_size:.1f} MB (self-contained, no external dependencies)")
print(f"  📊 Slides: 16 slides")
print(f"  🖼️ Charts embedded: {len(chart_files)} images")
print(f"\n  Open in any browser to view!")
