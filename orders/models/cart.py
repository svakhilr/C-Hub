from django.db import models

from users.models import CustomerProfile
from products.models import Product


from django.utils import timezone


class Cart(models.Model):
    customer = models.OneToOneField(CustomerProfile,
        on_delete= models.CASCADE,
        related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.name
    
    @property
    def cart_total(self):
        total = 0
        try:
            cart_items = self.cart_item.all()
            for cart_item in cart_items:
                total+=cart_item.product.price*cart_item.quantity
            return total
        except:
            return total

    @property    
    def discount(self):
        discount = 0
        return discount
    
    @property
    def grand_total(self):
        return self.cart_total-self.discount
    
    def place_order(self):
        from orders.models import Order,OrderItem
        order = Order.objects.create(
            customer_name = self.customer.name,
            customer      =self.customer,
            item_total    = self.cart_total,
            discount      = self.discount,
            grand_total   = self.grand_total
        )
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        order_id = f"IN{order.id}{timestamp}"
        order.order_id=order_id
        order.save()
        cart_items = self.cart_item.all()
        for cart_item in cart_items:
            OrderItem.objects.create(
                order = order,
                product_name = cart_item.product.name,
                price = cart_item.product.price,
                quantity = cart_item.quantity,
                product_image= cart_item.product.image,
                company = cart_item.product.company
            )
        self.clear_cart()
        
        return order
    
    def clear_cart(self):
        self.cart_item.all().delete()
    

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
    
    @property
    def cart_item_total(self):
        return self.product.price*self.quantity

