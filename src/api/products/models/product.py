from django.db import models

from .base_model import BaseModel
from .brand import Brand


class Product(BaseModel):
    sku = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
