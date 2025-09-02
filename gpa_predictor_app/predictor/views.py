import numpy as np
import pandas as pd
import pickle
import os
from django.shortcuts import render
from django.conf import settings
from django.apps import apps

def predict_gpa(request):
    prediction = None
    error_message = None

    if request.method == 'POST':
        try:
            # 1. Load the model directly within the function
            predictor_app_config = apps.get_app_config('predictor')
            model = predictor_app_config.model
            if model is None:
                raise RuntimeError("Model not loaded. Check predictor.apps.PredictorConfig.ready()")

            # 2. Get and validate all form data
            age = float(request.POST.get('age'))
            gender = int(request.POST.get('gender'))
            parentaleducation = int(request.POST.get('parentaleducation'))
            study_time = float(request.POST.get('study_time'))
            absences = int(request.POST.get('absences'))
            tutoring = int(request.POST.get('tutoring'))
            parental_support = int(request.POST.get('parental_support'))
            extracurricular = int(request.POST.get('extracurricular'))
            sports = int(request.POST.get('sports'))
            music = int(request.POST.get('music'))
            volunteering = int(request.POST.get('volunteering'))

            # 3. Perform server-side validation on specific fields
            if not (0 <= parentaleducation <= 4):
                error_message = "Parental Education must be between 0 and 4."
            elif not (0 <= parental_support <= 4):
                error_message = "Parental Support must be between 0 and 4."
            elif not (gender in [0, 1]):
                error_message = "Gender must be 0 or 1."
            # You can add more validation here if needed, e.g., for age, absences, etc.

            if not error_message:
                # 4. If validation passes, prepare data and make a prediction
                data = np.array([[
                    age, gender, parentaleducation, study_time, absences, tutoring,
                    parental_support, extracurricular, sports, music, volunteering
                ]])
                
                column_names = [
                    'Age', 'Gender', 'ParentalEducation', 'StudyTimeWeekly', 'Absences',
                    'Tutoring', 'ParentalSupport', 'Extracurricular', 'Sports',
                    'Music', 'Volunteering'
                ]
                df = pd.DataFrame(data, columns=column_names)

                predicted_gpa = model.predict(df)[0]
                prediction = f'{predicted_gpa:.2f}'

        except FileNotFoundError:
            error_message = "The machine learning model could not be loaded. Please ensure 'model.pkl' is in the 'predictor' directory."
        except Exception as e:
            error_message = f"An error occurred: {e}"

    # 5. Render the template with the result or error message
    return render(request, 'predictor/index.html', {'prediction': prediction, 'error_message': error_message})
