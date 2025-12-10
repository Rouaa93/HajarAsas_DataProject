import pandas as pd
import os

# --- PATHS AND FILE NAMES ---
RAW_PATH = "../1_datasets/raw/operating-expenses.csv"
PROCESSED_PATH = "../1_datasets/processed/operating-expenses_cleaned_final.csv"

# --- CREATE PROCESSED FOLDER IF IT DOESN'T EXIST ---
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)

# --- READ THE RAW FILE ---
try:
    # Read the CSV with UTF-8 for Arabic characters and skip bad lines
    df = pd.read_csv(
        RAW_PATH, 
        encoding='utf-8', 
        on_bad_lines='skip' 
    )
except FileNotFoundError:
    print(f"Error: The raw data file was not found at {RAW_PATH}.")
    print("Please check the path and file name.")
    exit()

# --- DATA CLEANING V1: INITIAL CLEANUP ---

# Remove leading and trailing whitespace from all string/object columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# Drop completely empty rows
df = df.dropna(how="all")

# --- DATA CLEANING V2: DATA TYPE CONVERSION & MISSING VALUE SETUP ---

# 1. Clean and convert 'Price / Amount' to numeric (float64)
# Removes non-numeric symbols (like currency signs if any) and converts to float
df['Price / Amount'] = pd.to_numeric(
    df['Price / Amount'].astype(str).str.replace(r'[$,]', '', regex=True),
    errors='coerce'
).astype('float64')

# 2. Convert 'Quantity' to Integer (Int64 allows NaNs)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').astype('Int64')

# 3. Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 4. Fill 'NaN' values in the 'Category' column with a default string
df['Category'] = df['Category'].fillna('Uncategorized')

# --- DATA CLEANING V3: CATEGORY AND UNIT STANDARDIZATION ---

# 1. Category Standardization Mapping
category_mapping = {
    'Service/Labor': 'Labor & Services',
    'Service': 'Labor & Services',
    'Rent/Service': 'Rent',
    'Factory Rent': 'Rent',
    'Guarantee': 'Financial/Admin',
    'Financial': 'Financial/Admin',
    'Parts': 'Parts & Supplies',
    'Oil/Supplies': 'Parts & Supplies',
    'Parts/Supplies': 'Parts & Supplies',
    'Supplies': 'Parts & Supplies',
    'Tools': 'Parts & Supplies',
    'Utility': 'Utilities/Fuel',
    'Gas/Utility': 'Utilities/Fuel',
    'Fuel': 'Utilities/Fuel',
    'Food': 'Food & Meals',
    'Miscellaneous Expense': 'Miscellaneous',
    'Expense': 'Miscellaneous'
}

df['Category'] = df['Category'].replace(category_mapping)

# 2. Unit and Notes Missing Value Handling
df['Unit'] = df['Unit'].fillna('N/A')
df['Notes'] = df['Notes'].fillna('N/A')


# --- SAVE CLEANED DATA ---
df.to_csv(PROCESSED_PATH, index=False)

print("\n--- Data Cleaning Complete ---")
print(f"Cleaned data successfully saved to: {PROCESSED_PATH}")
print("\nFinal Data Information:")
print(df.info())
print("\nTop 5 Final Categories:")
print(df['Category'].value_counts().head())