from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views_teacher

urlpatterns = [
    path('', views_teacher.index),
    path('input/', views_teacher.input),
    path('<id>/', views_teacher.detail),
    path('<id>/delete/', views_teacher.delete),
    # path('<id>/update/', views_teacher.update),
]