# Life Expectancy Analysis: WHO, UN and World Bank Data

Which factors explain differences in national life expectancy (2000–2015)?
Author: Priya Kailas Rakshe | B.Tech Bioengineering, MIT-ADT University

## Summary
- 193 countries, 2,928 country-year records after cleaning
- Mean life expectancy rose from 66.8 to 71.6 years; the developed–developing gap narrowed from 12.2 to 11.0 years (95% CI 9.3–12.7)
- Regression (test R² 0.84): HIV/AIDS has the strongest negative association, GDP per capita the strongest positive
- Random forest top predictors: HIV/AIDS, health spending, adult mortality
- K-means (k=4) grouped countries into four health profiles

## Methods
Python (pandas, NumPy, SciPy, statsmodels, scikit-learn, seaborn), World Bank API, ISO3 country matching, interpolation and imputation flags, Welch t-test, OLS with VIF check, random forest, K-means with PCA.

## Repository
- scripts/healthcare_pipeline.py – full pipeline
- docs/ – Week 1–4 reports and result tables
- visuals/ – charts

## Limitations
Country-level associations, not causal claims.
