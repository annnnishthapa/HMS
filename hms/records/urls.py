from django.urls import path

from records import views

app_name = 'records'

urlpatterns = [
    path('', views.medical_history_list, name='medical_history_list'),
    path('medical-history/', views.medical_history_form, name='medical_history_form'),
]
