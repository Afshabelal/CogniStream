
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataset
file_path = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
df = pd.read_csv(file_path)

# Output folder
output_dir = BASE_DIR / "data" / "output"
output_dir.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Flow State Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="flow_state")
plt.title("Developer Flow State Distribution")
plt.xlabel("Flow State")
plt.ylabel("Number of Sessions")
plt.tight_layout()
plt.savefig(output_dir / "flow_state_distribution.png")
plt.close()

# 2. Productivity by Developer
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="developer_id", y="productivity_score")
plt.title("Average Productivity by Developer")
plt.xlabel("Developer")
plt.ylabel("Productivity Score")
plt.tight_layout()
plt.savefig(output_dir / "productivity_by_developer.png")
plt.close()

# 3. Focus vs Productivity
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="focus_score",
    y="productivity_score",
    hue="flow_state"
)
plt.title("Focus Score vs Productivity")
plt.xlabel("Focus Score")
plt.ylabel("Productivity Score")
plt.tight_layout()
plt.savefig(output_dir / "focus_vs_productivity.png")
plt.close()

# 4. Correlation Heatmap
plt.figure(figsize=(9, 6))
numeric_df = df.select_dtypes(include="number")
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Developer Activity Correlation Heatmap")
plt.tight_layout()
plt.savefig(output_dir / "correlation_heatmap.png")
plt.close()

print("All Visualizations Generated Successfully!")

print("\nSaved Charts:")
for file in output_dir.glob("*.png"):
    print(file.name)
