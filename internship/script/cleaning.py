import os
import pandas as pd

# -----------------------------
# 1. File path setup
# -----------------------------
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "Dataset.xlsx")

print("Loading dataset from:", file_path)

# -----------------------------
# 2. Load dataset safely
# -----------------------------
try:
    df = pd.read_excel(file_path)
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("ERROR: Dataset not found. Check file path.")
    exit()

# -----------------------------
# 3. Basic exploration
# -----------------------------
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# -----------------------------
# 4. CLEANING (FINAL FIX)
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values safely
for col in df.columns:
    
    if df[col].dtype in ["int64", "float64"]:
        # numeric columns → mean
        df[col] = df[col].fillna(df[col].mean())
    
    else:
        # text columns → "Unknown"
        df[col] = df[col].fillna("Unknown")
# -----------------------------
# 5. After cleaning check
# -----------------------------
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset preview:")
print(df.head())

# -----------------------------
# 6. Save cleaned dataset
# -----------------------------
output_path = os.path.join(base_path, "data", "Cleaned_Dataset.xlsx")
df.to_excel(output_path, index=False)

print("\nCleaned dataset saved at:", output_path)
print("SUCCESS ✔ Data cleaning completed")