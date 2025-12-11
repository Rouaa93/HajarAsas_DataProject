<p align="center">
  <img src="assets/images/HajarAsas_Logo.png" alt="HajarAsas Project Logo" width="60" height="60">
</p>
# 🧱 HajarAsas Financial Analysis Project | Block Factory Financial Health

### 📊 **Status:** Core Financial Analysis Completed

[![Project Status: Analysis Completed](https://img.shields.io/badge/Status-Analysis_Completed-blue.svg)]()
[![Analysis Tool: Python](https://img.shields.io/badge/Tool-Python_Pandas-yellow.svg)]()
[![Visualization: Matplotlib/Seaborn](https://img.shields.io/badge/Visualization-Matplotlib/Seaborn-red.svg)]()

---

## 💡 1. Executive Summary & Project Goal

This project provides a comprehensive financial analysis for the **"HajarAsas"** block factory during its crucial initial and early operational phase. The primary objective is to transform raw expenditure records (Operational and Capital) into strategic insights that facilitate data-driven decision-making for management.

### ❓ **Core Business Question:**
>
> "What expenditure priorities (Capital vs. Operating) must be adjusted or focused on to maximize operational efficiency, and which expense category presents the most significant threat to early profitability?"

---

## 📈 2. Key Insights & Critical Findings

Following the Data Preparation and Analysis phases, the following critical insights were extracted, forming the basis for the management recommendations:

| Metric | Discovered Value | Immediate Management Recommendation |
| :--- | :--- | :--- |
| **Opex Concentration** | **The Rent category consumes 31.10% of total Opex.** | **Urgent Action:** Immediately review the lease agreement and explore cost-saving or renegotiation strategies to curb the single largest operational expense. |
| **CapEx/Opex Ratio** | **Ratio is 0.01.** (For every $1.00 Opex, $0.01 was invested in CapEx) | **Strategic Review:** This low ratio necessitates an investigation into missing Capital Asset prices and verification that all essential machinery has been acquired and valued correctly. |
| **Spending Trend** | **Spending peaked in Month 7, followed by a sharp decline.** | Confirms that the initial establishment costs have passed, and the business has entered a more stable operational phase with predictable expenses. |

---

## 🗃️ 3. Project Structure & Methodology

The project adheres to a standard, professional data analysis methodology, organized into dedicated stages:

* **`1_datasets/`**: Stores raw source data and the final cleaned datasets.
* **`2_data_preparation/`**: Contains Python scripts for cleaning, unifying, and preparing data for analysis.
* **`3_data_analysis/`**: Contains Jupyter Notebooks used for statistical analysis and visualization.
* **`4_communication/`**: The final folder containing the management report and recommendations document.

### 🔗 Detailed Work Artifacts (Relative Links)

The specific code and analysis reports can be reviewed via the following links:

| Stage | Artifact | Link (Relative Path) |
| :--- | :--- | :--- |
| **Data Preparation** | `clean_operating_expenses.py` | [View Preparation Code](2_data_preparation/clean_operating_expenses.py) |
| **Data Preparation** | `clean_capital.py` | [View Capital Cleaning Code](2_data_preparation/clean_capital.py) |
| **Data Analysis** | `data_analysis.ipynb` | [View Analysis & Visualizations](3_data_analysis/data_analysis.ipynb) |
| **Communication** | `Recommendations.pdf` | [Download Final Report](4_communication/Recommendations.pdf) |

***

## 🛠️ 4. Tools and Requirements

To run this project locally and replicate the analysis:

* **Python 3.8+**
* **Jupyter Notebook** or VS Code Notebooks environment.

### Required Python Libraries

```bash
pip install pandas numpy matplotlib seaborn
