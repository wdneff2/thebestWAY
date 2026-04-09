# Milestone Report
> This report serves as an update the to Project plan in regards to any progress that is made towards to the final submision in regards to the project

---

## Task Updates

<!-- * An update on each of the tasks described on your project plan including references and links to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc). -->

- **Task 1: [Task Name]**
  - Status: 
  - Updates: 
  - References: [Script name](link) | [Dataset](link) | [Workflow](link)

- **Task 2: [Task Name]**
  - Status: 
  - Updates: 
  - References: [Workflow Diagram](link) | [Script](link)

<!-- Add more tasks as needed -->

---

## Updated Timeline

<!-- * An updated timeline indicating the status of each task and when they will be completed. -->

| Task | Owner | Original Due Date | Updated Due Date | Status |
|------|-------|:-----------------:|:----------------:|--------|
| [Task 1] | | | | 🟡 In Progress |
| [Task 2] | | | | ✅ Complete |
| [Task 3] | | | | 🔴 Blocked |
| [Task 4] | | | | ⬜ Not Started |

---

## Project Plan Changes

<!--* A description of any changes to your project plan itself, in particular about your progress so far. Also include changes you made to your plan based on feedback you may have received for Milestone 2. -->

### Changes to Scope / Approach

- 

### Changes Based on Milestone 2 Feedback

- 

### Progress Summary

> Brief narrative of where the project stands overall.

---

## Challenges & Problems

<!-- * Summarize any challenges or problems you have encountered so far. For each issue, explain how you resolved it or describe your plan to address it in the near future. -->

## Challenges & Problems

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

  - Specifically, we will cross-reference two indicators:
    - [Health Spending](https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.JAI/DSD_TAXBEN_PTR@DF_PTRUB/1.0?references=all)
    - [Doctors per Capita](https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.HD/DSD_HEALTH_EMP_REAC@DF_PHYS/1.0?references=all)

  These indicators will help us discover patterns between the relative scope of health within
  a country and other socioeconomic development indicators across the EU.

  > **Integration Note:** Both datasets use standardized country names (e.g., "Austria") and
  > consistent year labeling, making it straightforward to join and clean the data with no
  > additional preprocessing steps needed.

  >**Project Plan Note:** This update is reflected within our Project Plan as well

---

## Team Contributions

> ⚠️ Each team member must **individually commit** their own contribution summary to the repo.

### Autumn

> For Autumn to fill out

### Will

> For will

### Yuri

>For Yuri
