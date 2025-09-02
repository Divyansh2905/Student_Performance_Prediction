from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_gpa, name='predict_gpa'),
]