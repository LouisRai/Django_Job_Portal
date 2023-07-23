import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.commons.models import BaseModel


class User(AbstractUser):
    username = models.CharField(default=uuid.uuid4, max_length=100, blank=True, unique=True)
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    account_activated = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def get_full_name(self) -> str:
        return super().get_full_name()

    def __str__(self):
        return self.get_full_name if self.get_full_name else self.email


class UserAccountActivationKey(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_activation_keys")
    key = models.CharField(max_length=50)

class UserProfile(BaseModel):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    about_me = models.CharField(max_length=1000)
    profile_picture = models.FileField(null=True, blank=True, upload_to='profile_pictures')
    resume = models.FileField(null=True, blank=True, upload_to='resume')

    def __str__(self):
        return f'Profule of {self.user.email}'
    
