# Healthcare Data Analysis Project

**Week 1: Healthcare Data Exploration & Requirement Planning**
Author: Priya Kailas Rakshe | B.Tech Bioengineering, MIT-ADT University

## Objective
Explore public healthcare datasets to understand diabetes risk factors, hospital readmission patterns and regional chronic-disease burden, and present the findings as clear, decision-ready insights.

## Data Sources
| Source | Level | Use in project |
|---|---|---|
| Diabetes 130-US Hospitals (UCI) | Patient encounter | Readmission, length of stay, treatment factors |
| Pima Indians Diabetes Database (UCI/Kaggle) | Patient clinical | Risk factors for diabetes |
| NFHS-5 India (2019-21) | State / district | Regional risk-factor comparison |
| WHO Global Health Observatory | Country / global | NCD mortality trends and global context |

Full justification for each source is in the project plan.

## Research Questions
1. Which clinical factors are most associated with diabetes?
2. Are longer stays or more prior inpatient visits associated with 30-day readmission?
3. Is HbA1c testing or a medication change associated with readmission?
4. Does readmission risk differ by age group and gender?
5. How do elevated blood glucose and hypertension vary across Indian states, and how do they relate to overweight/obesity?
6. How has NCD mortality changed across WHO regions and income groups, and where does India stand?

## Roadmap
| Week | Phase | Deliverable |
|---|---|---|
| 1 | Planning and research | Project plan, README, repo structure |
| 2 | Data extraction | Raw data, extraction notebook, data dictionary |
| 3 | Cleaning and transformation | Cleaned datasets, cleaning notebook |
| 4 | Analysis | Analysis notebook, hypothesis results |
| 5 | Visualization | Charts and dashboard |
| 6 | Insights and final report | Final report, polished repo |

## Project Plan
Full document: [Week 1 Project Plan](docs/Week1_Project_Plan.docx)

## Repository Structure
```
├── docs/          project plan and reports
├── data/
│   ├── raw/       original downloads (untouched)
│   └── processed/ cleaned data
├── notebooks/     Jupyter notebooks
├── scripts/       reusable Python/SQL scripts
└── visuals/       charts and dashboard files
```

## Tools
Python (pandas, NumPy, SciPy, matplotlib, seaborn), SQL, Excel, Power BI / Tableau, Jupyter, Git/GitHub

## Notes
Only public, de-identified data is used. Findings are reported as associations, not causal claims.
