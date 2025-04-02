from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from ..serializers.user_serializer import UserSerializer


class User(viewsets.ModelViewSet):
    """API endpoints for managing user accounts.

    This viewset provides CRUD operations for User objects with permission-based access control.
    Only staff users can access this operations

    Attributes:
        serializer_class: Serializer class for User model using UserSerializer"
    """

    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
