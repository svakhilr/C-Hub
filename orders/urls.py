from django.urls import path
from . import views

urlpatterns = [
    path('addtocart/',views.add_to_cart,name='add-to-cart')
]
