
from pathlib import Path
import pandas as pd

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load raw dataset
file_path = BASE_DIR / "data" / "raw" / "cognistream_developer_data.csv"

df = pd.read_csv(file_path)

print("\n========== DATASET INFORMATION ==========")

print("\n1. Dataset Shape:")
print(df.shape)

print("\n2. Column Names:")
print(df.columns.tolist())

print("\n3. Dataset Information:")
df.info()

print("\n4. Missing Values:")
print(df.isnull().sum())

print("\n5. Duplicate Records:")
print(df.duplicated().sum())

print("\n6. Statistical Summary:")
print(df.describe())

print("\n7. Flow State Distribution:")
print(df["flow_state"].value_counts())

print("\n========== INSPECTION COMPLETED ==========")
