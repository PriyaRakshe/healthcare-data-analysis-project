# Life Expectancy Analysis: WHO, UN and World Bank Health Data

Which factors explain differences in national life expectancy between 2000 and 2015?

**Author:** Priya Kailas Rakshe | B.Tech Bioengineering, MIT School of Bioengineering Sciences & Research, MIT-ADT University

## Objective
Integrate public WHO/UN and World Bank health data, then answer three questions:
1. How has life expectancy changed, and is the gap between developed and developing countries closing?
2. Which factors are most associated with life expectancy?
3. Which countries share similar health profiles?

The results are turned into recommendations for a hypothetical national health improvement programme.

## Key findings
- Data covers 183 countries (193 in the raw data) and 2,928 country-year records after cleaning; 99% of rows matched the World Bank indicators.
- Mean life expectancy rose from 66.8 to 71.6 years. The developed-developing gap narrowed from 12.2 to 11.0 years but remains significant (95% CI 9.3-12.7 years).
- Linear regression (test R-squared 0.84): HIV/AIDS has the strongest negative association and GDP per capita the strongest positive one.
- Random forest (test R-squared 0.96): top predictors are HIV/AIDS, health spending and adult mortality.
- K-means clustering (k = 4, silhouette 0.37) groups countries into four health profiles.

## Methods
- **Extract:** WHO/UN life expectancy panel (Kaggle) and World Bank WDI indicators through the World Bank API
- **Clean:** duplicate and plausibility checks, within-country interpolation, group-median imputation, imputation flags
- **Integrate:** join on ISO3 country code and year
- **Analyse:** trend analysis and Welch t-test, OLS regression with VIF check, random forest, K-means with PCA
- **Tools:** Python (pandas, NumPy, SciPy, statsmodels, scikit-learn, matplotlib, seaborn)

## Repository structure
```
├── data/
│   ├── raw/         original Life Expectancy Data.csv
│   ├── interim/     World Bank download and country-code crosswalk
│   └── processed/   analysis-ready dataset (health_integrated.csv)
├── scripts/         healthcare_pipeline.py (full pipeline)
├── visuals/         charts produced by the pipeline
└── docs/            Week 1-4 reports, results and profiling tables
```

## How to run
```
pip install -r requirements.txt
python scripts/healthcare_pipeline.py
```
Run it from the repository root. Results are written to `docs/` and charts to `visuals/`.
Cluster numbering and sizes can vary slightly between library versions.

## Reports
- [Week 1 project plan](docs/Week1_Project_Plan.docx)
- [Week 2 data extraction, cleaning and integration](docs/Week2_Data_Extraction_Cleaning_Integration.docx)
- [Week 3 analysis and visualization plan](docs/Week3_Data_Analysis_and_Visualization_Plan.docx)
- [Week 4 final report and recommendations](docs/Week4_Final_Evaluation_Report.docx)

## Data sources
- Life Expectancy (WHO) dataset, Kaggle
- World Bank World Development Indicators (health expenditure, physicians, hospital beds, population aged 65+, GDP per capita, population)

## Limitations
Findings are country-level associations, not causal claims. Public, de-identified data only.
