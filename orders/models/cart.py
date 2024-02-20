from django.db import models

from users.models import CustomerProfile
from products.models import Product


class Cart(models.Model):
    customer = models.OneToOneField(CustomerProfile,
        on_delete= models.CASCADE,
        related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.name
    
    @property
    def grand_total(self):
        total = 0
        try:
            cart_items = self.cart_item.all()
            for cart_item in cart_items:
                total+=cart_item.product.price*cart_item.quantity
            return total
        except:
            return total
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,
        on_delete=models.CASCADE,
        related_name='cart_item')
    product = models.ForeignKey(Product,
        on_delete=models.CASCADE,
        related_name='cart_item')
    quantity = models.IntegerField()
    purchased_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cart}-----{self.product}"

