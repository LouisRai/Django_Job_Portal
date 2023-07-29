from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.commons.utils import get_base_url, is_profile_complete
from .models import Category, job, JobApplication
from .pagination import CustomPagination
# Create your views here.

class HomeView(ListView):
    template_name = 'core/home.html'
    pagination_class = CustomPagination

    def get_pagination(self):
        return self.pagination_class()

    def get_queryset(self):
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        job_filter = {"is_active": True}
        exclude = dict()
        if self.request.user.is_authenticated:
            exclude = {"job_applications__user": self.request.user}
        if category:
            job_filter.update(category__uuid=category)
        if search:
            job_filter.update(title__icontains=search)
        return job.objects.filter(**job_filter).exclude(**exclude).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        pagination = self.get_pagination()
        qs = pagination.get_paginated_qs(view=self)
        paginated_qs = pagination.get_nested_pagination(qs, nested_size=2)
        context['job_lists'] = paginated_qs
        context['categories'] = Category.objects.all()
        page_number, page_str = pagination.get_current_page(view=self)
        context[page_str] = 'active'
        context["next_page"] = page_number + 1
        context["prev_page"] = page_number - 1
        context['base_url'] = get_base_url(request=self.request)
        if page_number >= pagination.get_last_page(view=self):
            context["next"] = "disabled"
        if page_number <= 1:
            context["prev"] = "disabled"
        context['home_active'] = 'active'
        return context
            
    
        
        return context
    
class JobDetailView(DetailView):
    template_name = "core/job_detail.html"
    queryset = job.objects.filter(is_active = True)
    slug_field = "uuid"
    slug_url_kwarg = "uuid"
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "Job Details"
        return context

@login_required
def job_apply(request, uuid):
    try:
        job = job.objects.get(uuid=uuid)
    except:
        messages.error(request, "Something went wrong!!")
        return redirect('hone')
    
    if is_profile_complete(request.user):
        JobApplication.objects.get_or_create(user=request.user, job=job, defaults={"status":"APPLIED"})
        messages.success(request, "You Have Successfully Applied For The Role Of {job.title}")
        return redirect('home')
    messages.error(request, "Please Actuvate You Account and Complete Your Profile")
    return redirect('home')