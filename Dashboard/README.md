# 🧠 CogniStream
### Developer Flow-State & Cognitive Load Analytics

## 📌 Project Overview
CogniStream is a data analytics project that explores developer productivity, focus, workload, interruptions, task switching, and flow states.

The project uses a synthetic dataset of 500 developer work sessions to identify patterns and understand how different work factors are associated with productivity.

## 🎯 Project Objectives
- Analyze developer productivity.
- Understand the relationship between focus and productivity.
- Study workload and task-switching patterns.
- Explore developer flow-state distribution.
- Build an interactive Streamlit dashboard.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## 📂 Project Structure
```text
CogniStream/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── src/
│   ├── 01_generate_data.py
│   ├── 02_inspect_data.py
│   ├── 03_clean_data.py
│   ├── 04_data_analysis.py
│   └── 05_visualization.py
│
├── Dashboard/
│   └── app.py
│
├── notebooks/
├── reports/
├── documentation/
├── presentation/
├── README.md
└── .gitignore
```

## 📊 Dataset Information
- Total Records: 500
- Data Type: Synthetic developer activity data
- Includes productivity, focus, workload, interruptions, task switches, and flow-state information.

**Note:** This is synthetic data created for educational and analytical purposes. It does not represent actual measurements of real developers.

## 📈 Key Analysis Findings
Correlation with productivity score:
- Focus Score: +0.73
- Workload Score: +0.36
- Interruption Count: -0.41
- Task Switches: -0.60

These values indicate associations, not proof of causation.

## 📉 Visualizations
The project includes:
- Correlation Heatmap
- Flow State Distribution
- Focus vs Productivity
- Productivity by Developer

## 🚀 Dashboard Features
- Interactive developer filter
- Date range filter
- Key Performance Indicators (KPIs)
- Productivity analysis
- Focus vs Productivity chart
- Flow State Distribution
- Workload Analysis
- Developer data table
- Filtered CSV download

## ▶️ How to Run the Project

### 1. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn plotly streamlit openpyxl jupyter
```

### 2. Run the Dashboard
From the main CogniStream project folder, execute:

```bash
.venv\Scripts\python.exe -m streamlit run Dashboard\app.py
```

### 3. Open in Browser
```text
http://localhost:8501
```

## 💡 Conclusion
CogniStream demonstrates how data analytics and visualization can help explore developer productivity and cognitive workload patterns.

The interactive dashboard makes it easier to examine developer sessions, compare metrics, and download filtered data.

## 👩‍💻 Project Domain
Data Analytics

**Project:** CogniStream – Developer Flow-State & Cognitive Load Analytics