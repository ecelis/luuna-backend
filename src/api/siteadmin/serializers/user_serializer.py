from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "password", "is_active"]
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        Hash the password if it's included in the validated data.
        """
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        # instance.save()

        return super().update(instance, validated_data)
