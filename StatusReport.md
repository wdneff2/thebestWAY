# Milestone Report
> This report serves as an update the to Project plan in regards to any progress that is made towards to the final submision

---

## Task Updates

<!-- * An update on each of the tasks described on your project plan, including references and links to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc). -->

- **Task 1: Dataset Identification - Will**
  - **Status:** Complete
  - **Updates:** Based on the question that we proposed, our group discovered that we needed separate datasets related to health as well as development indicators. While there are a lot of indicators related to representing the state of a country regarding its health, we tried to find some interesting indicators that are related to health — those being the number of doctors and money spent. With that, there is a large set of indicators that we can further examine in their interaction with the health indicators. Things like GDP, life expectancy, and crime rate are all factors that we could look at in relation to health
  - **References:** Project Plan


- **Task 2: Data Acquisition - Autumn**
  - **Status:** Complete
  - **Updates:** We identified and obtained the datasets needed for our project from the World Bank Open Data portal and the OECD Data Portal. Specifically, we selected relevant indicators such as GDP per capita and government health expenditure from the World Bank World Development Indicators (WDI), along with health-related indicators such as health spending and doctors per capita from the OECD.
  - We ensured that both datasets contain country-level and year-based data so they can be integrated in later stages of the project. Additionally, we confirmed that the datasets are accessible, relevant to our research question, and suitable for further cleaning and analysis.
  - **References:** World Bank WDI | OECD Data Portal

- **Task 3: Data Cleaning & Integration - Autumn**
  - **Status:** In Progress
  - **Updates:** We narrowed our integration plan to two primary data sources: the World Bank World Development Indicators (WDI) dataset and selected OECD health indicators. Our goal is to combine the economic and public health data for EU countries using shared identifiers found in both datasets. For this merge, we are planning to use the country name as the main key and the year as the secondary key so that all data aligns over time. From the World Bank, we are planning to use GDP per capita and government health expenditure, while from the OECD, we will use indicators such as health spending and doctors per capita. We may also include variables like life expectancy or infant mortality, depending on data completeness. To maintain consistency, we are focusing only on EU countries and the most recent 10 years where both datasets overlap.
  - Before merging, we will clean and standardize the data to ensure compatibility between the datasets. Variable names and formats may differ slightly, so we will need to align country names, rename columns where necessary, and ensure year formats are consistent. To do this, we will use OpenRefine, which we found helpful for identifying inconsistencies such as formatting issues, duplicates, and variations in naming. After cleaning, we will export the data as a standardized CSV file and use it for further analysis and visualization.
  - **References:** OpenRefine workflow | World Bank WDI | OECD indicators
 
- **Task 4: Exploratory Data Analysis - Yuri, Will**
  - **Status:** Not Started
  - **Updates:** As Task 3 is still in progress, we have been unable to begin Task 4. Delays are due to just recently updating our Project Plan, addressing comments left by the TA, as well as very recently learning how to use OpenRefine, which we plan to use for Task 3. 
  - **References:** N/A
 
- **Task 5: Interim Status Report - Team**
  - **Status:** In Progress
  - **Updates:** None, waiting for task 3-4 to be complete.
  - **References:** N/A

<!-- Add more tasks as needed -->

---

## Updated Timeline:

<!-- * An updated timeline indicating the status of each task and when they will be completed. -->

| Task | Description | Responsible Member(s)| Target Completion Date|
| :---: | :---: | :---: | :---: |
| Dataset Identification | Identify relevant indicators from the World Bank and OECD databases. | Autumn, Will | Complete |
| Data Acquisition | Download selected datasets and document data provenance, licensing, and metadata. | Will | Complete |
| Interim Status Report Preparation | Summarize progress, challenges, and preliminary insights for the course milestone. | Yuri, Autumn, Will | Complete |
| Data Cleaning | Standardize country names/codes, remove inconsistent records, and prepare datasets for integration. | Autumn | April 15 |
| Data Integration | Merge datasets using shared identifiers such as country and year, ensuring that the combined dataset is accurate and consistent. | Autumn | April 17 |
| Exploratory Data Analysis | Conduct initial statistical exploration and produce preliminary visualizations to identify trends or correlations. | Yuri | April 20 |
| Analysis & Data Visualization | Develop deeper statistical analysis and improved visualizations to answer the research questions. | Yuri | April 23 |
| Interpretation of Findings | Evaluate results and assess relationships between socioeconomic indicators and health outcomes. | Yuri, Autumn | April 26 |
| Documentation & Reproducibility | Finalize code documentation, workflow description, and ensure reproducibility of the data pipeline. | Will | April 30 |
| Final Report Writing & Review  | Compile analysis, visualizations, and discussion into the final project report and prepare GitHub release. | Yuri, Autumn, Will | May 1 |
| Final Project Submission | Publish GitHub release and submit final project deliverables. | Yuri, Autumn, Will | May 3 |

---

