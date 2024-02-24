from django import forms
from .models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('house_number','address','city','land_mark','pincode')