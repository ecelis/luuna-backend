from rest_framework import serializers

from ..models.brand import Brand


class BrandSerializer(serializers.ModelSerializer):
    """Brand serializer"""

    class Meta:
        model = Brand
        fields = ["name", "created_at", "updated_at"]
        extra_kwargs = {
            "created_at": {"read_only": True, "required": False},
            "updated_at": {"read_only": True, "required": False},
        }
