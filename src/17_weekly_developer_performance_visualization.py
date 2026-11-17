
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR / "data" / "processed"
    / "weekly_developer_performance.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Starting Weekly Developer Performance Visualization...")

# Load weekly performance data
df = pd.read_csv(DATA_FILE)
df["week_start"] = pd.to_datetime(df["week_start"])

developers = sorted(df["developer_id"].unique())
metrics = [
    ("average_productivity", "Weekly Developer Productivity",
     "Average Productivity", "weekly_developer_productivity.png"),
    ("average_focus", "Weekly Developer Focus",
     "Average Focus Score", "weekly_developer_focus.png"),
    ("average_workload", "Weekly Developer Workload",
     "Average Workload Score", "weekly_developer_workload.png")
]

# Generate comparison charts
for column, title, ylabel, filename in metrics:
    plt.figure(figsize=(11, 6))

    for developer in developers:
        developer_data = df[df["developer_id"] == developer]

        plt.plot(
            developer_data["week_start"],
            developer_data[column],
            marker="o",
            label=developer
        )

    plt.title(title)
    plt.xlabel("Week Starting")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.legend(title="Developer")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / filename)
    plt.close()

print("All weekly developer comparison charts generated successfully!")
print("Developers compared:", len(developers))
print("Weeks analyzed:", df["week_start"].nunique())
print("Charts saved in:", OUTPUT_DIR)
