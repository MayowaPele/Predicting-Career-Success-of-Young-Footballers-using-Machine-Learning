## ⚽ Predicting the Success and Position of Young Soccer Players Using Machine Learning
### 📌 Project Overview

This project uses machine learning to predict the overall rating of young soccer players (ages 17–20) based on their technical, physical, and mental attributes.
By leveraging FIFA/Football Manager-style datasets, the project applies feature selection, regression models, and a Streamlit web app to provide scouting and training insights.

### 🎯 Objectives

- Predict the overall rating of youth players using multiple ML models.

- Identify the most important attributes that influence player ratings.

- Build an interactive Streamlit app to test predictions with new data.

- Ensure compliance with ethical standards (privacy, fairness, and safeguarding minors).

### 📊 Dataset

- Source: FIFA/FM exports and Kaggle datasets (publicly available).
- Target variable: Overall rating.
- Key attributes include:

  - Technical: ball control, dribbling, short passing

  -  Mental: vision, composure, reactions

  -  Physical: pace, strength, agility

-  Players aged 17–20 only.
-  Missing values imputed using group mean by overall rating.

### 🛠️ Methodology

1. Data Preprocessing

  -  Removed irrelevant columns (tags, traits, clubs, player names, jersey numbers).
  -  Imputed missing values by group mean
  -  Encoded categorical variables with LabelEncoder.

2.  Feature Selection

  -  Applied SelectKBest(f_regression) to choose top 15 features.
  -  Features ranked by importance (e.g., composure, ball control, vision).

3.  Model Development

-  Models trained:

  -  Linear Regression
  -  Decision Tree Regressor
  -  Random Forest Regressor

-  Train/test split: 80/20.

4.  Evaluation

  -  Metrics: Mean Squared Error (MSE), R² Score.
  -  Random Forest achieved best performance (R² ≈ 0.93).

5.  Deployment

  -  Built a Streamlit app for real-time predictions.
  -  Users can input attributes manually or upload CSV files.


### 📈 Results

|Model |	R² Score |	MSE
|------| ----------|------|
|Linear Regression |	0.70 |	18.4 |
|Decision Tree |	0.81 |	11.2 |
|Random Forest |	0.85 |	9.6 |

🎯 Random Forest outperformed others.

🎯 Mental and technical attributes (composure, vision, ball control, reactions) are stronger predictors than physical stats.


### 🚀 How to Run the Project
#### 🔧 Requirements

Install dependencies:
```
pip install streamlit
pip install joblib
pip install sklearn
```

### ▶️ Run the Streamlit App
```
streamlit run app.py
```

### 📂 Project Structure
```
├── data/
│   └── filtered_young_players.csv   # Processed dataset
├── notebooks/
│   └── model_training.ipynb         # Jupyter notebook for experiments
├── app.py                           # Streamlit app
├── overall_rating_model.pkl         # Saved trained model
├── selected_features.pkl            # Selected features list
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation
```

### 🔮 Future Work

-  Position-specific models. Predicting ratings by pitch positions.
-  Incorporating time-series player progression data.
-  Adding explainability tools (SHAP/LIME).
-  Integration with scouting dashboards.
