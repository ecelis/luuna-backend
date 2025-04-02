from rest_framework import permissions, viewsets

from ..models.product import Product
from ..serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoints to manage products.

    Provides CRUD operations and is restricted for writes to admin users,
    anonymous users can list the products"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
