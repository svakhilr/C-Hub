from django.utils import  timezone
from django.db import models

class PaymentManager(models.Manager):
    def create(self, **kwargs):
        payment = super().create(**kwargs)
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        payment_id = f"IN{payment.id}{timestamp}"
        payment.payment_id= payment_id
        payment.save()
        return payment