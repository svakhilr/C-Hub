from django.urls import path
from . import views

urlpatterns = [
    path('addtocart/',views.add_to_cart,name='add-to-cart'),
    path('view/cart/', views.view_cart , name='view-cart'),
    path('delete/cartitem/<int:cartitem_id>/',views.remove_cart_item, name='remove-cart-item'),
    path('update/cart/',views.update_cart,name='update-cart'),
]
