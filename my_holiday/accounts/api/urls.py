from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login_api"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_create"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_create"),
]