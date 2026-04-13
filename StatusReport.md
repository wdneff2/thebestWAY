# Milestone Report
> This report serves as an update the to Project plan in regards to any progress that is made towards to the final submision in regards to the project

---

## Task Updates

<!-- * An update on each of the tasks described on your project plan, including references and links to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc). -->

- **Task 1: Dataset Identification - Will**
  - **Status:** ✅ Complete
  - **Updates:** 
  - **References:** [Workflow Diagram](link) | [Script](link)


- **Task 2: Data Acquisition - Autumn**
  - **Status:** ✅ Complete
  - **Updates:** We identified and obtained the datasets needed for our project from the World Bank Open Data portal and the OECD Data Portal. Specifically, we selected relevant indicators such as GDP per capita and government health expenditure from the World Bank World Development Indicators (WDI), along with health-related indicators such as health spending and doctors per capita from the OECD.
  - We ensured that both datasets contain country-level and year-based data so they can be integrated in later stages of the project. Additionally, we confirmed that the datasets are accessible, relevant to our research question, and suitable for further cleaning and analysis.
  - **References:** World Bank WDI | OECD Data Portal

- **Task 3: Data Cleaning & Integration - Autumn**
  - **Status:** 🟡 In Progress
  - **Updates:** We narrowed our integration plan to two primary data sources: the World Bank World Development Indicators (WDI) dataset and selected OECD health indicators. Our goal is to combine the economic and public health data for EU countries using shared identifiers found in both datasets. For this merge, we are planning to use the country name as the main key and the year as the secondary key so that all data aligns over time. From the World Bank, we are planning to use GDP per capita and government health expenditure, while from the OECD, we will use indicators such as health spending and doctors per capita. We may also include variables like life expectancy or infant mortality, depending on data completeness. To maintain consistency, we are focusing only on EU countries and the most recent 10 years where both datasets overlap.
  - Before merging, we will clean and standardize the data to ensure compatibility between the datasets. Variable names and formats may differ slightly, so we will need to align country names, rename columns where necessary, and ensure year formats are consistent. To do this, we will use OpenRefine, which we found helpful for identifying inconsistencies such as formatting issues, duplicates, and variations in naming. After cleaning, we will export the data as a standardized CSV file and use it for further analysis and visualization.
  - **References:** OpenRefine workflow | World Bank WDI | OECD indicators
 
- **Task 4: Exploratory Data Analysis - Yuri, Will**
  - **Status:** ⬜ Not Started
  - **Updates:** 
  - **References:** [Workflow Diagram](link) | [Script](link)
 
- **Task 5: Interim Status Report - Team**
  - **Status:** 🟡 In Progress
  - **Updates:** 
  - **References:** [Workflow Diagram](link) | [Script](link)

<!-- Add more tasks as needed -->

---

## Updated Timeline

<!-- * An updated timeline indicating the status of each task and when they will be completed. -->

| Task | Owner | Original Due Date | Updated Due Date | Status |
|------|-------|:-----------------:|:----------------:|--------|
| Dataset Identification | Will | | | ✅ Complete |
| Data Acquisition | Autumn | | | ✅ Complete |
| Data Cleaning & Integration | Autumn | | | 🟡 In Progress |
| Exploratory Data Analysis | Yuri, Will | | | ⬜ Not Started |
| Interim Status Report | Team | | | 🟡 In Progress |

---

## Project Plan Changes

<!--* A description of any changes to your project plan itself, in particular about your progress so far. Also include changes you made to your plan based on feedback you may have received for Milestone 2. -->

### Changes to Scope / Approach

- Compared with our original project plan, we have narrowed our approach by focusing specifically on EU countries and the most recent 10 years of overlapping data. Before, we were trying to work with the full historical span of both sources, but we found this to be too much. Now we feel at ease with our project manageability, and this will help improve comparability between the datasets.
- Additionally, we narrowed down our integration approach. We decided to merge primarily on country and year, and to use OpenRefine to standardize labels and prepare the datasets before analysis. Our original plan was too broad, and this is our way of narrowing down data cleaning.



### Changes Based on Milestone 2 Feedback

- 

### Progress Summary

> Brief narrative of where the project stands overall.

---

## Challenges & Problems

<!-- * Summarize any challenges or problems you have encountered so far. For each issue, explain how you resolved it or describe your plan to address it in the near future. -->

### Challenge 1: Narrowing Down Datasets and Indicators

- **Description:** We originally provided larger data collections with the intent of narrowing them
  down later, but quickly realized there was too much to choose from in regards to what
  datasets and indicators to look at specifically.

- **Resolution / Plan:** Through team discussion, we decided to use two datasets that complement
  each other and can be integrated based on country and year. For relevancy, we narrowed our
  scope to only EU countries over the most recent 10 years of data points.

  **1. World Bank Open Data** ([data.worldbank.org](https://data.worldbank.org/))
  Contains development indicators for over 200 countries, including GDP per capita, health
  expenditure, and population statistics. Provides the socioeconomic context needed to analyze
  health outcomes.

  - Specifically, we will use the **World Development Indicators (WDI)** via the
    [searchable API](https://raw.githubusercontent.com/worldbank/open-api-specs/refs/heads/main/Data360%20Open_API.json).
    This is the primary World Bank collection of development indicators compiled from
    officially-recognized international sources, and includes national, regional, and global
    estimates. We will use these financial and nonfinancial indicators against health factors
    to compare EU countries.

  **2. OECD Data Portal** ([oecd.org/en/data.html](https://www.oecd.org/en/data.html))
  Offers detailed health statistics for member countries, including life expectancy, infant
  mortality, and healthcare access metrics.

  - Specifically, we will cross-reference two indicators within the OECD Data Portal:
    - [Health Spending](https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.JAI/DSD_TAXBEN_PTR@DF_PTRUB/1.0?references=all)
    - [Doctors per Capita](https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.HD/DSD_HEALTH_EMP_REAC@DF_PHYS/1.0?references=all)

  These indicators will help us discover patterns between the relative scope of health within
  a country and other socioeconomic development indicators across the EU.

  > **Integration Note:** Both datasets use standardized country names (e.g., "Austria") and
  > consistent year labeling, making it straightforward to join and clean the data with no
  > additional preprocessing steps needed.

  >**Project Plan Note:** This update is reflected within our Project Plan as well

  ### Challenge 2: Potential Computational Overload from Large Datasets

- **Description:** Since we are interacting with a large number of datasets, we anticipate that
  cleaning and analyzing the data may overload our computers.

- **Resolution / Plan:** To preemptively address this, we have decided to use **OpenRefine**
  (that to which we learned from our Lab 11) to clean the data, fuse the datasets together,
  and then export the result to another platform for manipulation and insight discovery.
  This approach offloads the heavy data processing from our local machines and gives us a
  clean, unified dataset to work with before any analysis begins.

---

## Team Contributions

> ⚠️ Each team member must **individually commit** their own contribution summary to the repo.

### Autumn

> Focused on data integration and cleaning. Helped determine how the datasets will be merged using country and year, narrowed the scope to EU countries and recent data, and planned the use of OpenRefine to standardize and clean the data before merging.

### Will

> For will

### Yuri

>For Yuri
