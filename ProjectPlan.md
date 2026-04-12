This file explores our preliminary plan as our group tackles the final project. It is subject to change and alteration as we progress throughout the project, but it will overall not deviate drastically from this layout.

## Overview: 
The goal of this project is to analyze how socioeconomic factors influence public health outcomes across European countries. In particular, we are aiming to investigate whether indicators like GDP per capita and government health expenditure are associated with key health metrics such as life expectancy and infant mortality. Understanding these relationships highlights broader patterns between economic development and population health, as well as identify any regional disparities that might persist even among economically similar countries.

To accomplish this, we will utilize publicly available data from the World Bank Open Data portal and the OECD Data Portal, with the World Bank dataset offering broad socioeconomic indicators and the OECD dataset providing detailed health statistics. Because both datasets contain standardized country identifiers and time-series data, they can be linked by country and year to create a unified dataset for our analysis.

Our workflow will involve several stages. First, we have already acquired relevant datasets, documenting their origin, any transformations done to them, ownership, etc. Next, we will clean, standardize, and integrate the data to ensure any country identifiers and metrics are consistent. Once the combined dataset is constructed, we will perform exploratory data analysis and visualization to identify any trends and relationships in the data. Finally, we will interpret the results and communicate our findings through visualizations, written analysis, and a reproducible project repository. 

## Team: ##
Our team is made up of 3 members (which has been approved through the professor and TA team), which is different than the typical team. As such, our roles are relatively different than a typical team. See below the distribution and responsibilities:
1. Autumn: Data integration, Data quality assessment, Data cleaning, Data documentation and metadata, Extraction and enrichment
2. Will: Data acquisition, Storage, and organization strategy, Workflow automation and provenance, Reproducibility package, Git/GitHub repository setup and maintenance
3. Yuri: Data analysis and visualization, Findings and interpretation, Overall project documentation, Ethical/legal compliance, Final report coordination and quality control

## Research Question(s): 
After being able to explore the world or having a desire to explore and travel after graduation, it is equally important that we are aware of the state of individual countries. Narrowing our scope down to Europe (due to both personal connections to the EU and it being a popular travel destination for many post-graduate plans), we want to explore the correlation between socioeconomic indicators and public health outcomes. Specifically, our research aims to look at the following:
1. How do socioeconomic indicators like GDP per capita and government health expenditure correlate to key public health outcomes like life expectancy and infant mortality across European countries?
2. Are there regional disparities in health outcomes that persist even after accounting for economic factors?

## Datasets:
We will use two datasets that complement each other and can be integrated based on country and year. While important to see changes in time, a lot happens over the course of time especially in the EU and so for relavancy, we will only be looking at the most recent 10 years of data points. The most recent 10 years and only looking at EU countries:

__World Bank Open Data (via https://data.worldbank.org/)__: Though these data sets are vast, our investigation will be looking at different aspects of them. They contain development indicators for over 200 countries, including GDP per capita, health expenditure, and population statistics. It also provides the socioeconomic context needed to analyze health outcomes.

Specifically within the World Bank Open Data, we will be using World Development Indicators (WDI) (with the Searchable API of https://raw.githubusercontent.com/worldbank/open-api-specs/refs/heads/main/Data360%20Open_API.json). This dataset is the primary World Bank collection of development indicators, compiled from officially-recognized international sources. It presents the most current and accurate global development data available, and includes national, regional and global estimates. We can use these indicators (financial and explorations of nonfinancial ones) against the health factors to plot out how different countries in the EU compare.

__OECD Data Portal (via https://www.oecd.org/en/data.html)__: Similarly, the dataset itself is vast, and through our investigation, we aim to narrow down on what is the specific dataset that we will use. It offers detailed health statistics for member countries, including life expectancy, infant mortality, and healthcare access metrics.

Specfically within the OECD Data Portal, we will cross reference a couple of different indicators. Those being health spending (https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.JAI/DSD_TAXBEN_PTR@DF_PTRUB/1.0?references=all) and doctors per capita (https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.HD/DSD_HEALTH_EMP_REAC@DF_PHYS/1.0?references=all). These can help us discover unique patterns between the relative scope of health within a country and other socioeconomic development indicators in the EU.

All these datasets have different columns and display different information, but it is important that we are able to convene these sets based on the standardized name of the country as well as the year. For example both sets use the name "Austria" and label their years in the same manner so that we are able to converge the datasets and clean it. There are no additional steps needed as the labeling is consistent, meaning that joining the individual sets will be seamless and easy. 

## Timeline:

| Task | Description | Responsible Member(s)| Target Completion Date|
| :---: | :---: | :---: | :---: |
| Dataset Identification | Identify relevant indicators from the World Bank and OECD databases. | Autumn, Will | March 15 |
| Data Acquisition | Download selected datasets and document data provenance, licensing, and metadata. | Will | March 15 |
| Data Cleaning | Standardize country names/codes, remove inconsistent records, and prepare datasets for integration. | Autumn | March 20 |
| Data Integration | Merge datasets using shared identifiers such as country and year, ensuring that the combined dataset is accurate and consistent. | Autumn | March 31 |
| Exploratory Data Analysis | Conduct initial statistical exploration and produce preliminary visualizations to identify trends or correlations. | Yuri | April 10 |
| Interim Status Report Preparation | Summarize progress, challenges, and preliminary insights for the course milestone. | Yuri, Autumn, Will | April 14 |
| Analysis & Data Visualization | Develop deeper statistical analysis and improved visualizations to answer the research questions. | Yuri | April 20 |
| Interpretation of Findings | Evaluate results and assess relationships between socioeconomic indicators and health outcomes. | Yuri, Autumn | April 25 |
| Documentation & Reproducibility | Finalize code documentation, workflow description, and ensure reproducibility of the data pipeline. | Will | April 30 |
| Final Report Writing & Review  | Compile analysis, visualizations, and discussion into the final project report and prepare GitHub release. | Yuri, Autumn, Will | May 1 |
| Final Project Submission | Publish GitHub release and submit final project deliverables. | Yuri, Autumn, Will | May 3 |

## Constraints:
We identified the top 4 constraints in relation to our project plan below:
1. Some countries or years within the dataset may have missing values for the different indicators. For example, life expectancy, infant mortality, or health expenditure may not be completely filled in.
2. There may be minor dataset differences in how the values are reported. World Bank and OECD data may use different country names or indicator definitions. This will require standardization and merging.
3. We can only analyze the data of overlapping years. Our datasets may cover different time ranges, so we won't be able to use all the data if that's the case.
4. The analysis we conduct can help us identify correlations between socioeconomic factors and health outcomes, but we cannot establish causation.

## Gaps:
We identified the top 4 gaps we plan on assessing as we begin our project within the next couple of weeks below:
1. The specific variables from each dataset still need to be chosen and finalized.
2. We have to review which European countries are available within both datasets before we can finalize the exact set of European countries that will be included.
3. Like above, we cannot determine the final analysis period until we find the overlapping years across our datasets.
4. The team has not yet chosen which statistical techniques and visualization methods we will be using.
