Healthcare Data Exploration & Requirement Planning
Week 1 Project Plan
Focus: Diabetes and Chronic Disease Burden, and Hospital Readmission Outcomes
Submitted by: Priya Kailas Rakshe
Role: Healthcare Data Analyst Intern
Programme: B.Tech Bioengineering, MIT School of Bioengineering Sciences & Research, MIT-ADT University
Date: 1 October 2026
Repository: github.com/<PriyaRakshe>/healthcare-data-analysis-project


1. Introduction and Project Overview
Healthcare organisations generate large volumes of data on patients, treatments, outcomes and costs. A Healthcare Data Analyst turns this data into evidence that helps clinicians, hospital managers and policymakers make better decisions.
This document is the Week 1 planning deliverable for my analysis project. It sets out what I will analyse, why, which public data sources I will use, the questions and hypotheses that will guide the work, and a six-week roadmap covering extraction, transformation, analysis and visualization.
Theme chosen: diabetes and related chronic disease. Diabetes is a high-burden non-communicable disease (NCD) that affects population health (prevalence and mortality) and hospital operations (admissions, length of stay and readmissions). This lets me study the problem at three levels: global, national (India) and hospital or patient level.
2. Project Objectives
2.1 Main objective
To explore public healthcare datasets and identify patterns in diabetes-related risk factors, population-level disease burden and hospital readmission outcomes, and to present the findings as clear, decision-ready insights.
2.2 Specific objectives
•Identify which clinical and demographic factors are most associated with diabetes.
•Understand which hospital-encounter factors are associated with 30-day readmission among diabetic patients.
•Compare diabetes and NCD burden across Indian states and across world regions.
•Build a reproducible workflow (extract, clean, analyse, visualize) documented on GitHub.
•Translate analytical findings into practical recommendations for healthcare stakeholders.
2.3 Stakeholders and who benefits
•Hospital administrators: identify patient groups at higher risk of readmission to plan follow-up care.
•Clinicians: understand risk factors that matter most when screening patients.
•Public health planners: see which regions carry the highest burden and need targeted programmes.
3. Key Healthcare Metrics
The following metrics are standard in healthcare analytics and will be used to answer the research questions.
Metric	Definition	Why it matters
Prevalence	Proportion of a population with a condition at a given time	Measures disease burden and screening needs
Incidence	Number of new cases in a population over a period	Shows how fast a disease is spreading
Mortality rate	Deaths per 100,000 population (crude or age-standardised)	Shows severity and impact of a disease
Premature NCD mortality	Probability of dying between ages 30 and 70 from major NCDs	WHO headline indicator for NCD progress
30-day readmission rate	Share of discharged patients readmitted within 30 days	Indicator of care quality and cost pressure
Average length of stay (ALOS)	Mean number of days per hospital admission	Reflects efficiency and case complexity
Utilisation measures	Prior inpatient, outpatient and emergency visits; number of lab tests, procedures and medications	Proxy for patient complexity and risk
Clinical measures	BMI, plasma glucose, blood pressure, HbA1c	Core risk factors for diabetes and complications
Demographic breakdowns	Age group, gender, region, urban or rural	Reveals inequalities and high-risk groups
Bed occupancy rate	Occupied bed-days divided by available bed-days	Hospital capacity metric (context for operational analysis)

