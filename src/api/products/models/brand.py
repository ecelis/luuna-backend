from django.db import models

from .base_model import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=255, unique=True)
