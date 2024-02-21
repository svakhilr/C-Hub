from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import  login_required

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
    
def remove_cart_item(request,cartitem_id):
    print("romve")
    cart_item = CartItem.objects.get(id=cartitem_id)
    cart_item.delete()
    return redirect('view-cart')
    
    
@login_required(login_url="/users/user/login")
def view_cart(request):
    cart = get_cart(request)
    cart_items = cart.cart_item.all()
    context = {
        "cart":cart,
        "cart_items":cart_items
    } 
    return render(request,'shop/cart.html',context)

def update_cart(request):
    if request.method =="POST":
        cart = get_cart(request)
        product_id = int(request.POST.get('prod_id'))
        quantity   = int(request.POST.get('quantity'))
        action     = request.POST.get('action')
        print(product_id)
        cart_item = CartItem.objects.get(cart=cart,product__id=product_id)
        if action == 'add':
            quantity+=1
        else:
            if quantity == 1:
                return JsonResponse(
                    {"caritemtotal": cart_item.cart_item_total,
                     "quantity":quantity,
                     "cartitem_id":cart_item.id,
                     "discount":cart.discount,
                     "carttotal":cart.cart_total,
                     "grandtotal":cart.grand_total
                    }
                )
            else:
                quantity -=1
        
        cart_item.quantity = quantity
        cart_item.save()
        context = {
            "caritemtotal": cart_item.cart_item_total,
            "quantity":quantity,
            "cartitem_id":cart_item.id,
            "discount":cart.discount,
            "carttotal":cart.cart_total,
            "grandtotal":cart.grand_total
        }
        return JsonResponse(context)




