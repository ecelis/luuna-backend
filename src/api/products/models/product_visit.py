from django.db import models

from products.models.product import Product


class ProductVisit(models.Model):
    """
    Model to track visits to individual product detail pages.
    """

    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT, related_name="visits"
    )
    visit_timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"Visit to {self.product.name} at {self.visit_timestamp} from {self.ip_address.__str__()}"
