from django.contrib import admin
from django.urls import path, include
from .views import HomeView,JobDetailView

urlpatterns = [
    path('job-detail/<str:uuid>', JobDetailView.as_view(), name = "job_detail"),
    path('', HomeView.as_view(), name = "home"),
]
