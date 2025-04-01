from django.db import models

from .base_model import BaseModel
from .product_brand import ProductBrand


class Product(BaseModel):
    sku = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    brand = models.ForeignKey(ProductBrand, on_delete=models.RESTRICT)
