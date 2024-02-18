from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.vendor_signup,name='vendor-signup'),
    path('signin/',views.vendor_signin, name='vendor-signin'),
    path('signout',views.vendor_signout, name='vendor-signout'),
    path('upload/documents/', views.upload_documents, name='upload-document'),
    path('dashboard/',views.vendor_dashboard,name='vendor-dashboard'),
    path('product/', views.vendor_products, name='vendor-products')
    
]
