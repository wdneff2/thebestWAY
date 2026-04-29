##notes from examples - explain what each of us did in relation to the modules in class, shorter summary (not too long), where the dataset is, how did we get it and licnense, quality and cleaning like accuracy, completeness, timeliness, etc in relation to each set, be as indepth as possible whule also acknowledging needing to be short and brief, be in depth with the reproducability 

# Euros and Years: Does Money Buy a Longer Life in Europe?

## Contributors
- Autumn Rosedale (Data Cleaning Section, Initial Data Analysis, and Reproducability)
- William Neff (Data Profile, Data Quality)
- Yuri You (Data Analysis, Data Visualizations, Findings, Future Work, Challenges)

---

## Summary

### Motivation
We chose this topic because understanding the link between economic development and population health is essential not only for academic insight but also for informed travel, living, and working abroad. With personal connections to the European Union and the region’s popularity as a post-graduation destination, we wanted to move beyond surface-level impressions of European countries and examine the actual socioeconomic and health conditions across them. While GDP per capita is often used as a shorthand for a nation’s well-being, important gaps remain in understanding whether wealth alone guarantees better health outcomes—or whether factors like health spending efficiency and regional policy matter more. This project addresses those gaps by systematically analyzing whether economic indicators translate into tangible health system performance across European countries.


### Research Questions
1. How do socioeconomic indicators like GDP per capita and government health expenditure correlate to key public health outcomes like life expectancy and infant mortality across European countries?
2. Are there regional disparities in health outcomes that persist even after accounting for economic factors?

### Overview
We used publicly available secondary data from the World Bank Open Data Portal and the OECD Data Portal, merging socioeconomic indicators (GDP per capita, current health expenditure as a percentage of GDP) with health system metrics (doctors per capita). The dataset spans European countries over multiple years (2000–2024, with GDP data extending to 1960). Our approach involved data cleaning, standardization, and integration using country and year identifiers, followed by exploratory data analysis and visualization. We generated scatter plots, calculated correlation coefficients, and constructed a correlation matrix to examine relationships between economic capacity, healthcare investment, and healthcare access. All data preprocessing and analysis are seen in `data/` and `analysis/` folders.

### Key Findings
- **Wealth strongly predicts healthcare access:** GDP per capita shows a strong positive correlation (0.78) with doctors per capita, indicating that richer European countries tend to have significantly better physician availability.

- **Health spending alone does not guarantee access:** Health expenditure as a percentage of GDP correlates only moderately (0.46) with doctors per capita, with similar-spending countries showing wide variation in outcomes.

- **Wealth does not drive health investment decisions:** There is virtually no correlation (0.02) between GDP per capita and health spending as a percentage of GDP, suggesting that healthcare investment reflects policy choices rather than economic capacity.

- **High-income countries can achieve strong access with modest spending:** Luxembourg and Ireland, for example, maintain high doctors-per-capita levels despite allocating only about 5.6–5.8% of GDP to health, pointing to potential system efficiencies.

These findings suggest that while economic wealth facilitates better healthcare access, policy decisions and institutional efficiency may be equally important for achieving strong health outcomes—a nuance relevant to understanding regional disparities across Europe.

---

## Data Profile

### Dataset 1: Doctors per Capita

| Attribute | Detail |
|-----------|--------|
| **Source** | [URL or citation] |
| **License** | [e.g., CC BY 4.0, Public Domain, Proprietary] |
| **Location in repo** | `data/raw/doctors_per_capita_raw.csv/` |
| **Format** | [e.g., CSV, JSON, Parquet] |
| **Size** | 159 rows x 40 columns |
| **Date range / scope** | [e.g., 2018–2023, United States only] |

**Description:**
[What does this dataset contain? Where does it come from? Who collected it and for what purpose?]

**Key Variables:**
| Field | Type | Description |
|-------|------|-------------|
| `field_name` | string | [Description] |
| `field_name` | integer | [Description] |
| `field_name` | float | [Description] |

**Ethical & Legal Constraints:**
[Discuss licensing, privacy implications, redistribution restrictions, or any bias concerns.]

**Relevance to Research Questions:**
[How does this dataset help answer your specific research questions?]

---

### Dataset 2: GDP per Capita

