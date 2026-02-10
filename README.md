# Sales Insight & Alert System – SkyGeni Case Study

## Overview

This project analyzes sales performance data for a B2B SaaS company to understand why win rate has declined despite a healthy pipeline.  
Based on the analysis, a lightweight **Sales Insight & Alert System** is designed to help sales leadership proactively identify risks, understand root causes, and protect revenue.

The focus of this project is **decision support**, not Kaggle-style model accuracy.

---

## Business Problem

The Chief Revenue Officer (CRO) observed:
- A decline in win rate over recent quarters
- Healthy-looking pipeline volume
- Lack of clarity on what is going wrong and where to focus

The objective of this project is to:
- Diagnose the root cause of win rate decline
- Quantify revenue risk
- Design a data-driven system that supports proactive sales decisions

---

## Approach

The project follows a structured, business-first analytics workflow.

### 1. Data Understanding
- Validate dataset structure, coverage, and quality
- Check date ranges, deal sizes, and sales cycle realism
- Ensure data is suitable before drawing conclusions

Notebook: `data_understanding.ipynb`

---

### 2. Exploratory Data Analysis (EDA)
EDA focuses on answering **what is happening and why**, not just visualization.

Key analyses include:
- Overall and quarterly win rate trends
- Pipeline volume vs conversion efficiency
- Funnel leakage by deal stage
- Sales cycle comparison for won vs lost deals
- Win rate driver analysis by lead source, industry, and sales rep

Notebook: `eda.ipynb`

---

### 3. Decision Engines

Based on EDA insights, three decision engines are implemented.

#### Option A – Deal Risk Scoring
Identifies deals at higher risk of being lost using:
- Deal stage
- Deal age
- Historical win rates

#### Option B – Win Rate Driver Analysis
Identifies factors that improve or hurt win rate by comparing:
- Segment-level win rates
- Against the overall baseline win rate

#### Option C – Revenue Forecasting
Calculates **expected (risk-adjusted) revenue** using:
- Deal amount
- Historical stage-level win probabilities

This avoids overestimating revenue by assuming all deals will close.

---

### 4. Insight & Alert Layer

For this prototype:
- Insights and alerts are surfaced via **console output**
- This validates decision logic and prioritization

In a production SkyGeni system, these outputs would feed:
- Dashboards
- Email or Slack alerts
- APIs for downstream consumption

---

## How to Run the Project

### Prerequisites
- Python 3.9+
- macOS / Linux / Windows

---

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Notebooks (Recommended Order)
```bash
data_understanding.ipynb
eda.ipynb
```

### Step 4: Run the Decision System
```bash
python main.py
```

---

## Project Structure
```bash
.
├── data/
│   └── raw/
│       └── skygeni_sales_data.csv
├── notebooks/
│   ├── data_understanding.ipynb
│   └── eda.ipynb
├── src/
│   ├── feature_engineering/
│   ├── decision_engines/
│   └── alerts/
├── main.py
├── requirements.txt
└── README.md
```

## Key Decisions & Rationale

### Why rule-based logic instead of complex ML?

- Interpretability is critical for sales leadership
- Historical conversion behavior provides strong signals
- The goal is decision support, not predictive accuracy

### Why use win rate by stage?

- Conversion probability varies across funnel stages
- A flat win rate oversimplifies sales dynamics
- Stage-level probabilities align with how CROs think

### Why expected revenue instead of pipeline value?

- Pipeline value assumes all deals close
- Expected revenue accounts for conversion risk
- This provides a more realistic forecast

### Why focus on early-stage funnel leakage?
- Poor qualification inflates pipeline volume
- Early leakage wastes sales effort
- Fixing qualification improves win rate without increasing pipeline


### Why print insights instead of building a UI?
- This project focuses on logic and reasoning
- Console output acts as a placeholder delivery layer
- In production, outputs would feed dashboards and alerts

### Assumptions & Limitations

- Historical win rates represent near-term behavior
- Analysis identifies correlation, not causation
- New segments may lack sufficient historical data
- Forecasts represent expectations, not guarantees


### Future Improvements

- ML-based deal win probability models
- Rolling-window recalibration of win rates
- Rep-level coaching recommendations
- Scenario simulations (what-if analysis)
- Real-time CRM integrations

