from django.db import models

from users.models import CompanyProfile,CustomerProfile



class Order(models.Model):
    
    customer_name = models.CharField(max_length=50)
    customer = models.ForeignKey(CustomerProfile,on_delete=models.SET_NULL,null=True,blank=True)
    order_id      = models.CharField(max_length=50,blank=True,null=True)
    item_total    = models.DecimalField(max_digits=10,decimal_places =2)
    discount      = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total   = models.DecimalField(max_digits=10, decimal_places=2)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.customer_name}"
    
class OrderItem(models.Model):

    PENDING  =  'Pending'
    PLACED   = 'Placed'
    ACCEPTED = 'Accepted'
    REJECTED  = 'Rejected'
    CANCELLED = 'Cancelled'
    DELIVERED = 'Delivered'

    ORDER_STATUS =(
        ("Pending",PENDING),
        ("Accepted",ACCEPTED),
        ("Rejected",REJECTED),
        ("Cancelled",CANCELLED),
        ("Delivered",DELIVERED)
    )

    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    company       = models.ForeignKey(CompanyProfile,
        on_delete=models.SET_NULL,
        null=True,blank=True,
        related_name = 'order_item')
    product_name = models.CharField(max_length=60)
    product_image = models.ImageField(upload_to='orders/product',blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=25,choices=ORDER_STATUS,default=PENDING)

    def __str__(self):
        return self.product_name
    
    @property
    def total_price(self):
        return self.price*self.quantity
    
class OrderAddress(models.Model):
    order        = models.OneToOneField(Order,
        on_delete=models.CASCADE,
        related_name='order_address')
    house_number = models.CharField(max_length=20)
    address      = models.TextField(blank=True,null=True)
    city         = models.CharField(max_length=20,null=True)
    state        = models.CharField(max_length=20)
    land_mark    = models.CharField(max_length =100, blank=True,null=True)
    pincode     = models.IntegerField()

    def __str__(self):
        return self.order.customer_name



    
