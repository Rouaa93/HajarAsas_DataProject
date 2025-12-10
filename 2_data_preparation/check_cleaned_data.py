import pandas as pd
import os

# Adjusted path for scripts folder
processed_folder = "./../data/processed/"
files = ["capital_cleaned.csv", "operating-expenses_cleaned.csv"]

for file_name in files:
    file_path = os.path.join(processed_folder, file_name)
    print(f"\nChecking file: {file_name}")
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_name}")
        continue
    
    df = pd.read_csv(file_path)
    
    # 1. Check for completely empty rows
    empty_rows = df.isnull().all(axis=1).sum()
    print(f"Number of completely empty rows: {empty_rows}")
    
    # 2. Check for leading/trailing spaces in string cells
    spaces = df.applymap(lambda x: isinstance(x, str) and (x != x.strip())).sum().sum()
    print(f"Number of cells with extra spaces: {spaces}")
    
    # 3. Column data types
    print("Column types:")
    print(df.dtypes)
    
    print("-" * 40)
