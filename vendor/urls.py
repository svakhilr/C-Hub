from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.vendor_signup,name='vendor-signup'),
    path('signin/',views.vendor_signin, name='vendor-signin'),
    path('signout',views.vendor_signout, name='vendor-signout'),
    path('upload/documents/', views.upload_documents, name='upload-document'),
    path('dashboard/',views.vendor_dashboard,name='vendor-dashboard'),
    path('product/', views.vendor_products, name='vendor-products'),
    path('product_view/<int:product_id>/', views.product_view, name = 'product-view'),
    path('add/product/',views.add_product, name='add-product'),
    path('remove/products/<int:product_id>' , views.remove_product,name='remove-product')
]
