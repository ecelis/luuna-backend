from http import HTTPStatus

from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

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

    def partial_update(self, request, *args, **kwargs):
        """Update an user

        Returns:
            Response: Updated user data or error details.
        """

        instance = self.get_object()

        try:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)

            self.perform_update(serializer)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValidationError as error:
            if type(error) is ValidationError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=error.detail)
        except Exception:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"error": HTTPStatus.INTERNAL_SERVER_ERROR.phrase},
            )

    def perform_update(self, serializer):
        instance = serializer.save()

        return instance
