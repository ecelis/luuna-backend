import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models.product import Product

from ..email.email_service import EmailService


@receiver(post_save, sender=Product)
def save_product(sender, instance, **kwargs):
    content = f"{instance.id} - {instance.name} - {instance.price} was updated at {instance.updated_at}"
    if sender is Product:
        payload = {"user_email": "empleado2@gosoftlive.com"}
        email_service = EmailService(payload, channel=os.getenv("EMAIL_CHANNEL", None))
        mailer = email_service.get_mailer()
        mailer.send_email(subject="Prueba", content=content)
