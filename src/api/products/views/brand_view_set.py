from rest_framework import permissions, viewsets

from ..models.brand import Brand
from ..serializers.brand_serializer import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """API endpoints to manage product brands.

    Provides CRUD operations and is restricted for writes to admin users,
    anonymous users can list the products"""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticatedOrReadOnly,
    ]
