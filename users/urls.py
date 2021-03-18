from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('update_profile/', views.update_profile)
]
