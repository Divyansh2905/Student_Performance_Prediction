import os
import pickle
from django.apps import AppConfig
from django.conf import settings

class PredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictor'
    model = None

    def ready(self):
        # The ready() method is called exactly once when the app is loaded.
        # This is the ideal place to load the machine learning model.
        # It prevents the model from being reloaded on every single request.
        
        # Construct the path to the model file
        model_path = os.path.join(settings.BASE_DIR, 'predictor', 'model.pkl')
        
        try:
            # Open and load the model file in binary read mode
            with open(model_path, 'rb') as model_file:
                self.model = pickle.load(model_file)
            print("Successfully loaded the machine learning model.")
        except FileNotFoundError:
            print(f"Error: The model file was not found at {model_path}")
        except Exception as e:
            print(f"Error loading the machine learning model: {e}")
