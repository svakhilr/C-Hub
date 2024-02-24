from django.contrib import admin
from .models import Address,Cart,CartItem,Order,OrderItem,OrderAddress,Payments



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass