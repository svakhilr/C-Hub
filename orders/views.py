from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import  login_required

from .models import CartItem,Address,Order,Payments
from .forms import AddressForm
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


def checkout(request):
    cart = get_cart(request)
    customer = request.user.customer
    cart_items = cart.cart_item.all()
    addresses = Address.objects.filter(customer=customer) 
    context = {
        'cart':cart,
        'cartitems':cart_items,
        'addresses':addresses
    }
    return render(request,'order/checkout.html',context)

def add_address(request):
    print("add address")
    customer = request.user.customer
    house_number = request.POST.get('house_number')
    address      = request.POST.get('address')
    city         = request.POST.get('city')
    state        = request.POST.get('state')
    land_mark    = request.POST.get('landmark')
    pincode      = request.POST.get('pincode')
    print(state)
    address = Address.objects.create(
        customer = customer,house_number=house_number,address=address,
        city=city,state=state,land_mark=land_mark,pincode=pincode
    )
    return redirect('checkout')

def confirm_order(request):
    address_id = request.POST.get('order_address')
    cart = get_cart(request)
    order = cart.place_order()
    address = Address.objects.get(id=address_id)
    address.copy_to_order_address(order)
    context = {
        "success":"added",
        "order_id":order.order_id
    }
    return JsonResponse(context)

def payment_view(request,order_id):
    order = Order.objects.get(order_id=order_id)
    order_items = order.order_item.all()
    order_address = order.order_address
    print("order")
    context = {
        'order':order,
        'order_items':order_items,
        'order_address':order_address
    }
    return render(request,'order/payment.html',context)

def paypal(request):
    print('paypal')
    order_id = request.POST.get('order_id')
    transaction_id = request.POST.get('transaction_id')
    print(order_id)
    order = Order.objects.get(id=order_id)
    payment = Payments.objects.create(order=order,online_transaction_id=transaction_id)
    
    return JsonResponse({"message":"payment done"})

def cash_on_delivery(request):
    pass


def invoice(request):
    customer = request.user.customer
    order = Order.objects.filter(customer=customer).last()
    print(order)
    order_items =  order.order_item.all()
    context = {
        'order':order,
        'order_items':order_items
    }
    return render(request,'order/invoice.html',context)





