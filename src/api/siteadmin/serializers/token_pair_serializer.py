from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JSON Web Token serializer"""

    def validate(self, attrs):
        """Validate the user login and if successful add basic claims to the token.

        Return dict
        """
        data = super().validate(attrs)
        if self.user:
            data["user_id"] = self.user.id
            data["username"] = self.user.username
            data["is_staff"] = self.user.is_staff

        return data

    @classmethod
    def get_token(cls, user):
        """Class method that returns a customized JSON Web Token"""
        token = super().get_token(user)

        return token
