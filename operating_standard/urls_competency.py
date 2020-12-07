from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views_competency

urlpatterns = [
    # Nasional 
    path('', views_competency.index_nasional),
    path('input/', views_competency.input_nasional, name='input'),
    # path('<id>/', views_competency.detail_nasional),
    # path('<id>/update', views_competency.update_nasional),
    # path('<id>/delete/', views_competency.delete_nasional),
]