## Project Plan Changes

<!--* A description of any changes to your project plan itself, in particular about your progress so far. Also include changes you made to your plan based on feedback you may have received for Milestone 2. -->

### Changes to Scope / Approach

- Compared with our original project plan, we have narrowed our approach by focusing specifically on EU countries and the most recent 10 years of overlapping data. Before, we were trying to work with the full historical span of both sources, but we found this to be too broad in scope and unrealistic due to time constraints. Now we feel at ease with our project manageability, and this will help improve comparability between the datasets.
- Additionally, we narrowed down our integration approach. We decided to merge primarily on country and year, and to use OpenRefine to standardize labels and prepare the datasets before analysis. Our original plan was too broad, and this is our way of narrowing down data cleaning.



### Changes Based on Milestone 2 Feedback

In response to our TA’s feedback, we made several important updates to improve both the technical setup and overall feasibility of our project.

**GitHub Submission Fix**
- Updated our repository to upload the raw `.md` file directly instead of a zipped folder  
- This ensures our project materials are easily viewable and aligned with submission expectations  

**Data Coverage & Feasibility**
- Investigated the temporal and country overlap between the World Bank WDI and OECD datasets  
- Found that:
  - Both datasets extend back to approximately the 1960s  
  - Coverage varies depending on the specific indicator and country  
  - OECD data is limited to member countries, while WDI has broader global coverage  

**Scope Refinement**
- To ensure feasibility for a 3-person team, we:
  - Limited our analysis to EU countries  
  - Focused on the most recent 10 years of overlapping data  
- This reduces missing data issues and simplifies dataset integration

**Grounding in Course Concepts**
- Explicitly incorporated key data concepts into our plan:
  - Completeness: addressing missing values across datasets  
  - Consistency: aligning country names and indicator definitions  
  - Integration constraints: restricting analysis to overlapping years and countries  

**Timeline & Task Updates**
- Met with the TA after class to clarify feedback regarding timeline and task distribution  
- While the concern was that responsibilities and deadlines were unclear, our existing timeline already specified this information  
- After reviewing it, the TA acknowledged the clarity and verbally retracted that portion of the comment  
- As a result, task distribution has remained the same, with only minor adjustments to due dates to account for delays  

Overall, these changes make our project more structured, feasible, and better aligned with course expectations.

### Progress Summary

At this stage, our project has completed the dataset identification and data acquisition phases, and is currently in the data cleaning and integration stage. We have finalized our use of the World Bank World Development Indicators (WDI) and OECD Data Portal datasets, selecting key indicators such as GDP per capita, government health expenditure, health spending, and doctors per capita.

After incorporating TA feedback and reassessing feasibility, we refined our project scope to focus specifically on EU countries and the most recent 10 years of overlapping data. This change allowed us to better address issues related to data completeness and consistency, while also making the project more manageable for a 3-person team. We also clarified our integration approach by standardizing our process to merge datasets using country and year as shared identifiers, and began using OpenRefine to clean and align the data prior to merging.

Currently, data cleaning is still in progress, which has delayed the start of exploratory data analysis. However, we now have a more structured workflow, clearer scope, and defined toolset moving forward. Once cleaning and integration are completed, we will begin exploratory data analysis and visualization to identify trends and relationships between socioeconomic indicators and public health outcomes across EU countries. 

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

>  Each team member must **individually commit** their own contribution summary to the repo.

### Autumn

> Focused on data acquisition, cleaning, and integration. Identified and selected relevant indicators from the World Bank WDI and OECD datasets, including GDP per capita, government health expenditure, and health-related metrics. Developed the integration plan by determining that datasets will be merged using country and year, narrowed the scope to EU countries and the most recent 10 years, and planned the use of OpenRefine to standardize country names, variable formats, and prepare the data for merging.

### Will

> Throughout the project, I have taken on several tasks to help us reach the specified checkpoints as well as progress towards the overall completion of the project. Most notably, I played a critical role in setting up the templates for both the Project Plan and Status Report. I set up the template based on the requirements from the Canvas page so that the rest of the group could easily fill in their respective components. Beyond the templates, I, with guidance from the team, selected our research question and the datasets that we are to use. Looking forward, I will continue to build the template that our team will use for the final project submission as well as summarize and aggregate all the data findings done by my teammates. Collaboratively, our team will create a final product that explores the relationship between health-related indicators and development indicators in the EU.

### Yuri

> I have primarily worked on shaping the analytical direction and overall structure of the project. I've been responsible for organizing and drafting key components of the project documentation, most notably the project's timeline. I also played a central role in meeting with the TA after class to clarify the project scope, feasibility, and alignment with course concepts, and communicating her expectations with the rest of the team. Looking ahead, I will lead the exploratory data analysis, visualization, and interpretation phases of the project after data cleaning and integration is complete. This includes identifying trends, building visualizations to communicate findings, and connecting results back to the research questions. 