4. Public Data Sources and Justification
I researched several public sources and shortlisted four that together cover global, national and patient-level views of the same theme. Each is open or freely accessible, so the work is reproducible.
4.1 Diabetes 130-US Hospitals for Years 1999 to 2008 (UCI Machine Learning Repository)
•What it contains: About 100,000 hospital encounters for diabetic patients across 130 US hospitals, with roughly 50 variables including demographics, admission type, length of stay, lab tests, medications, diagnoses and readmission status (<30 days, >30 days, no readmission).
•Format and access: CSV download from the UCI repository; free to use with citation.
•Justification: It is one of the few openly available hospital-encounter datasets with a direct readmission outcome, which maps closely to real hospital analytics work. Its size supports meaningful grouping, statistical testing and visualization.
•Limitations: Data is dated (1999 to 2008) and from the US; some fields have many missing values and coded diagnoses need mapping. Findings are about association, not causation.
4.2 Pima Indians Diabetes Database (National Institute of Diabetes and Digestive and Kidney Diseases, via UCI/Kaggle)
•What it contains: 768 records of female patients aged 21 or older, with eight clinical variables (pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, age) and a diabetes outcome flag.
•Format and access: Single CSV file, freely available.
•Justification: A compact, well-known clinical dataset ideal for exploring how risk factors relate to diabetes, practising data cleaning and building clear visual comparisons.
•Limitations: Small sample and a single population group, so results cannot be generalised. Several variables record zero where a value is biologically impossible (e.g. glucose, blood pressure), which are really missing values and must be handled during cleaning.
4.3 National Family Health Survey, NFHS-5 (India), 2019 to 2021
•What it contains: Indicators from a large nationally representative household survey, reported by state and district, including nutrition, BMI, hypertension and elevated blood glucose among adults, plus background characteristics such as age, residence and wealth.
•Format and access: State and district fact sheets and datasets from the Ministry of Health and Family Welfare and the International Institute for Population Sciences, and the DHS Program (registration may be needed for unit-level data); indicator tables are also available through India's open data portal.
•Justification: It brings the analysis to my own national context and allows state-level comparison of risk factors, which supports public-health style questions and geographic visualization.
•Limitations: Survey-based and partly self-reported; fact sheets give aggregated values only, and definitions can differ slightly between survey rounds.
4.4 WHO Global Health Observatory (GHO)
•What it contains: Country-level indicators over time, including NCD mortality, premature NCD mortality, diabetes-related indicators, risk-factor prevalence and health-system statistics, with breakdowns by region, income group and sex.
•Format and access: Downloadable CSV and a public API (OData), which also lets me practise extraction beyond manual downloads.
•Justification: It is an authoritative global source that gives context for India's position and enables trend analysis over time across regions and income groups.
•Limitations: Many values are modelled estimates, with coverage and update dates varying by indicator and country.
4.5 Summary comparison
Source	Level	Main use in project	Access
Diabetes 130-US Hospitals	Patient encounter	Readmission, length of stay, treatment factors	CSV (UCI)
Pima Indians Diabetes	Patient clinical	Risk factors for diabetes	CSV (UCI/Kaggle)
NFHS-5 India	State / district	Regional risk factor comparison	Fact sheets / DHS data
WHO GHO	Country / global	Trends and global context	CSV / API

4.6 Sources considered but not selected
•MIMIC-IV (ICU data): very rich, but requires credentialed access and training, so listed as future scope.
•CDC datasets (e.g. BRFSS, WONDER): valuable US population data; excluded to keep the project focused, and could extend the work later.
5. Research Questions and Hypotheses
Each question is tied to a metric and a data source so that every hypothesis can be tested with the data I plan to extract.
#	Research question	Hypothesis	Data source
RQ1	Which clinical factors (glucose, BMI, age, blood pressure, insulin) are most strongly associated with a diabetes diagnosis?	H1: Glucose and BMI show the strongest positive association with diabetes, and the proportion of diabetic patients rises with age.	Pima Indians Diabetes
RQ2	Is longer hospital stay or more prior inpatient visits associated with 30-day readmission?	H2: Patients with longer stays and more prior inpatient visits have a higher 30-day readmission rate.	Diabetes 130-US Hospitals
RQ3	Is HbA1c testing during admission, or a change in diabetes medication, associated with readmission?	H3: Patients who had an HbA1c test and a medication adjustment have lower readmission rates.	Diabetes 130-US Hospitals
RQ4	Does readmission risk differ by age group and gender?	H4: Older patients (60+) show higher readmission rates than younger groups.	Diabetes 130-US Hospitals
RQ5	How do elevated blood glucose and hypertension vary across Indian states, and how do they relate to overweight/obesity?	H5: States with higher overweight/obesity prevalence also show higher elevated blood glucose and hypertension prevalence.	NFHS-5
RQ6	How has NCD mortality changed over time across WHO regions and income groups, and where does India stand?	H6: Premature NCD mortality has declined more slowly in low- and middle-income settings than in high-income ones.	WHO GHO

