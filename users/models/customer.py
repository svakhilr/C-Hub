from django.db import models
from ..models import CustomUser


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser,
        on_delete = models.CASCADE,
        related_name = 'customer')
    name = models.CharField(max_length = 30)
    profile_picture = models.ImageField(upload_to='users/customer',
        null=True,blank=True)
    
    def __str__(self):
        return self.name