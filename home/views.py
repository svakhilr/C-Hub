from django.shortcuts import render
from products.models import Product

def homeview(request):
    products = Product.objects.order_by('-created_on')[:3]
    print(request.user.is_authenticated)
    context = {
        "products":products
    }
    return render(request, 'home/home.html',context)
