from django.shortcuts import render,get_object_or_404

from .models import Product

def view_products(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,'shop/shop.html',context)

def product_detail(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    context = {
        "product":product
        }
    return render(request,'shop/product_detail.html',context)

