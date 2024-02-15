from django.db import models

from users.models import CompanyProfile

class Product(models.Model):
    company = models.ForeignKey(CompanyProfile,
        on_delete=models.CASCADE,
        related_name ='product')
    name = models.CharField(max_length=50)
    discription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='company/products',null=True)
    stock = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
