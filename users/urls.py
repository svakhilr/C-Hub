from django.urls import path
from . import views

urlpatterns = [
    path('customer/signup',views.customer_signup,name='customer-signup'),
    path('logout/',views.user_logout, name='user-logout'),
    path('user/login',views.user_login, name='user-login')
]
