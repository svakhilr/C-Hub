from django.shortcuts import render,redirect
from vendor.forms import VendorRegistrationForm,VendorDocumentsForm
from django.contrib.auth import  login
import sweetify

from users.models import CompanyProfile

def vendor_signup(request):

    if request.method == "POST":
        
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            print("company form")
            user = form.save()
            login(request,user)
            sweetify.success(request , "Account Registered")
            return redirect("upload-document")
    form = VendorRegistrationForm()
    return render(request, 'vendor/signup.html',{'form':form})

def upload_documents(request):
    print(request.user)
    if request.method == "POST":
        company = CompanyProfile.objects.get(user=request.user)
        form = VendorDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            
            documents_form = form.save(commit=False)
            documents_form.company= company
            documents_form.save()
            sweetify.success(request , "Documents Uploaded")
            return redirect('/')
    
    form = VendorDocumentsForm()
    return render(request,'vendor/document_upload.html' , {"form":form})
        
