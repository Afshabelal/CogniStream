# CogniStream: Developer Flow-State & Cognitive Load Analytics

## 1. Introduction

CogniStream is a data analytics project designed to explore developer productivity, focus, workload, interruptions, task switching, and flow-state patterns.

The project uses Python-based data analysis and an interactive Streamlit dashboard to understand relationships between different work-session factors and productivity.

## 2. Project Objectives

- Analyze developer productivity patterns.
- Explore the relationship between focus and productivity.
- Understand the impact of interruptions and task switching.
- Examine workload and flow-state distribution.
- Create an interactive dashboard for data exploration.

## 3. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive charts |
| Streamlit | Dashboard development |

## 4. Dataset Description

The project uses a synthetic dataset containing 500 developer work-session records.

Important attributes include:
- Developer ID
- Date
- Coding Hours
- Interruption Count
- Meeting Hours
- Task Switches
- Break Minutes
- Focus Score
- Workload Score
- Productivity Score
- Flow State

The dataset was generated for educational and analytical purposes. It does not contain actual measurements from real developers.

## 5. Data Cleaning

The dataset was inspected and cleaned before analysis.

Cleaning results:
- Total Records: 500
- Missing Values: 0
- Duplicate Records: 0

The cleaned dataset was saved as:

`data/processed/cognistream_cleaned_data.csv`

## 6. Exploratory Data Analysis

The analysis examined the relationships between productivity and several work-session factors.

### Correlation with Productivity Score

| Variable | Correlation |
