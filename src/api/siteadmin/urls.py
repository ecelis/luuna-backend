from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from .views.auth import CustomTokenObtainPairView
from .views.user import User

router = routers.DefaultRouter()
router.register(r"user", User)

urlpatterns = [
    path("", include(router.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
