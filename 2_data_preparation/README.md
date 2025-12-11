# ⚙️ 2. Data Preparation and Cleaning Phase

This directory contains the essential Python scripts responsible for transforming the raw financial logs into clean, structured, and unified datasets ready for analysis.

---

## 🚀 Objective and Methodology

The primary goal of this phase was to achieve **data integrity** by addressing three critical issues: missing values, inconsistent naming conventions, and incorrect data types.

The process followed these steps:

1. **Loading:** Reading the raw data from `1_datasets/raw`.
2. **Cleaning:** Applying transformations to handle inconsistencies.
3. **Unification:** Standardizing all categorical fields to a predefined list.
4. **Saving:** Exporting the clean files to `1_datasets/processed`.

---

## 🛠️ Key Cleaning Scripts

The cleaning process was split into two dedicated scripts to handle the distinct nature of Operational Expenses (Opex) and Capital Assets (CapEx):

### 1. `clean_operating_expenses.py`

This script focused on refining the Opex data to ensure accurate aggregation:

* **Handling Missing Values:** Checked for and confirmed **no missing values** in the critical 'Price' column.
* **Data Type Conversion:** Ensured the 'Date' field was correctly converted to a `Datetime` object for time-series analysis.
* **Standardization:** Applied a lookup or mapping function to unify all spelling and naming variations within the 'Category' field (e.g., 'Ajar' to 'Rent').

### 2. `clean_capital.py`

This script addressed the more complex issues associated with long-term assets:

* **Critical Missing Data:** Identified the assets where the **'Price' column was null**. These records were kept in the file but flagged, as their omission would distort the total CapEx figure.
* **Renaming:** Renamed complex Arabic column titles to simple, English, machine-readable names for ease of coding.
* **Categorization:** Grouped asset items (e.g., 'Cement Mixer' or 'Water Pump') into standardized high-level categories (e.g., 'Machinery' or 'Equipment').

---

## ✅ Output and Next Steps

The successful execution of these two scripts generated the clean files found in the `1_datasets/processed` directory:

1. `operating-expenses_cleaned_final.csv`
2. `capital_cleaned_final_V2.csv`

These files are the sole input for the next stage: **3. Data Analysis.**
