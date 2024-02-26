from django import forms
from .models import Address,OrderItem


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('house_number','address','city','land_mark','pincode')

class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ('product_name','product_image','quantity','order_status')