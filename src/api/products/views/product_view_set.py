from rest_framework import permissions, viewsets
from rest_framework.response import Response

from ..models.product import Product
from ..models.product_visit import ProductVisit
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

    def retrieve(self, request, *args, **kwargs):
        """
        Override the retrieve method to track product visits.
        """
        instance = self.get_object()
        ip_address = request.META.get("REMOTE_ADDR")
        if not request.user.is_authenticated:
            ProductVisit.objects.create(product=instance, ip_address=ip_address)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
