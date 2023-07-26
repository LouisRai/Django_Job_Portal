from django.db import models

from apps.commons.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

class job(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name = "category_jobs")
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class JobApplication(BaseModel):
    status_choices = [
        ("APPLIED", "Applied"),
        ("SCREENING" , "Screening"),
        ("SELECTED" , "Selected"),
        ("SHORT_LISTED" , "Short Listed"),
        ("REJECTED" , "Rejected")
    ]

    job = models.ForeignKey(job, on_delete=models.CASCADE, related_name = "job_applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "job_applications")
    interview_date = models.DateTimeField(null = True, blank = True)
    status = models.CharField(choices = status_choices, max_length=20)



class Contact(BaseModel):
    mane = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    message = models.TextField(max_length=1000)
    


    
    