# Student GPA Prediction

**Predict student GPA (0–10)** using academic, behavioral, and support-related factors.

## 📌 Overview

This project applies **Machine Learning** to predict a student's GPA based on multiple features such as study time, absences, parental education, extracurricular activities, and more. The project includes:

* A well-documented **Jupyter Notebook** with complete workflow (data cleaning → EDA → modeling → evaluation → saving model).
* A trained **Random Forest model** saved with Pickle.
* A small **Django web app** to serve predictions via a simple web interface.

## 🎯 Objectives

* Understand how academic, behavioral, and parental factors affect GPA.
* Train and compare multiple ML models (Linear Regression, Decision Tree, Random Forest).
* Evaluate models with **R², MAE, RMSE** and choose the best one.
* Deploy the best model in a Django web app for real-time GPA prediction.

## 📊 Key Insights from EDA

* **Absences** have the strongest negative impact on GPA (correlation ≈ -0.88).
* **Parental Support**, **Study Time**, and **Tutoring** show positive correlations with GPA.
* Extracurricular participation also shows mild positive effects.

## 🤖 Model Performance

Three models were trained and compared:

| Model             | R² (Test) | MAE  | RMSE |
| ----------------- | --------- | ---- | ---- |
| **Random Forest** | \~0.89    | 0.37 | 0.55 |
| Linear Regression | \~0.89    | 0.39 | 0.56 |
| Decision Tree     | \~0.81    | 0.52 | 0.73 |

➡️ **Random Forest** achieved the best balance of accuracy and error, and was selected as the final model.

## ⚙️ How to Use

### 1. Run the Notebook

* Open `Student_Performance_ML.ipynb` in Jupyter/Colab.
* Execute all cells to reproduce cleaning, EDA, training, and evaluation.
* The trained model will be saved as `model/model.pkl`.
* Paste that model in the `gpa_predictor_app/predictor` folder.

### 2. Run the Django App

* Ensure dependencies are installed (see `requirements.txt`).
* Run the Django server:

  ```bash
  python manage.py runserver
  ```
* Go to `http://127.0.0.1:8000/` to enter student details and get GPA prediction.

## 🔮 Future Improvements

* Add **hyperparameter tuning** for further accuracy.
* Integrate **SHAP / permutation importance** for explainable predictions.
* Improve UI/UX of the Django app.
* Expand dataset to include more diverse student factors.

