from rest_framework import serializers

from ..models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    class Meta:
        model = Product
        fields = ["id", "sku", "name", "price", "brand", "created_at", "updated_at"]
        extra_kwargs = {
            "created_at": {"read_only": True, "required": False},
            "updated_at": {"read_only": True, "required": False},
        }
