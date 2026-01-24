from django.contrib import admin
from django.urls import path
from . import views

app_name = 'opinions'

urlpatterns = [
    path('all/', views.viewOpinions, name='allOpinions'),
]
