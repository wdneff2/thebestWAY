# [Project Title]

## Contributors
- Autumn Rosedale
- William Neff
- Yuri You

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
<!-- Target: ~500 words -->

[Describe your results. Be specific — include numbers, percentages, and statistical summaries where applicable. Reference your visualizations below.]

### [Finding 1 Title]
[Description...]

![Figure 1](results/figures/figure1.png)
*Figure 1: [Caption.]*

### [Finding 2 Title]
[Description...]

![Figure 2](results/figures/figure2.png)
*Figure 2: [Caption.]*

<!-- Add more findings/figures as needed -->

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
