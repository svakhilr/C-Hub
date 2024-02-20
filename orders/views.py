from django.shortcuts import render
from django.http import JsonResponse

from .models import CartItem
from products.models import Product
from config.helper import get_cart

def add_to_cart(request):
    if request.method == "POST":
        cart = get_cart(request)
        
        if cart:
            product_id = int(request.POST.get('prod_id'))
            quantity = int(request.POST.get('item_quantity'))
            product = Product.objects.get(id=product_id)
            if cart.cart_item.all().filter(product=product):
                flag = 1
            else:
                CartItem.objects.create(cart=cart,product=product,quantity=quantity)
                product.stock-=quantity
                product.save()
                flag = 2
        else:
            flag = 3
        
        context = {
            "flag":flag
        }
        return JsonResponse(context)




