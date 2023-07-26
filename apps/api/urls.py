from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserProfileAPIView,
    UserProfileUpdateAPIView,
)

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="api_user_register"),
    path("login/", UserLoginAPIView.as_view(), name="api_user_login"),
    path("logout/", UserLogoutAPIView.as_view(), name="api_user_logout"),
    path("profile/", UserProfileAPIView.as_view(), name="api_user_profile"),
    path("profile/update/", UserProfileUpdateAPIView.as_view(), name="api_user_profile_update"),
]
