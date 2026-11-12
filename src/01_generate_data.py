
from pathlib import Path
import pandas as pd
import numpy as np

# Reproducible sample data
np.random.seed(42)

# Project location
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Generate 500 developer work sessions
n = 500

data = pd.DataFrame({
    "developer_id": np.random.choice(
        ["DEV001", "DEV002", "DEV003", "DEV004", "DEV005"],
        n
    ),
    "date": pd.date_range(
        start="2026-10-01",
        periods=n,
        freq="h"
    ).date,
    "coding_hours": np.round(
        np.random.uniform(1, 8, n), 2
    ),
    "interruption_count": np.random.randint(0, 16, n),
    "meeting_hours": np.round(
        np.random.uniform(0, 3, n), 2
    ),
    "task_switches": np.random.randint(0, 21, n),
    "break_minutes": np.random.randint(5, 91, n)
})

# Calculate analytical indicators
data["focus_score"] = np.clip(
    100
    - data["interruption_count"] * 3
    - data["task_switches"] * 1.5
    + np.random.normal(0, 8, n),
    0, 100
).round(2)

data["workload_score"] = np.clip(
    data["coding_hours"] * 9
    + data["meeting_hours"] * 12
    + data["interruption_count"] * 1.5
    + np.random.normal(0, 5, n),
    0, 100
).round(2)

data["productivity_score"] = np.clip(
    data["focus_score"] * 0.6
    + data["coding_hours"] * 5
    - data["task_switches"] * 0.8
    + np.random.normal(0, 5, n),
    0, 100
).round(2)

data["flow_state"] = np.where(
    (data["focus_score"] >= 70)
    & (data["interruption_count"] <= 5),
    "High Flow",
    "Normal Flow"
)

# Save dataset
file_path = OUTPUT_DIR / "cognistream_developer_data.csv"
data.to_csv(file_path, index=False)

print("CogniStream Dataset Created Successfully!")
print("Total Records:", len(data))
print("Total Columns:", len(data.columns))
print("Saved File:", file_path)
print(data.head())
