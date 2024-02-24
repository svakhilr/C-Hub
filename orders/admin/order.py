from django.contrib import admin
from ..models import Address,Cart,CartItem,Order,OrderItem,OrderAddress,Payments


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    pass