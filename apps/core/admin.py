from django.contrib import admin
from .models import Category, JobApplication, job, Contact

# Register your models here.
admin.site.register(Category)
admin.site.register(JobApplication)
admin.site.register(job)
admin.site.register(Contact)