| Attribute | Detail |
|-----------|--------|
| **ID** | NY.GDP.PCAP.CD |
| **Source** | Country official statistics, National Statistical Organizations and/or Central Banks; National Accounts data files, Organisation for Economic Co-operation and Development ( OECD ); Staff estimates, World Bank ( WB ) |
| **License** | CC BY-4.0 |
| **Location in repo** | `data/raw/gdp_per_capita.csv/` |
| **Format** | CSV |
| **Size** | 270 rows x 70 columns > 304 KB |
| **Raw Reference Period** | 1960-2025 |

**Description:**
This dataset contains annual estimates of GDP per capita in current US dollars, measuring the total economic output of a country divided by its population without adjusting for inflation. It covers the period from 1960 to 2024, with data sourced from official national statistics, the OECD, and World Bank staff estimates.

**Key Variables:**
| Field | Type | Description |
|-------|------|-------------|
| `Country Name` | string | Name of country |
| `Country Code` | string | Standardized way of presenting the country due from the International Organization for Standardization (ISO) under the ISO 3166 standard. This system provides recognized codes for countries, dependent territories, and special geographic areas |
| `19xx or 20xx` | int | The associated GDP per capita (meaning dividing the GDP by its population) for the respecitive coutnry during the year as presented for standarization  |

**Ethical & Legal Constraints:**
The dataset is licensed under CC BY-4.0, which allows sharing and adaptation as long as appropriate credit is given to the original sources (country official statistics, OECD, World Bank). There are no privacy concerns since the data consists of aggregated national economic indicators, not individual or household-level information. However, it should should be noted of potential bias due to differences in national statistical methodologies, gaps in data coverage across countries and years, and the fact that current-price estimates do not account for inflation or purchasing power parity, which can distort cross-country comparisons. Redistribution is permitted under the license terms, but the original source and license must be attributed.

**Relevance to Research Questions:**
This dataset is directly relevant to the first research question, as it provides the key socioeconomic indicator of GDP per capita (current US$) , which the project aims to correlate with public health outcomes like life expectancy and infant mortality across European countries. By merging this data with health metrics from the OECD datasets used and government health expenditure indicators, the team can statistically assess whether wealthier European nations tend to have better population health outcomes.

---

### Dataset 3: Health Expenditure

| Attribute | Detail |
|-----------|--------|
| **ID** | SH.XPD.CHEX.GD.ZS |
| **Source** | Global Health Expenditure Database, updated December 12th, 2025, World Health Organization ( WHO ), uri: apps.who.int/nha/database |
| **License** | CC BY-4.0 |
| **Location in repo** | `data/raw/health_expenditure_raw.csv/` |
| **Format** | CSV |
| **Size** | 270 rows x 70 columns > 139 KB |
| **Raw Reference Period** | 2000-2025 (though the recording starts at 1960, no data is received until 2000) |

**Description:**
This dataset contains annual estimates of current health expenditure expressed as a percentage of GDP for countries worldwide, covering the period 2000–2024. It includes spending on healthcare goods and services consumed each year (e.g., hospital care, medications, preventive medicine) but excludes capital investments such as buildings, machinery, or IT infrastructure. The data comes from the World Health Organization (WHO) Global Health Expenditure Database, compiled under the System of Health Accounts 2011 (SHA 2011) framework. The WHO collects these data primarily to support evidence-based health policy-making, track progress toward Universal Health Coverage (UHC) , and monitor Sustainable Development Goal (SDG) target 3.c (strengthening health financing).

