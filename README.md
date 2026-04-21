# [Project Title]

## Contributors
- Autumn Rosedale
- William Neff
- Yuri You

---

## Summary
<!-- 500–600 words -->

[Describe your project here. Cover:
- What is the project about?
- What motivated you to pursue this topic?
- What research question(s) are you trying to answer?
- What did you find (high-level)?]

---

## Data Profile
<!-- Max 2000 words total across all datasets -->

### Dataset 1: [Dataset Name]

- **Location in repository:** `data/raw/dataset1/`
- **Source:** [URL or citation]
- **Format:** [e.g., CSV, JSON, SQL dump]
- **Size:** [e.g., 50,000 rows × 12 columns]
- **Description:** [What does this dataset contain? What time period or scope does it cover?]
- **Key fields/variables:**
  | Field | Type | Description |
  |-------|------|-------------|
  | `field_name` | string | Description |
  | `field_name` | integer | Description |
- **Ethical/legal constraints:** [e.g., license type, privacy considerations, redistribution restrictions]
- **Relevance to research questions:** [How does this dataset help answer your questions?]

### Dataset 2: [Dataset Name]

- **Location in repository:** `data/raw/dataset2/`
- **Source:** [URL or citation]
- **Format:** [e.g., CSV, JSON, SQL dump]
- **Size:** [e.g., 10,000 rows × 8 columns]
- **Description:** [What does this dataset contain?]
- **Key fields/variables:**
  | Field | Type | Description |
  |-------|------|-------------|
  | `field_name` | string | Description |
- **Ethical/legal constraints:** [License, privacy, redistribution notes]
- **Relevance to research questions:** [How does this dataset help answer your questions?]

<!-- Add more dataset sections as needed -->

---

## Data Quality
<!-- 500–1000 words -->

[Summarize the results of your quality assessment. Consider covering:
- Completeness: Were there missing values? In which fields? How many?
- Consistency: Were there formatting inconsistencies, duplicate records, or conflicting values?
- Accuracy: Were there outliers, impossible values, or obvious errors?
- Timeliness: Is the data current enough for your purposes?
- Any tools or scripts used to assess quality (reference files in the repo)]

---

## Data Cleaning
<!-- Max 1000 words -->

[Describe the cleaning operations performed. For each operation, explain:
1. What the issue was
2. What you did to fix it
3. Which script or tool performed the operation

Example structure:]

### Operation 1: [e.g., Removing duplicate records]
- **Issue:** [Description of the problem]
- **Action:** [What was done]
- **Script:** [`scripts/clean_data.py`](scripts/clean_data.py)

### Operation 2: [e.g., Standardizing date formats]
- **Issue:** [Description of the problem]
- **Action:** [What was done]
- **Script:** [`scripts/clean_data.py`](scripts/clean_data.py)

<!-- Add more operations as needed -->

---

## Findings
<!-- ~500 words -->

[Describe your findings. Include:
- Key numeric results
- Trends or patterns observed
- References to visualizations (embed images or link to them)

Example:]

![Visualization 1](results/figures/figure1.png)
*Figure 1: [Caption describing the figure]*

[Interpretation of results...]

---

## Future Work
<!-- ~500–1000 words -->

[Discuss:
- Lessons learned during the project
- What you would do differently
- How the analysis could be extended
- Additional datasets or methods that could improve results
- Limitations of the current approach]

---

## Challenges
<!-- ~500 words -->

[Discuss the main challenges encountered, such as:
- Data access or acquisition issues
- Data quality problems that were difficult to resolve
- Technical difficulties
- Limitations in time, compute, or expertise]

---

## Reproducing

Follow these steps to reproduce our results from scratch:

### Prerequisites

- Python 3.x (see `requirements.txt` for dependencies)
- [Any other tools, e.g., PostgreSQL, OpenRefine]

```bash
pip install -r requirements.txt
```

### Steps

1. **Clone the repository**
```bash
   git clone https://github.com/[your-repo-url].git
   cd [repo-name]
```

2. **Acquire the data**
```bash
   python scripts/acquire_data.py
```
   > If data files exceed 50MB, download them from Box: [Box link]  
   > Save downloaded files to `data/raw/` before continuing.

3. **Run data cleaning**
```bash
   python scripts/clean_data.py
```

4. **Run analysis / generate visualizations**
```bash
   python scripts/analyze.py
```

Results will be saved to `results/`.

---

## References

<!-- Use a consistent citation format, e.g., APA or Chicago -->

1. [Author(s). (Year). *Title*. Publisher/Journal. URL]
2. [Dataset citation]
3. [Software citation, e.g., pandas, scikit-learn]
