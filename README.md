##notes from examples - explain what each of us did in relation to the modules in class, shorter summary (not too long), where the dataset is, how did we get it and licnense, quality and cleaning like accuracy, completeness, timeliness, etc in relation to each set, be as indepth as possible whule also acknowledging needing to be short and brief, be in depth with the reproducability 

# [Project Title]

## Contributors
- Autumn Rosedale (Data Cleaning Section and Reproducability)
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
> [`scripts/analyze.py`](scripts/analyze.py)

This section presents the key relationships identified between socioeconomic indicators and healthcare access across EU countries. The analysis focuses on GDP per capita, health spending, and doctors per capita, using both visualizations and correlation metrics to support each finding.

---

### **Finding 1: Wealth Is Strongly Associated with Healthcare Access**
A strong positive relationship exists between GDP per capita and doctors per capita, with a correlation coefficient of approximately **0.78**. This indicates that wealthier countries tend to have greater access to healthcare resources, as measured by physician availability. The scatter plot shows a clear upward trend, where countries with higher GDP levels consistently exhibit higher numbers of doctors per capita.

This finding suggests that overall economic capacity plays a significant role in shaping healthcare access, likely due to increased funding availability, infrastructure, and institutional development in wealthier nations.

![Figure 1](results/figures/figure1.png)
*Figure 1: Relationship between GDP per capita and doctors per capita.*

### **Finding 2: Health Spending Does Not Guarantee Healthcare Access**
Health spending as a percentage of GDP shows only a **moderate correlation (0.46)** with doctors per capita. While some countries with higher health spending tend to have more doctors, the relationship is much more dispersed compared to GDP. Countries with similar levels of health spending often display significant differences in physician availability.

This suggests that simply allocating a higher proportion of GDP to healthcare does not consistently translate into improved access. Instead, how resources are distributed and managed within healthcare systems appears to play a more significant role than overall spending levels alone.

![Figure 2](results/figures/figure2.png)
*Figure 2: Relationship between health spending and doctors per capita.*

### **Finding 3: Wealth Does Not Drive Healthcare Investment Decisions**
There is virtually **no correlation (0.02)** between GDP per capita and health spending as a percentage of GDP. The scatter plot shows no clear pattern, with both low- and high-income countries exhibiting a wide range of health spending levels.

This indicates that wealthier countries do not necessarily allocate a larger share of their economic resources to healthcare. Instead, healthcare investment appears to reflect national policy priorities, institutional structures, and strategic decisions rather than overall economic wealth alone.

![Figure 3](results/figures/figure3.png)
*Figure 3: Relationship between GDP per capita and health spending.*

### **Finding 4: High-Income Countries Achieve Strong Healthcare Access Despite Lower Relative Spending**

Country-level analysis further reinforces these findings. For example, Luxembourg, the wealthiest country in the dataset with GDP per capita exceeding $130,000, allocates only about **5.6–5.8%** of its GDP to healthcare while maintaining one of the highest levels of doctors per capita (approximately 18 physicians per capita). Similarly, Ireland exhibits high GDP levels with relatively moderate healthcare spending but still achieves strong physician availability.

These examples demonstrate that high-income countries can maintain strong healthcare access without proportionally high spending, suggesting potential efficiencies or structural advantages within their healthcare systems.

### **Supporting Evidence: Correlation Matrix**

A correlation matrix of all variables confirms these patterns. GDP per capita shows a strong positive correlation with doctors per capita (0.78), while health spending has a weaker relationship (0.46). Additionally, the near-zero correlation between GDP and health spending (0.02) reinforces the conclusion that economic wealth does not directly determine healthcare investment levels.

It is also important to note that health expenditure and health spending are perfectly correlated (1.00), indicating that they represent the same underlying measure and were treated as equivalent variables in the analysis.

![Figure 4](results/figures/figure4.png)
*Figure 4: Correlation matrix of key socioeconomic and healthcare indicators.*


---

## Future Work
<!-- Target: 500–1,000 words -->

### Lessons Learned
[What did you learn about the data, tools, or process that you didn't expect going in?]

### Limitations
[What are the limitations of your current analysis? What would you caution others about when interpreting results?]

### Potential Extensions
[What could be done next? New datasets, different methods, broader scope?]

---

## Challenges
<!-- Target: ~500 words -->

[Discuss the main obstacles you faced. Consider covering:
- Data access or acquisition difficulties
- Data quality problems that were hard to resolve
- Integration challenges across datasets
- Technical hurdles
- Time or resource constraints]

---

## Reproducing

### Requirements

- Python 3.x
- Install dependencies:
```bash
  pip install -r requirements.txt
```
- [Any other tools needed, e.g., PostgreSQL 15, OpenRefine 3.7]

### Steps

1. **Clone the repository**
```bash
   git clone https://github.com/[org]/[repo].git
   cd [repo]
```

2. **Acquire the data**
```bash
   python scripts/acquire_data.py
```
   > ⚠️ **Large files (>50MB):** Download from Box: [INSERT SHAREABLE BOX LINK]  
   > Save downloaded files to `data/raw/` before proceeding.

3. **Profile data quality** *(optional but recommended)*
```bash
   python scripts/profile_data.py
```

4. **Clean the data**
```bash
   python scripts/clean_data.py
```

5. **Integrate datasets**
```bash
   python scripts/integrate_data.py
```

6. **Run analysis and generate visualizations**
```bash
   python scripts/analyze.py
```

7. **Run full pipeline** *(optional, requires Snakemake)*
```bash
   snakemake --cores 1
```

Output files and figures will be saved to `results/`.

---

## References

<!-- Use a consistent format (APA, Chicago, etc.) -->

1. [Author(s). (Year). *Dataset/Paper title*. Publisher. https://doi.org/...]
2. [Author(s). (Year). *Dataset/Paper title*. Publisher. https://doi.org/...]
3. [Software: e.g., McKinney, W. (2010). pandas. https://pandas.pydata.org]
