from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('update_profile', views.update_profile)
]
