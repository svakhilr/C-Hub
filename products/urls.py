from django.urls import path
from . import views

urlpatterns = [
    path('view/products/',views.view_products,name='view-products'),
    path('view/product/detail/<int:product_id>' , views.product_detail , name = 'product-detail')
]
