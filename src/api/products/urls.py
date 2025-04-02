from django.urls import include, path
from rest_framework import routers

from .views.brand_view_set import BrandViewSet
from .views.product_view_set import ProductViewSet

router = routers.DefaultRouter()
router.register("brand", BrandViewSet)
router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
