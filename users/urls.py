from django.urls import path
from . import views

urlpatterns = [
    path('customer/signup',views.customer_signup,name='customer-signup'),
]
