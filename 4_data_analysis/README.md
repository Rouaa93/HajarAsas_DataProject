# 💡 Core Financial Analysis Phase (KPIs & Final Visualizations)

This document describes the function of the final analytical notebook: **`data_analysis.ipynb`**.

---

## ⚖️ Objective: Calculating Strategic Key Performance Indicators (KPIs)

This phase moved beyond simple statistics to calculate the specific, strategic metrics required to answer the project's core business questions related to efficiency and investment balance.

### Core Metrics Calculated

1. **Opex Concentration Ratio:**
    * **Formula:** (Total of Top Category / Total Opex) * 100
    * **Result:** 31.10% (driven by the Rent category). This metric provides an immediate basis for cost control recommendations.

2. **CapEx to Opex Ratio:**
    * **Formula:** Total CapEx / Total Opex
    * **Result:** 0.01. This metric highlights the crucial imbalance between long-term investment and short-term operational costs.

3. **Monthly Spending Trend:**
    * Aggregating costs by month to plot the project's financial lifecycle (setup vs. stability).

---

## 📈 Final Visualizations and Output

The notebook produced the three primary visual assets used directly in the final management report:

| Visualization | Insight Provided | Purpose in Report |
| :--- | :--- | :--- |
| **Bar Chart: Opex by Category** | Clearly identifies the top 3 drivers of operational cost. | Focuses management on cost control priorities (e.g., Rent). |
| **Line Plot: Monthly Trend** | Maps the financial transition from high setup costs to stable operational expenses. | Provides a reliable baseline for future budgeting. |
| **Pie Chart: CapEx vs. Opex** | Visually demonstrates the stark difference in spending allocation (0.97% CapEx vs. 99.03% Opex). | Forces an executive review of the project's asset acquisition strategy. |

The numerical and visual outputs of this notebook are the sole foundation for the Strategic Recommendations documented in the `4_communication` directory.
