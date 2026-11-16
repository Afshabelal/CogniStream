
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "weekly_productivity_analysis.csv"
OUTPUT_DIR = BASE_DIR / "data" / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Starting Weekly Productivity Visualization...")

# Load weekly analysis data
df = pd.read_csv(DATA_FILE)
df["week_start"] = pd.to_datetime(df["week_start"])
df = df.sort_values("week_start")

# Chart 1: Weekly Average Productivity
plt.figure(figsize=(10, 5))
plt.plot(df["week_start"], df["average_productivity"], marker="o")
plt.title("Weekly Average Productivity")
plt.xlabel("Week Starting")
plt.ylabel("Average Productivity")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "weekly_productivity_trend.png")
plt.close()

# Chart 2: Weekly Average Focus
plt.figure(figsize=(10, 5))
plt.plot(df["week_start"], df["average_focus"], marker="o")
plt.title("Weekly Average Focus")
plt.xlabel("Week Starting")
plt.ylabel("Average Focus")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "weekly_focus_trend.png")
plt.close()

# Chart 3: Weekly Average Workload
plt.figure(figsize=(10, 5))
plt.plot(df["week_start"], df["average_workload"], marker="o")
plt.title("Weekly Average Workload")
plt.xlabel("Week Starting")
plt.ylabel("Average Workload")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "weekly_workload_trend.png")
plt.close()

print("All weekly productivity visualizations generated successfully!")
print("Total weeks visualized:", len(df))
print("Charts saved in:", OUTPUT_DIR)
