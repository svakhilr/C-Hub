from orders.models import Cart
from users.models import CustomerProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CustomerProfile)
def create_documents(sender, instance, created, **kwargs):
    print("signal")
    if created:
        Cart.objects.create(customer=instance)