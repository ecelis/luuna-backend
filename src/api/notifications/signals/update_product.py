import os

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models.product import Product

from ..email.email_service import EmailService


@receiver(post_save, sender=Product)
def save_product(sender, instance, **kwargs):
    if sender is Product:
        content = f"{instance.id} - {instance.name} - {instance.price} was updated at {instance.updated_at}"
        staff_emails = User.objects.filter(is_staff=True).values_list(
            "email", flat=True
        )
        payload = {"user_email": ",".join(staff_emails)}
        email_service = EmailService(payload, channel=os.getenv("EMAIL_CHANNEL", None))
        mailer = email_service.get_mailer()
        mailer.send_email(subject="Product updated", content=content)
