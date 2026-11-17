
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Starting Weekly Developer Performance Analysis...")

# Load cleaned developer data
df = pd.read_csv(DATA_FILE)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create Monday-based weekly groups
df["week_start"] = (
    df["date"] - pd.to_timedelta(df["date"].dt.weekday, unit="D")
)

# Weekly developer performance
weekly_report = (
    df.groupby(["week_start", "developer_id"])
    .agg(
        total_sessions=("productivity_score", "count"),
        average_productivity=("productivity_score", "mean"),
        average_focus=("focus_score", "mean"),
        average_workload=("workload_score", "mean"),
        high_flow_sessions=("flow_state", lambda x: (x == "High Flow").sum())
    )
    .reset_index()
)

# Round average scores
score_columns = [
    "average_productivity",
    "average_focus",
    "average_workload"
]

weekly_report[score_columns] = weekly_report[score_columns].round(2)

# Sort report
weekly_report = weekly_report.sort_values(
    ["week_start", "average_productivity"],
    ascending=[True, False]
)

# Save report
output_file = OUTPUT_DIR / "weekly_developer_performance.csv"
weekly_report.to_csv(output_file, index=False)

print("\nWeekly Developer Performance Summary:")
print(weekly_report.to_string(index=False))

print("\nTotal developers:", weekly_report["developer_id"].nunique())
print("Total weekly records:", len(weekly_report))
print("\nReport saved at:", output_file)
