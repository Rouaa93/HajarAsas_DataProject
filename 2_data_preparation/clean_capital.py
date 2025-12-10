import pandas as pd
import os

# ---------- Paths and File Names ----------
RAW_PATH = "../1_datasets/raw/capital.csv"
PROCESSED_PATH = "../1_datasets/processed/capital_cleaned_final_V2.csv" # New name for the output file

# ---------- Create processed folder if it doesn't exist ----------
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)

# ---------- Read the raw file (FAIL-SAFE READ) ----------
try:
    # Read the file assuming NO headers, we will rename columns manually.
    df = pd.read_csv(
        RAW_PATH, 
        encoding='utf-8',
        header=None, # Treat ALL lines as data for now
        skiprows=1 # Skip the first line (which contains the actual headers) if it's the only issue
    )
except FileNotFoundError:
    print(f"Error: Capital file not found at {RAW_PATH}.")
    exit()

# ***************************************************************
# FAIL-SAFE COLUMN RENAMING
# We manually assign the column names based on your clean data structure.
df.columns = ['Item Arabic', 'Item English', 'Category', 'Price', 'Notes', 'Extra_Col_A', 'Extra_Col_B', 'Extra_Col_C', 'Extra_Col_D', 'Extra_Col_E', 'Extra_Col_F', 'Extra_Col_G', 'Extra_Col_H', 'Extra_Col_I', 'Extra_Col_J', 'Extra_Col_K']
# Now we rely on the clean structure you created manually.

# Drop any excess columns from the old complex file structure that might remain
df = df.iloc[:, :5] # Keep only the first 5 columns: Item Arabic, Item English, Category, Price, Notes
df.columns = ['Item Arabic', 'Item English', 'Category', 'Price', 'Notes']

print("\n--- Columns after manual renaming (Expected Clean Structure) ---")
print(df.columns.tolist())
print("-------------------------------------------------------------\n")
# ***************************************************************


# ---------- DATA CLEANING V1: INITIAL CLEANUP & WHITESPACE REMOVAL ----------

# 1. Strip whitespace from string values in data cells
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# 2. Drop completely empty rows
df = df.dropna(how="all")


# ---------- DATA CLEANING V2: TYPE CONVERSION & MISSING VALUE HANDLING ----------

# 3. Convert 'Price' column to numeric (float64) - THIS IS FINALLY SAFE!
df['Price'] = pd.to_numeric(
    df['Price'].astype(str)
               .str.replace(r'[$,]', '', regex=True)
               .str.replace('NULL', '', regex=False),
    errors='coerce'
).astype('float64')

# 4. Fill Missing Values in text columns
df['Notes'] = df['Notes'].fillna('N/A')
df['Category'] = df['Category'].fillna('Uncategorized')

# 5. Unify Category names (Standardization) - SAME MAPPING AS BEFORE
category_mapping = {
    'guarantee': 'Financial/Admin',
    'Financial': 'Financial/Admin',
    'Service': 'Labor & Services',
    'Rent/Service': 'Rent',
    'General': 'Miscellaneous',
    'GENERAL': 'Miscellaneous',
    'Tools': 'Parts & Supplies',
    'Items': 'Parts & Supplies',
    'Constrction': 'Construction', 
}
df['Category'] = df['Category'].replace(category_mapping)


# ---------- SAVE CLEANED DATA ----------
df.to_csv(PROCESSED_PATH, index=False)

print("\n--- Capital Data Cleaned and Finalized Successfully ---")
print(f"Cleaned capital data saved to: {PROCESSED_PATH}")
print("\nFinal Data Information:")
print(df.info())