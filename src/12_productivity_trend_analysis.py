
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "productivity_trend_analysis.csv"

print("Starting Productivity Trend Analysis...")

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Calculate daily productivity trends
daily_trend = (
    df.groupby("date")
    .agg(
        total_sessions=("productivity_score", "count"),
        average_productivity=("productivity_score", "mean"),
        average_focus=("focus_score", "mean"),
        average_workload=("workload_score", "mean"),
    )
    .reset_index()
)

# Round calculated values
daily_trend[
    ["average_productivity", "average_focus", "average_workload"]
] = daily_trend[
    ["average_productivity", "average_focus", "average_workload"]
].round(2)

# Save report
daily_trend.to_csv(OUTPUT_FILE, index=False)

print("\nProductivity Trend Analysis completed!")
print("Total dates analyzed:", len(daily_trend))
print("\nDaily Productivity Summary:")
print(daily_trend.head(10).to_string(index=False))
print("\nReport saved at:", OUTPUT_FILE)
