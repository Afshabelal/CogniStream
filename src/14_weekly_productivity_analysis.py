
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "productivity_trend_analysis.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "weekly_productivity_analysis.csv"

print("Starting Weekly Productivity Analysis...")

# Load daily productivity data
df = pd.read_csv(INPUT_FILE)
df["date"] = pd.to_datetime(df["date"])

# Create weekly groups (Monday to Sunday)
df["week_start"] = (
    df["date"] - pd.to_timedelta(df["date"].dt.weekday, unit="D")
)

# Calculate weekly summary
weekly_summary = (
    df.groupby("week_start")
    .agg(
        total_sessions=("total_sessions", "sum"),
        average_productivity=("average_productivity", "mean"),
        average_focus=("average_focus", "mean"),
        average_workload=("average_workload", "mean"),
        days_recorded=("date", "count"),
    )
    .reset_index()
)

# Round average values
columns_to_round = [
    "average_productivity",
    "average_focus",
    "average_workload",
]

weekly_summary[columns_to_round] = weekly_summary[columns_to_round].round(2)

# Save weekly report
weekly_summary.to_csv(OUTPUT_FILE, index=False)

print("\nWeekly Productivity Analysis completed!")
print("Total weeks analyzed:", len(weekly_summary))
print("\nWeekly Summary:")
print(weekly_summary.to_string(index=False))
print("\nReport saved at:", OUTPUT_FILE)