Note: hypotheses are tested using statistical methods (e.g. chi-square tests, correlation, group comparisons) and reported as associations, not causal claims.
6. Methodology and Approach
6.1 Data extraction
•Download CSV files for the UCI datasets and NFHS-5 indicator tables; pull WHO GHO indicators through its API with Python.
•Store original files untouched in data/raw and record source URL, access date and licence in a data dictionary.
6.2 Data transformation and cleaning
•Profile each dataset: shape, data types, missing values, duplicates, outliers.
•Handle missing and invalid values (e.g. zeros in Pima clinical fields, '?' placeholders in the readmission data) with documented rules such as median imputation or exclusion.
•Standardise column names, categories and units; group age bands; create a binary 30-day readmission flag; map diagnosis codes to broader groups.
•Save cleaned outputs in data/processed with a short change log.
6.3 Analysis
•Exploratory data analysis: distributions, summary statistics, cross-tabulations.
•Statistical testing: correlation, chi-square and t-tests or non-parametric equivalents for each hypothesis.
•Optional modelling (if time allows): logistic regression for diabetes and readmission, used to rank risk factors rather than to claim prediction accuracy.
6.4 Visualization and reporting
•Charts in Python (matplotlib/seaborn) and a dashboard in Power BI or Tableau, e.g. readmission rate by age group, state-level choropleth for NFHS-5 indicators, NCD mortality trends.
•Final report with findings, limitations and recommendations.
6.5 Tools
Python (pandas, NumPy, SciPy, matplotlib, seaborn), SQL for querying and joins, Excel for quick checks, Power BI or Tableau for dashboards, Jupyter Notebook for analysis, and Git/GitHub for version control and documentation.
6.6 Data ethics and quality
•Only public, de-identified data is used; no attempt will be made to re-identify individuals.
•Licences and citations for every source are recorded in the repository.
•Limitations such as bias, missing data and age of data are stated alongside every finding.
7. Project Roadmap and Timeline
Week	Phase	Key activities	Deliverable
1	Planning and research	Research sources and metrics, define objectives, questions and hypotheses, set up GitHub repository	Project plan DOC, README, repo structure, GitHub issues
2	Data extraction	Download datasets, call WHO API, load into pandas, create data dictionary, initial data profiling	Raw data folder, extraction notebook, data dictionary
3	Cleaning and transformation	Handle missing values and outliers, standardise fields, engineer features (age bands, readmission flag), validate	Cleaned datasets, cleaning notebook, change log
4	Exploratory and statistical analysis	EDA, group comparisons, hypothesis tests for RQ1 to RQ6, optional logistic regression	Analysis notebook, results table (hypothesis supported or not)
5	Visualization	Build charts and an interactive dashboard, review for clarity	Visuals folder, dashboard file or screenshots
6	Insights and final report	Summarise findings, limitations and recommendations, polish repository and documentation	Final report, updated README, final GitHub release

Success checkpoints
•End of Week 2: all four datasets loaded and described in the data dictionary.
•End of Week 3: every dataset has a documented, reproducible cleaning script or notebook.
•End of Week 4: each hypothesis has a clear outcome backed by a test and a chart.
•End of Week 6: a reviewer can reproduce the work by following the README.
8. Risks and Mitigation
Risk	Mitigation
Dataset access delays or format changes	Download and archive raw copies early; keep alternative sources listed
Large amount of missing data in hospital dataset	Document handling rules, run sensitivity checks with and without imputed values
Small sample size (Pima)	Treat results as exploratory; avoid overgeneralising
Mismatched definitions across sources	Maintain a data dictionary and avoid combining sources without justification
Time constraints	Prioritise RQ1 to RQ3; treat modelling and extra sources as optional

9. Relevance to the Healthcare Data Analyst Intern Role
This plan mirrors the core responsibilities of a Healthcare Data Analyst Intern:
•Translating problems into analysis questions: broad health challenges are converted into measurable research questions and testable hypotheses.
•Working with healthcare metrics: readmission, length of stay, prevalence and mortality are standard measures used in hospital and public-health reporting.
•Data extraction and cleaning: the workflow covers files and APIs, and the handling of missing and inconsistent clinical data.
•Analysis and visualization: statistical testing and dashboards present insights for non-technical stakeholders.
•Documentation and version control: everything is recorded in a structured GitHub repository so the work is transparent and reproducible.
•Domain grounding: my bioengineering background supports interpreting clinical variables and understanding their meaning, not just their statistics.
10. Expected Outcomes
•A cleaned, documented set of datasets with a data dictionary.
•Evidence for or against each of the six hypotheses.
•A visual dashboard summarising risk factors, readmission patterns and regional burden.
•Practical recommendations, e.g. which patient groups may benefit from closer follow-up, and which regions may need targeted screening.
•A public GitHub repository that demonstrates my workflow end to end.
11. References
•UCI Machine Learning Repository: Diabetes 130-US Hospitals for Years 1999-2008 dataset. archive.ics.uci.edu
•Strack, B. et al. (2014). Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records. BioMed Research International.
•Smith, J.W. et al. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. Pima Indians Diabetes Database, via UCI/Kaggle.
•Ministry of Health and Family Welfare, Government of India; International Institute for Population Sciences. National Family Health Survey (NFHS-5), 2019-21. rchiips.org/nfhs
•World Health Organization. Global Health Observatory data repository. who.int/data/gho
•Data.gov.in: India Open Government Data Platform. data.gov.in
