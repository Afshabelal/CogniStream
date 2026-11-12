
from pathlib import Path
import pandas as pd

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Read raw dataset
input_file = BASE_DIR / "data" / "raw" / "cognistream_developer_data.csv"

df = pd.read_csv(input_file)

print("Before Cleaning:")
print("Rows:", len(df))
print("Duplicates:", df.duplicated().sum())
print("Missing Values:", df.isnull().sum().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Save cleaned dataset
output_dir = BASE_DIR / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "cognistream_cleaned_data.csv"

df.to_csv(output_file, index=False)

print("\nAfter Cleaning:")
print("Rows:", len(df))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

print("\nCleaned Dataset Saved Successfully!")
print(output_file)
