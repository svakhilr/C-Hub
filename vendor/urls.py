from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.vendor_signup,name='vendor-signup'),
    path('upload/documents', views.upload_documents, name='upload-document')
]
