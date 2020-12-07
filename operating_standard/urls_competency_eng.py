from django.shortcuts import render
from django.urls import path

from . import views_competency

urlpatterns = [
    path('', views_competency.index_internasional),
    path('input/', views_competency.input_international),
    # path('<id>/', views_competency.detail_internasional),
    # path('<id>/update', views_competency.update_internasional),
    # path('<id>/delete/', views_competency.delete_internasional),


]