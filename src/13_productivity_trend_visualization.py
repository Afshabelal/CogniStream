
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "productivity_trend_analysis.csv"
OUTPUT_DIR = BASE_DIR / "data" / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Starting Productivity Trend Visualization...")

# Load productivity trend data
df = pd.read_csv(INPUT_FILE)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# 1. Daily Productivity Trend
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["average_productivity"], marker="o")
plt.title("Daily Average Productivity Trend")
plt.xlabel("Date")
plt.ylabel("Average Productivity")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "daily_productivity_trend.png")
plt.close()

# 2. Daily Focus Trend
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["average_focus"], marker="o")
plt.title("Daily Average Focus Trend")
plt.xlabel("Date")
plt.ylabel("Average Focus")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "daily_focus_trend.png")
plt.close()

# 3. Daily Workload Trend
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["average_workload"], marker="o")
plt.title("Daily Average Workload Trend")
plt.xlabel("Date")
plt.ylabel("Average Workload")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "daily_workload_trend.png")
plt.close()

print("\nAll productivity trend visualizations generated successfully!")
print("Total dates visualized:", len(df))
print("Charts saved in:", OUTPUT_DIR)
