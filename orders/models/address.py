from django.db import models

from users.models import CustomerProfile


class Address(models.Model):
    customer     = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    house_number = models.CharField(max_length=20)
    address      = models.TextField(null=True)
    city         = models.CharField(max_length=20,null=True)
    state        = models.CharField(max_length=20)
    land_mark    = models.CharField(max_length =100, blank=True,null=True)
    pincode     = models.IntegerField()

    def __str__(self):
        return f"Address of {self.customer.name}"
    
    def copy_to_order_address(self,order):
        from ..models import OrderAddress
        
        OrderAddress.objects.create(order=order,
            house_number = self.house_number,
            address = self.address,
            city = self.city,
            state = self.state,
            land_mark=self.land_mark,
            pincode=self.pincode)