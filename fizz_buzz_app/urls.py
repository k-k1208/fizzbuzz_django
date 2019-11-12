from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.numform, name='form'),
    path('result/', views.result, name='result')
]
