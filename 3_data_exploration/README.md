# 🔎 Data Exploration Phase (Q.A. & First Look)

This document describes the function of the initial notebook: **`data_exploration.ipynb`**.

---

## 🚀 Objective: Quality Assurance and Sanity Checks

The primary purpose of this phase was to ensure the data, after cleaning (Phase 2), was structurally sound, mathematically coherent, and ready for deep analysis. This serves as a vital **Quality Assurance (QA)** step.

### Key Exploratory Actions Performed

1. **Data Structure Verification (`.info()`, `.dtypes`):**
    * Confirmed all critical columns (Price/Amount) were of the correct numeric type (`Float64`).
    * Ensured the 'Date' column was correctly parsed as a `Datetime` object for time-series aggregation.

2. **Missing Value Confirmation:**
    * Verified that the cleaning process successfully eliminated missing values in the Opex data.
    * Re-confirmed the existence and location of **critical missing price data in the CapEx file**, noting the exact number of records that need external management input.

3. **Descriptive Statistics (`.describe()`):**
    * Calculated fundamental metrics (Min, Max, Mean, Total Sum) for both Capital and Operational spending to establish the initial scale of the project's financial outlay.

---

## 🎯 Initial Insights Discovered

The exploration revealed the first signs of the financial narrative, setting the stage for the core analysis:

* **Identified Peak Spending:** Quickly determined the month with the highest total expenditure (Month 7), confirming the period of initial setup costs.
* **Identified Top 5 Opex Categories:** Created an initial sorted list of operational categories by total cost, revealing **Rent** as the immediate cost leader.

This notebook confirmed data integrity and provided the foundational statistics needed for calculating the Key Performance Indicators (KPIs) in the subsequent analysis notebook.
