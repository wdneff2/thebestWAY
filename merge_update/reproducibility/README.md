# Reproducibility Guide

## Overview

This project integrates multiple datasets from the World Bank World Development Indicators (WDI) and OECD Data Portal to analyze the relationship between economic wealth and healthcare access. The final dataset includes variables such as GDP per capita, government health expenditure, health spending, and doctors per capita.

---

## Data Sources

* World Bank WDI (GDP per capita, health expenditure)
* OECD Data Portal (health spending, doctors per capita)

---

## Scope and Constraints

* Analysis limited to **European Union (EU) countries**
* Final dataset includes **25 countries**
* Due to limited overlap across datasets, only **4 years of data** were available (instead of the originally planned 10 years)
* Only overlapping countries and years across all datasets were retained

---

## Data Cleaning (OpenRefine)

Data cleaning was performed in OpenRefine using the following steps:

1. **Filter to EU countries only**

   * Removed all non-EU countries and aggregate entries (e.g., “World”, “European Union”, “High income”)

2. **Standardize country names**

   * Ensured consistent naming across datasets
   * Example: “Slovak Republic” vs. “Slovakia”

3. **Remove unnecessary columns**

   * Kept only:

     * `country`
     * `year`
     * indicator value

4. **Reshape data (Wide → Long format)**

   * Converted year columns into a single `year` column

5. **Ensure consistency**

   * Checked for duplicates and formatting issues
   * Verified numeric data types

6. **Export cleaned datasets**

   * Saved as CSV files for integration

---

## Data Integration (Python)

Data integration was performed using Python and the pandas library.

### Steps:

1. Load cleaned datasets:

```python
import pandas as pd

gdp = pd.read_csv("gdp_per_capita.csv")
health_exp = pd.read_csv("health_expenditure.csv")
health_spend = pd.read_csv("health_spending.csv")
doctors = pd.read_csv("doctors_per_capita.csv")
```

2. Merge datasets using shared identifiers:

```python
df = gdp.merge(health_exp, on=["country", "year"], how="inner")
df = df.merge(health_spend, on=["country", "year"], how="inner")
df = df.merge(doctors, on=["country", "year"], how="inner")
```

* Used **inner join** to keep only overlapping observations across all datasets

3. Save final dataset:

```python
df.to_csv("merged_dataset.csv", index=False)
```

---

## Final Dataset

* **Rows:** 98
* **Columns:** 6
* **Countries:** 25
* **Years:** 4
* **Missing Values:** 0

The dataset is fully clean, consistent, and ready for analysis.

---

## Analysis

### Scatter Plot

A scatterplot was created to examine the relationship between GDP per capita and doctors per capita.

```python
import matplotlib.pyplot as plt

plt.scatter(df["gdp_per_capita"], df["doctors_per_capita"])
plt.xlabel("GDP per Capita")
plt.ylabel("Doctors per Capita")
plt.title("Wealth vs Healthcare Access")
plt.show()
```

### Interpretation

The scatterplot shows a positive relationship between GDP per capita and doctors per capita. Countries with lower GDP per capita tend to have fewer doctors, while wealthier countries generally have more doctors available. This suggests that economic wealth is associated with better healthcare access. However, the relationship is not perfectly linear, indicating that additional factors may influence healthcare outcomes.

---

## Correlation Analysis

```python
df[["gdp_per_capita", "doctors_per_capita"]].corr()
```

### Result:

* Correlation = **0.77579**

### Interpretation:

This indicates a strong positive relationship between GDP per capita and doctors per capita. As economic wealth increases, the number of doctors per capita also tends to increase, supporting the pattern observed in the scatterplot.

---

## Reproducibility

This project is fully reproducible because:

* All raw datasets are provided
* Data cleaning steps are documented (OpenRefine)
* Integration and analysis are performed using Python code
* The final dataset can be recreated by following the steps above

---
