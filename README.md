# Student GPA Prediction

**Predict student GPA (0–10)** using academic, behavioral, and support-related factors.

## 🚀 Live Demo

<p align="center">
  <a href="https://student-performance-prediction-chkq.onrender.com/" target="_blank">
    <img src="https://github.com/user-attachments/assets/3af77a17-de12-4e4a-a442-2e1950942257" 
         alt="Preview of the Student GPA Prediction website" 
         width="600" />
  </a>
</p>

<h3 align="center">
  <a href="https://student-performance-prediction-chkq.onrender.com/" target="_blank">
    🌎 <b>Visit the Live Site</b> 🚀
  </a>
</h3>


<br>

## 📌 Overview

This project applies **Machine Learning** to predict a student's GPA based on multiple features such as study time, absences, parental education, extracurricular activities, and more. It includes:

* A well-documented **Jupyter Notebook** with a complete workflow (data cleaning → EDA → modeling → evaluation → saving the model).
* A trained **Random Forest model** saved as a pickle file (`model/model.pkl`).
* A **Django web app** to serve predictions via a simple web interface.

## 🎯 Objectives

* Understand how academic, behavioral, and parental factors affect GPA.
* Train and compare multiple ML models (Linear Regression, Decision Tree, Random Forest).
* Evaluate models with **R², MAE, RMSE** to select the best one.
* Deploy the final model in a web application for real-time GPA prediction.

## 📊 Key Insights from EDA

* **Absences** have the strongest negative impact on GPA (correlation ≈ -0.88).
* **Parental Support**, **Study Time**, and **Tutoring** show positive correlations with GPA.
* Extracurricular participation also shows mild positive effects.

## 🤖 Model Performance

Three models were trained and compared:

| Model             | R² (Test) | MAE  | RMSE |
| ----------------- | --------- | ---- | ---- |
| **Random Forest** | ~0.89    | 0.37 | 0.55 |
| Linear Regression | ~0.89    | 0.39 | 0.56 |
| Decision Tree     | ~0.81    | 0.52 | 0.73 |

➡️ **Random Forest** achieved the best balance of accuracy and error and was selected as the final model.

## ⚙️ How to Use

### 1. Run the Notebook

* Open `Student_Performance_ML.ipynb` in Jupyter or Google Colab.
* Execute all cells to reproduce the data cleaning, EDA, training, and evaluation.
* The trained model will be saved as `model/model.pkl`.

### 2. Run the Django App Locally

* Clone the repository: `git clone https://github.com/Divyansh2905/Student_Performance_Prediction.git`
* Install dependencies from `requirements-dev.txt`: `pip install -r requirements-dev.txt`
* Navigate into the project directory.
* Run the Django server: `python manage.py runserver`
* Go to `http://127.0.0.1:8000/` to use the prediction tool.

## 🌐 Deployment

The application is deployed on **Render** using a `gunicorn` web server. The platform automatically handles the installation of all dependencies from `requirements.txt` and serves the app from a live URL.

---
