from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.token_pair_serializer import CustomTokenObtainPairSerializer


@method_decorator(csrf_exempt, name="dispatch")
class CustomTokenObtainPairView(TokenObtainPairView):
    """API endpoint that returns a JSON Web Token with"""

    serializer_class = CustomTokenObtainPairSerializer
