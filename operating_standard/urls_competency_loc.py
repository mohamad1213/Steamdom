from django.shortcuts import render
from django.contrib import admin
from django.urls import path

from . import views_competency

urlpatterns = [
    # Local
    path('', views_competency.index_local),
    path('input/', views_competency.input_local),
    # path('<id>/', views_competency.detail_local),
    # # path('<id>/update', views_competency.update_local),
    # path('<id>/delete/', views_competency.delete_local),

]