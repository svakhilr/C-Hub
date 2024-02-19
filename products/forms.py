from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name','image','discription','price','stock','in_stock')