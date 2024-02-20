from orders.models import Cart

def get_cart(request):
    try:
        
        return Cart.objects.get(customer=request.user.customer)
    except:
        return None