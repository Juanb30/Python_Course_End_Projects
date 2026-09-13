# Incremental Capstone — Healthcare Data Analysis

## Project Overview

This incremental capstone project analyzes the NSMES1988 healthcare dataset using Python, Pandas, NumPy, and Matplotlib.

The project progresses through four sessions covering data preprocessing, statistical analysis, Pandas-based exploration, and data visualization. The goal is to prepare, analyze, and visualize healthcare data to identify patterns in healthcare utilization, demographics, socioeconomic characteristics, insurance coverage, and income.

## Project Structure

```text
incremental_capstone/
│
├── data/
│   ├── NSMES1988.csv
│   ├── NSMES1988.json
│   ├── NSMES1988new.csv
│   └── NSMES1988updated.csv
│
├── notebooks/
│   ├── Capstone_Session_1.ipynb
│   ├── Capstone_Session_2.ipynb
│   ├── Capstone_Session_3.ipynb
│   └── Capstone_Session_4.ipynb
│
├── requirements/
│   ├── Capstone_Session_1.pdf
│   ├── Capstone_Session_2.pdf
│   ├── Capstone_Session_3.pdf
│   └── Capstone_Session_4.pdf
│
├── reports/
│
└── README.md

Session 1 — Data Preprocessing

Session 1 focuses on importing and inspecting the original healthcare dataset.

Key tasks include:

Importing Pandas and NumPy
Inspecting dataset dimensions and data types
Checking for missing values
Reviewing age and income ranges
Exporting the dataset to JSON
Analyzing memory usage
Optimizing appropriate data types
Removing the unnecessary saved-index column
Exporting the prepared dataset as NSMES1988new.csv
Session 2 — Statistical Analysis and Data Preparation

Session 2 builds on the cleaned dataset.

Key tasks include:

Loading NSMES1988new.csv
Converting age to actual years
Converting income to actual dollar values
Calculating descriptive statistics
Reviewing count, mean, median, standard deviation, minimum, maximum, and quartiles
Reviewing categorical and numerical data types
Exporting the transformed dataset as NSMES1988updated.csv
Session 3 — Data Analysis with Pandas

Session 3 performs detailed exploratory analysis using Pandas.

Key analyses include:

Numerical and categorical data identification
Health and Region pivot-table analysis
Healthcare utilization by gender
Healthcare utilization by marital status
Healthcare utilization by education
Healthcare utilization by employment status
Healthcare utilization by insurance status
Healthcare utilization by Medicaid status
Age and gender distribution
Health status by gender
Income distribution by gender
Regional income distribution
Age-wise income analysis
Session 4 — Data Visualization

Session 4 visualizes the findings from the previous analysis using Matplotlib.

Visualizations include:

Health status by region
Average healthcare visits by health status and region
Healthcare utilization by gender
Healthcare utilization by employment status
Healthcare utilization by insurance status
Healthcare utilization by Medicaid status
Age and gender distribution
Mean and median income by gender
Mean and median income by region
Mean and median income by age
Correlation matrix heatmap
Key Findings
Poor self-reported health is associated with greater average healthcare utilization across all regions.
Healthcare utilization varies across gender, employment, insurance, and Medicaid status.
Females make up a larger portion of the dataset than males.
Mean income is higher than median income across several demographic and regional groups, indicating a right-skewed income distribution.
Male individuals have higher mean and median income than female individuals in this dataset.
The West has the highest mean and median regional income.
The strongest positive numerical correlations are between emergency and hospital utilization and between physician and non-physician outpatient visits.
Years of schooling and income show a positive correlation.
The observed relationships are descriptive associations and do not establish causation.
Tools Used
Python
Pandas
NumPy
Matplotlib
Jupyter Notebook
Visual Studio Code
Dataset

The project uses the NSMES1988 healthcare dataset containing 4,406 observations and variables describing healthcare utilization, health status, demographics, education, employment, insurance coverage, Medicaid coverage, age, and income.

Reproducibility

Each notebook has been tested using:

Restart Kernel → Run All
