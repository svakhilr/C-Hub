from typing import Iterable
from django.db import models
from ..models import Order
from orders.manager import PaymentManager

class Payments(models.Model):
    COD ='COD'
    ONLINE = 'Online'
    
    UN_PAID ='Un_Paid'
    PAID    ='Paid'

    PAYMENT_TYPE = (
        (COD,'COD'),
        (ONLINE,'Online')
        )
    
    PAYMENT_STATUS = (
        (PAID,'Paid'),
        (UN_PAID,'Unpaid')
    )

    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    online_transaction_id = models.CharField(max_length=60,null=True,blank=True)
    payment_id = models.CharField(max_length=30,blank=True,null=True)
    payment_type = models.CharField(max_length=20,choices=PAYMENT_TYPE)
    payment_status = models.CharField(max_length=10, choices = PAYMENT_STATUS,default= UN_PAID)

    def __str__(self):
        return self.online_transaction_id
    
    objects = PaymentManager()

    def save(self,*args, **kwargs):
        if self.online_transaction_id:
            self.payment_type = self.ONLINE
            self.payment_status = self.PAID
        return super().save(*args, **kwargs)