from django.urls import include, path
from rest_framework import routers

from .views.brand_view_set import BrandViewSet

router = routers.DefaultRouter()
router.register("brand", BrandViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
