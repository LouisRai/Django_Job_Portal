from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import job
from .pagination import CustomPagination
# Create your views here.

class HomeView(ListView):
    template_name = 'core/home.html'
    pagination_class = CustomPagination
    queryset = job.objects.filter(is_active = True)

    def get_pagination(self):
        return self.pagination_class()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        pagination = self.get_pagination()
        qs = pagination.get_paginated_qs(view = self)
        nested_qs = pagination.get_nested_pagination(qs, nested_size=2)

        context["Title"] = "Home"
        
        context["jobs_list"] = nested_qs

        return context