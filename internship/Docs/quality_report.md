# Data Quality Assessment Report

## Dataset Overview

* Dataset Name: Sales Dataset
* Total Rows: 1000
* Total Columns: 12

## Data Familiarization

The dataset contains sales transaction information including customer details, product information, quantity purchased, unit price, and total sales amount.

## Data Quality Issues Identified

### Missing Values

| Column | Missing Values |
| ------ | -------------- |
| Age    | 20             |
| City   | 13             |

### Duplicate Records

* Duplicate Rows Found: 0

## Data Cleaning Actions Performed

1. Filled missing values in the Age column using the mean value.
2. Filled missing values in the City column using the mode value.
3. Converted Order_Date to datetime format.
4. Created Order_Year column from Order_Date.
5. Created Order_Month column from Order_Date.

## Final Outcome

* Missing Values Remaining: 0
* Duplicate Records Remaining: 0
* Dataset is clean and ready for analysis.
