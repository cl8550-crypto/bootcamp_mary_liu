# Titanic Data Project

## Project Summary
We will predict passenger survival on the Titanic using basic demographic and travel information. This small project demonstrates a reproducible data pipeline—from raw data to cleaned data—so it can be adapted to real-world safety/risk questions.

## Stakeholder Persona
Primary stakeholder: a shipping-company safety officer who wants to identify higher-risk passenger groups to guide safety planning, evacuation procedures, and resource allocation.

## Repo Structure
- /data/ — all datasets
- /data/raw/ — raw data (downloaded/ingested)
- /data/processed/ — saved processed datasets
- /notebooks/ — demo/analysis notebooks
- /src/ — Python scripts (utils, cleaning)
- /docs/ — documentation and memos

## Preprocessing Assumptions
- Missing Age filled with dataset median.
- Sex encoded as 0/1 for simple downstream modeling.
- Cleaned dataset saved to `data/processed/titanic_clean.csv`.

## Outlier Assumptions
- Defined outliers using the IQR rule (k=1.5).
- Age outliers flagged; sensitivity analysis showed survival rates are similar with/without them.
- Risk: removing outliers may remove valid extreme passengers.

## Full EDA
- Produced histograms, boxplots, and correlation heatmap.
- Found clear survival differences by sex and passenger class.
- Age has outliers but median imputation helps.

## Features
- FamilySize = SibSp + Parch + 1
- IsAlone = 1 if passenger has no family aboard
- Title extracted from Name (Mr, Mrs, Miss, etc.)

## Modeling
- Logistic Regression on Titanic survival.
- Features: Pclass, Sex, Age, Fare, FamilySize, IsAlone.
- Accuracy around ~80% on test set.

## Evaluation & Risks
- Model accuracy ~80%, bootstrap CI around [X, Y].
- Risks: Age imputation may bias; model assumes linear log-odds.
- Removing Age outliers didn’t change results much.

## Productization
- Saved logistic regression model in /model/logreg.pkl
- Simple Flask API in app.py: send JSON POST to /predict
- Example: {"Pclass":3,"Sex":0,"Age":22,"Fare":7.25,"FamilySize":1,"IsAlone":1}