**Key Variables:**
| Field | Type | Description |
|-------|------|-------------|
| `Country Name` | string | Name of country |
| `Country Code` | string | Standardized way of presenting the country due from the International Organization for Standardization (ISO) under the ISO 3166 standard. This system provides recognized codes for countries, dependent territories, and special geographic areas |
| `19xx or 20xx` | int | The respective health expenditure as a percentage of their GDP (meaning that the higher percentage, the more poriton of GDP the country spends on their country's health) for the given year |

**Ethical & Legal Constraints:**
The dataset is licensed under CC BY-4.0, permitting sharing and adaptation with proper attribution to the WHO and the Global Health Expenditure Database. There are no privacy concerns, as the data reflect aggregated national-level spending, not individual or household information. However, potential bias should be considered: estimates rely on national reporting, which may vary in accuracy, completeness, and methodological consistency across countries. Additionally, the indicator excludes capital expenditures, meaning it may underrepresent total health investment in countries building new infrastructure, and it does not capture out-of-pocket spending burdens directly. Redistribution is allowed under the license terms, but credit must be given to the original source.

**Relevance to Research Questions:**
This dataset is directly relevant to the first research question, as it provides the second key socioeconomic factor—government/current health expenditure as a percentage of GDP—that the project aims to correlate with public health outcomes like life expectancy and infant mortality across European countries. By merging this dataset with the GDP per capita data and OECD health metrics, the project can statistically assess whether European nations that allocate a larger share of their economy to current health spending tend to have better health outcomes, independent of overall wealth. For the second research question (regional disparities), this dataset helps identify whether countries with similar GDP per capita but different health spending levels (e.g., Eastern vs. Western Europe) exhibit divergent health outcomes, revealing potential policy or systemic differences.

---

### Dataset 4: Health Spending

| Attribute | Detail |
|-----------|--------|
| **Source** | [URL or citation] |
| **License** | [e.g., CC BY 4.0, Public Domain, Proprietary] |
| **Location in repo** | `data/raw/health_spending_raw.csv/` |
| **Format** | [e.g., CSV, JSON] |
| **Size** | 499 rows x 46 columns |
| **Date range / scope** | [e.g., 2020–2023] |

**Description:**
[What does this dataset contain?]

**Key Variables:**
| Field | Type | Description |
|-------|------|-------------|
| `field_name` | string | [Description] |
| `field_name` | date | [Description] |

**Ethical & Legal Constraints:**
[Discuss licensing, privacy, redistribution restrictions, or bias concerns.]

**Relevance to Research Questions:**
[How does this dataset connect to your research questions?]

---

## Data Quality

### Assessment Approach
[Briefly describe how you assessed quality — what scripts or tools did you use? Reference files in the repo, e.g., [`scripts/profile_data.py`](scripts/profile_data.py).]

### Dataset 1: [Name]
- **Completeness:** [e.g., "Field X had 4.2% missing values; field Y was fully populated."]
- **Consistency:** [e.g., "Date formats were inconsistent across rows (MM/DD/YYYY vs YYYY-MM-DD)."]
- **Accuracy:** [e.g., "Several numeric outliers detected in column Z; values above 999 appeared erroneous."]
- **Duplicates:** [e.g., "Found 312 duplicate rows based on composite key (id, date)."]
- **Other issues:** [Any additional concerns.]

### Dataset 2: [Name]
- **Completeness:** [...]
- **Consistency:** [...]
- **Accuracy:** [...]
- **Duplicates:** [...]
- **Other issues:** [...]

### Summary
[Overall takeaway — what was the general state of the data? Were quality issues minor or significant?]

---

## Data Cleaning
<!-- Target: max 1,000 words -->

> Scripts: [`scripts/clean_data.py`](scripts/clean_data.py) <!-- update as needed -->

### Operation 1: [e.g., Remove duplicate records]
- **Issue:** [What problem did this address?]
- **Action:** [What did you do, specifically?]
- **Script/Tool:** [`scripts/clean_data.py`](scripts/clean_data.py), lines XX–XX

### Operation 2: [e.g., Standardize date formats]
- **Issue:** [...]
- **Action:** [...]
- **Script/Tool:** [...]

### Operation 3: [e.g., Handle missing values]
- **Issue:** [...]
- **Action:** [...]
- **Script/Tool:** [...]

### Operation 4: [e.g., Normalize column names]
- **Issue:** [...]
- **Action:** [...]
- **Script/Tool:** [...]

<!-- Add more operations as needed -->

### OpenRefine
[If applicable, describe any operations performed in OpenRefine. The JSON recipe should be saved at `scripts/openrefine_recipe.json`.]

---

## Findings

> Analysis and visualizations were generated using:
> [`Analysis/Data_Analysis.ipynb`](Analysis/Data_Analysis.ipynb)

This analysis reflects key stages of the data lifecycle, including data integration, cleaning, and exploratory analysis (Module 2, Module 7, Module 10). By combining secondary data sources from the World Bank and OECD (Module 4), we created a unified dataset to examine relationships between socioeconomic indicators and healthcare access across EU countries. The analysis focuses on GDP per capita, health spending, and doctors per capita, using both visualizations and correlation metrics to support each finding.

---

### **Finding 1: Wealth Is Strongly Associated with Healthcare Access**
A strong positive relationship exists between GDP per capita and doctors per capita, with a correlation coefficient of approximately **0.78**. This indicates that wealthier countries tend to have greater access to healthcare resources, as measured by physician availability. The scatter plot shows a clear upward trend, where countries with higher GDP levels consistently exhibit higher numbers of doctors per capita.

This finding suggests that overall economic capacity plays a significant role in shaping healthcare access, likely due to increased funding availability, infrastructure, and institutional development in wealthier nations.

![Figure 1](Analysis/figure1.png)

*Figure 1: Relationship between GDP per capita and doctors per capita.*

### **Finding 2: Health Spending Does Not Guarantee Healthcare Access**
Health spending as a percentage of GDP shows only a **moderate correlation (0.46)** with doctors per capita. While some countries with higher health spending tend to have more doctors, the relationship is much more dispersed compared to GDP. Countries with similar levels of health spending often display significant differences in physician availability.

This suggests that simply allocating a higher proportion of GDP to healthcare does not consistently translate into improved access. Instead, how resources are distributed and managed within healthcare systems appears to play a more significant role than overall spending levels alone.

![Figure 2](Analysis/figure2.png)

*Figure 2: Relationship between health spending and doctors per capita.*

### **Finding 3: Wealth Does Not Drive Healthcare Investment Decisions**
There is virtually **no correlation (0.02)** between GDP per capita and health spending as a percentage of GDP. The scatter plot shows no clear pattern, with both low- and high-income countries exhibiting a wide range of health spending levels.

This indicates that wealthier countries do not necessarily allocate a larger share of their economic resources to healthcare. Instead, healthcare investment appears to reflect national policy priorities, institutional structures, and strategic decisions rather than overall economic wealth alone.

![Figure 3](Analysis/figure3.png)

*Figure 3: Relationship between GDP per capita and health spending.*

### **Finding 4: High-Income Countries Achieve Strong Healthcare Access Despite Lower Relative Spending**

Country-level analysis further reinforces these findings. For example, Luxembourg, the wealthiest country in the dataset with GDP per capita exceeding $130,000, allocates only about **5.6–5.8%** of its GDP to healthcare while maintaining one of the highest levels of doctors per capita (approximately 18 physicians per capita). Similarly, Ireland exhibits high GDP levels with relatively moderate healthcare spending but still achieves strong physician availability.

These examples demonstrate that high-income countries can maintain strong healthcare access without proportionally high spending, suggesting potential efficiencies or structural advantages within their healthcare systems.

### **Supporting Evidence: Correlation Matrix**

A correlation matrix of all variables confirms these patterns. GDP per capita shows a strong positive correlation with doctors per capita (0.78), while health spending has a weaker relationship (0.46). Additionally, the near-zero correlation between GDP and health spending (0.02) reinforces the conclusion that economic wealth does not directly determine healthcare investment levels.

It is also important to note that health expenditure and health spending are perfectly correlated (1.00), indicating that they represent the same underlying measure and were treated as equivalent variables in the analysis.

![Figure 4](Analysis/figure4.png)

*Figure 4: Correlation matrix of key socioeconomic and healthcare indicators.*

---

## Future Work

### Lessons Learned

Throughout this project, we gained a deeper understanding of the complexities involved in working with real-world datasets. While publicly available data from sources such as the World Bank and OECD appear clean at a high level, integrating them revealed challenges related to consistency, completeness, and variable alignment (Module 10, Module 7). We also developed our analytical and problem solving skills when defining our integration scope amd methods. This emphasized that data must be actively managed and refined throughout the data lifecycle rather than assumed to be immediately usable (Module 2).

Additionally, we developed practical experience organizing our workflow into a reproducible pipeline. Using OpenRefine for data integration, as well as using Python for exploratory analysis highlighted the importance of computational reproducibility and transparency (Module 1, Module 14). Ensuring that results could be consistently regenerated using the same data and code reinforced key principles of data curation and documentation.

---

### Limitations

This project highlights several limitations related to data quality and integration. First, the dataset is limited to only four years of data due to the overlap between the World Bank and OECD sources. This reflects a timeliness constraint (Module 10), as the integration process required restricting the dataset to a common time window, limiting the ability to analyze long-term trends.

Second, the analysis relies on secondary observational data (Module 4), meaning that we were not involved in the data collection process. As discussed in lecture, this introduces uncertainty regarding how the data was collected, potential biases, and limitations in accuracy.

Additionally, while the dataset was cleaned and integrated to ensure completeness and consistency (Module 10, Module 7), it does not include key health outcome variables such as life expectancy or infant mortality. This limits the ability to directly evaluate public health outcomes and instead focuses on healthcare access.

Finally, the analysis is based on correlation, which does not establish causation. This reflects a fundamental limitation of observational data (Module 4) and highlights the need for more advanced analytical methods to fully understand underlying relationships.

---

### Potential Extensions

Future work could expand this project in several meaningful ways. One potential extension is to incorporate additional variables, such as life expectancy, infant mortality rates, or education levels, to provide a more comprehensive analysis of public health outcomes. Including these variables would allow for stronger connections between socioeconomic factors and actual health results.

Another extension would be to apply more advanced statistical methods, such as regression analysis, to better understand relationships between variables while controlling for confounding factors. This would move beyond simple correlation and provide deeper analytical insight into the data.

Additionally, expanding the dataset beyond the European Union to include a broader set of countries and a longer timeline would address current limitations related to timeliness and scope (Module 10). This would allow for deeper trend analysis and allow us to generalize our findings better.

Finally, further investigation into outlier countries, such as Luxembourg and Ireland, could provide valuable insights into how certain nations achieve strong healthcare access despite relatively lower proportional spending. This type of deeper analysis reflects the importance of interpreting patterns within observational data rather than relying solely on aggregate trends (Module 4).

---

## Challenges

Throughout this project, we encountered several challenges that directly relate to key concepts in data curation and the data lifecycle (Module 1, Module 2). While many of these issues were expected when working with multiple real-world datasets, actually dealing with them in practice required more time and iteration than we initially anticipated.

One of the primary challenges was addressing data heterogeneity during integration (Module 7). The World Bank and OECD datasets differed significantly in structure, formatting, and variable naming conventions. Even when the datasets were measuring similar concepts, they were often labeled differently or stored in different formats, which made direct merging difficult. We had to spend a considerable amount of time aligning schemas and transforming both datasets into a consistent structure. This process highlighted challenges related to schema mapping and semantic ambiguity (Module 7), where similar indicators do not always translate cleanly across sources. In some cases, we had to make judgment calls about which variables were truly comparable, which introduced a level of subjectivity into the integration process.

Another major challenge involved ensuring data quality across multiple dimensions (Module 10). Because we were combining datasets from different sources, inconsistencies naturally emerged. We encountered missing values, differences in country naming conventions, and occasional discrepancies in reported values. To address this, we went through multiple rounds of data cleaning, including identifying missing or invalid entries, standardizing formats, and verifying the accuracy of merged records. This process reflects key components of data cleaning workflows such as discovery, error detection, and repair (Module 10). Even after cleaning, there was still some uncertainty about whether all inconsistencies had been fully resolved, which is a common issue when working with large, secondary datasets.

The restriction to overlapping years also introduced a timeliness constraint (Module 10). Since the World Bank and OECD datasets did not fully overlap in terms of time coverage, we had to limit our analysis to a smaller time window of four years. While this decision improved consistency and comparability, it reduced the overall depth of our analysis and limited our ability to observe long-term trends. This tradeoff between data consistency and temporal coverage was something we had to carefully consider.

We also faced challenges related to reproducibility and transparency (Module 1, Module 14). Transitioning from exploratory work in a notebook environment to a structured Python script required us to rethink how our code was organized. In the notebook, it was easy to run cells out of order or rely on intermediate variables, but creating a reproducible pipeline meant that everything had to be clearly defined and executable from start to finish. This aligns with the concept of computational reproducibility, where results must be consistently reproducible using the same data, code, and environment (Module 1). Getting to that point required restructuring our workflow and being more intentional about how we wrote and documented our code.

Finally, managing files across local environments and GitHub introduced additional challenges in workflow organization. We had to ensure that all scripts, datasets, and outputs were properly structured so that others could easily navigate and reproduce our work. At times, this was confusing, especially when dealing with file paths, environment differences, and version control issues. However, this process reinforced the importance of proper data curation, documentation, and organization throughout the data lifecycle (Module 1, Module 2). Overall, these challenges were a key part of the learning experience and helped us better understand what it takes to work with real-world data in a structured and reproducible way.

---

## Reproducing
### Files
Here are the files needed for the following:
#### Data Sources
- [World Bank World Development Indicators](https://databank.worldbank.org/source/world-development-indicators)
- [OECD Data Portal](https://data.oecd.org/)

#### Reproducibility Files

Full OpenRefine operation histories are included for each cleaned dataset:

- [GDP Cleaning Operations](data/clean/gdp_openrefine_operations.json)
- [Health Expenditure Cleaning Operations](data/clean/health_expenditure_openrefine_operations.json)
- [Health Spending Cleaning Operations](data/clean/health_spending_openrefine_operations.json)
- [Doctors per Capita Cleaning Operations](data/clean/doctors_openrefine_operations.json)

- [Analysis Notebook](Analysis/Data_Analysis.ipynb)
- [Merged Dataset](data/merged/merged_dataset.csv)


For this project, we used integrated data from the World Bank World Development Indicators (WDI) and OECD Data Portal. We filtered this data to only EU countries. The final merged dataset includes:
1. 25 EU Countries
2. 4 overlapping years (we had originally planned 10, but there was limited overlap across all datasets)
3. 98 observations
4. 0 missing values after integration
5. Variables included:
   1. GDP per capita
   2. Government health expenditure
   3. Health spending
   4. Doctors per capita

Our repository is structured as follows:
project/ ├── Analysis/ │ ├── Data Analysis.ipynb │ ├── data/ │ ├── raw/ │ │ ├── gdp_per_capita_raw.csv │ │ ├── health_expenditure_raw.csv │ │ ├── health_spending_raw.csv │ │ └── doctors_per_capita_raw.csv │ │ │ ├── clean/ │ │ ├── gdp_per_capita.csv │ │ ├── health_expenditure.csv │ │ ├── health_spending.csv │ │ ├── doctors_per_capita.csv │ │ └── README.md │ │ │ ├── merged/ │ │ ├── merged_dataset.csv │ │ └── README.md │ └── README.md

The datasets used were from the World Bank World Development Indicators and the OECD Data Portal. From the World Bank World Development Indicators, we used:
1. GDP per capita
2. Government health expenditure
From OECD Data Portal:
1. Health spending
2. Doctors per capita
You can access these raw source files in: data/raw/

### Data Cleaning
For data cleaning, we used OpenRefine. Full OpenRefine cleaning operations are included in data/clean/openrefine_operations.json. This allows the cleaning workflow (filtering EU countries, standardizing country names, removing inconsistent records, and formatting variables) to be replayed exactly in OpenRefine. The clean files we exported from OpenRefine can be accessed in: data/clean/

The cleaning steps are as follows:
1. Filtered all raw data sources so that the data only consisted of EU countries. We renamed all columns with country data to the "country" column. There should be 25 countries total.
   Final country list:
      Austria, Belgium, Bulgaria, Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Netherlands, Poland, Portugal, Romania, Slovak Republic, Slovenia, Spain, Sweden.
2. Went through and checked every country name and made sure the spelling was consistent across all the datasets. A naming consistency we had to change was renaming the datasets from "Slovak Republic" to "Slovakia" before merging.
3. We removed all variables we weren't interested in using for analysis. The datasets had columns that contained information we didn't need to use for this project. The remaining variables were "country", "year", and indicator values.
4. Finally, we made sure all datasets had the same format. We checked for duplicates and verified that all numbers were recorded in the correct format. All four datasets overlapped for only 4 years; the final analysis used 4 years rather than the originally planned 10 years.

### Data Inegration
For merging our datasets, we used Python, and our integration can be performed in: Analysis/Data Analysis.ipynb.

Merge:
import pandas as pd

gdp = pd.read_csv("gdp_per_capita.csv")
health_exp = pd.read_csv("health_expenditure.csv")
health_spend = pd.read_csv("health_spending.csv")
doctors = pd.read_csv("doctors_per_capita.csv")

df = gdp.merge(health_exp, on=["country", "year"], how="inner")
df = df.merge(health_spend, on=["country", "year"], how="inner")
df = df.merge(doctors, on=["country", "year"], how="inner")

df.to_csv("merged_dataset.csv", index=False)

df.head()

The shared key we used to merge the datasets was "country" + "year". We did inner joins to only keep overlapping observations. You can find the final merged output in: data/merged/merged_dataset.csv

### Validation
To validate your dataset, there are a couple of sanity checks that should be performed to make sure you have correctly filtered your data. We used:

df.shape
df.isnull().sum()
df["country"].nunique()
df["year"].nunique()

The results from above should be as follows:
   1. 98 rows
   2. 6 variables
   3. 25 countries
   4. 4 years
   5. 0 missing values

### Analysis Reproduction
Run: jupyter notebook Analysis/Data\ Analysis.ipynb

This line will provide you with the analysis we conducted with our merged dataset.

### Software

Install: pip install pandas matplotlib jupyter

## References

<!-- Use a consistent format (APA, Chicago, etc.) -->

1. [Author(s). (Year). *Dataset/Paper title*. Publisher. https://doi.org/...]
2. [Author(s). (Year). *Dataset/Paper title*. Publisher. https://doi.org/...]
3. [Software: e.g., McKinney, W. (2010). pandas. https://pandas.pydata.org]
