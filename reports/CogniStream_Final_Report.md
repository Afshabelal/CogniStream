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
|---|---:|
| Focus Score | 0.73 |
| Task Switches | -0.60 |
| Interruption Count | -0.41 |
| Workload Score | 0.36 |

### Key Findings

- Focus Score shows the strongest positive relationship with productivity.
- Task switching has a negative relationship with productivity.
- Interruptions are also negatively associated with productivity.
- Workload shows a moderate positive relationship.

## 7. Data Visualization

The project includes the following visualizations:

- Correlation Heatmap
- Flow-State Distribution
- Focus vs Productivity
- Productivity by Developer

## 8. Interactive Dashboard

An interactive dashboard was developed using Streamlit.

Dashboard features:

- Developer selection filter
- Date range filter
- Key performance indicators
- Interactive charts
- Developer activity records
- Filtered CSV download

## 9. Conclusion

CogniStream demonstrates how data analytics can help explore developer productivity, focus, workload and flow-state patterns.

The analysis highlights the importance of focus and the negative associations of task switching and interruptions with productivity.

These findings are exploratory and do not establish causation.

## 10. Future Scope

- Use real-world developer activity data.
- Add more advanced statistical analysis.
- Explore machine learning models.
- Improve dashboard functionality.
- Develop personalized productivity insights.

## 11. Cognitive Load Risk Analysis

### Overview
A rule-based Cognitive Load Risk Analysis feature was developed to identify developer work sessions with different levels of cognitive load. The analysis uses workload score, focus score, interruption count, and task-switching activity.

### Methodology
A Cognitive Load Risk Score was calculated using the following weighted components:

- Workload Risk: 35%
- Low Focus Risk: 30%
- Interruption Risk: 20%
- Task Switching Risk: 15%

Each session was classified into one of three categories:

- Low Risk: Score below 35
- Medium Risk: Score from 35 to below 65
- High Risk: Score of 65 or above

### Results
The analysis covered all 500 developer activity sessions.

| Risk Category | Sessions |
|---|---:|
| Low Risk | 65 |
| Medium Risk | 311 |
| High Risk | 124 |

The average Cognitive Load Risk Score was **52.70**.

### Dashboard Integration
The new analysis was integrated into the interactive Streamlit dashboard. It displays the average cognitive load risk score, number of high-risk sessions, and a bar chart showing the distribution of Low, Medium, and High Risk sessions.

### Conclusion and Limitation
This feature provides an exploratory, rule-based indicator of cognitive workload patterns. It can help highlight sessions that may need further attention. The scores are analytical estimates based on the selected rules and are not clinical or psychological diagnoses.

