##notes from examples - explain what each of us did in relation to the modules in class, shorter summary (not too long), where the dataset is, how did we get it and licnense, quality and cleaning like accuracy, completeness, timeliness, etc in relation to each set, be as indepth as possible whule also acknowledging needing to be short and brief, be in depth with the reproducability 

# [Project Title]

## Contributors
- Autumn Rosedale (Data Cleaning Section, Initial Data Analysis, and Reproducability)
- William Neff (Summary, Data Profile, Data Quality)
- Yuri You (Data Analysis, Data Visualizations, Findings, Future Work, Challenges)

---

## Summary
<!-- Target: 500–600 words -->

### Motivation
[Why did you choose this topic? What problem or gap does it address?]

### Research Questions
1. [Research question 1]
2. [Research question 2]

### Overview
[Briefly describe your approach — what data did you use, what methods, and what did you do overall?]

### Key Findings
[High-level summary of what you found. You'll elaborate in the Findings section.]

---

## Data Profile
<!-- Target: max 2,000 words total across all datasets -->

### Dataset 1: [Name]

| Attribute | Detail |
|-----------|--------|
| **Source** | [URL or citation] |
| **License** | [e.g., CC BY 4.0, Public Domain, Proprietary] |
| **Location in repo** | `data/raw/dataset1/` |
| **Format** | [e.g., CSV, JSON, Parquet] |
| **Size** | [e.g., 45,000 rows × 14 columns, ~12MB] |
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

### Dataset 2: [Name]

| Attribute | Detail |
|-----------|--------|
| **Source** | [URL or citation] |
| **License** | [e.g., CC BY 4.0, Public Domain, Proprietary] |
| **Location in repo** | `data/raw/dataset2/` |
| **Format** | [e.g., CSV, JSON] |
| **Size** | [e.g., 8,000 rows × 9 columns, ~3MB] |
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

<!-- Duplicate the section above for any additional datasets -->

---

## Data Quality
<!-- Target: 500–1,000 words -->

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
> [`Analysis/scripts/analyze.py`](Analysis/scripts/analyze.py)

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

For this project, we used integrated data from the World Bank World Development Indicators (WDI) and OECD Data Portal. We filtered this data to only EU countries. The final merged dataset includes:
1. 25 EU Countries
2. 4 overlapping years (we had originally planned 10, but there was limited overlap across all datasets)
3. Variables included:
   1. GDP per capita
   2. Government health expenditure
   3. Health spending
   4. Doctors per capita
4. We removed all missing values. We first cleaned each dataset separately before merging.

Our repository is structured as follows:
data/ ├── raw/ │ ├── gdp_per_capita.csv │ ├── health_expenditure.csv │ ├── health_spending.csv │ └── doctors_per_capita.csv 

clean/ ├── merged_dataset.csv 

reproducibility/ ├── merge.ipynb ├── scatter_plot.png ├── requirements.txt └── pip-freeze.txt

Reproducing our results:

1. Step 1: 

## References

<!-- Use a consistent format (APA, Chicago, etc.) -->

1. [Author(s). (Year). *Dataset/Paper title*. Publisher. https://doi.org/...]
2. [Author(s). (Year). *Dataset/Paper title*. Publisher. https://doi.org/...]
3. [Software: e.g., McKinney, W. (2010). pandas. https://pandas.pydata.org]
