# Food Supply Gap Analysis
## Overview
This project analyzes statewide food distribution data to identify supply-demand imbalances across food shelves.

The analysis was developed during my data analytics internship with a nonprofit organization supporting food distribution programs across Minnesota.

The objective was to help partners better understand inventory distribution patterns and identify categories experiencing shortages.

## Dashboard Preview

This dashboard provides a detailed view of food distribution cost patterns across categories and regions, helping identify areas of high spending and potential supply gaps.

The top section shows total spending by food category, highlighting which categories contribute the most to overall cost.

The bottom left chart compares cost per individual visit across a selected food shelf, food bank median, and state median, enabling benchmarking of operational efficiency.

The table on the right displays the most expensive items within each category, offering granular insight into cost drivers.

Interactive filters (year, time period, food shelf and food bank) allow users to explore trends across different timeframes and locations.

![Dashboard](images/fsa_report_screenshot.png)

## Dataset
The dataset includes food inventory and distribution records collected from 230+ food shelves across **Minnesota**.

The records include information such as:

Food category

Inventory quantities

Distribution metrics

Regional service areas

Due to data confidentiality, the dataset in this repository is a simplified sample version that preserves the structure used in the analysis.

## Data Workflow

This project follows a structured data pipeline:

1. **Data Cleaning (Python)**  
   Raw inventory data contained inconsistent naming, formatting issues, and category mismatches.  
   A Python script was developed to standardize item names, clean text fields, and apply rule-based categorization.

2. **Data Analysis (SQL)**  
   Cleaned data was queried using SQL (AWS Athena) to generate category-level metrics such as total cost, item distribution, and cost per visit.

3. **Data Visualization (Tableau)**  
   The processed data was visualized in an interactive dashboard to identify cost drivers and compare food shelf performance against benchmarks.

This pipeline reduced manual preprocessing effort and enabled reliable downstream analysis.

## Key Insights

- Certain food categories, particularly proteins, showed significant supply gaps across multiple regions.

- Rural areas often experienced lower supply levels compared with urban service areas.

- Data visualization enabled partners to benchmark performance against statewide metrics.

## Tools Used

Python

SQL (AWS Athena)

Tableau
