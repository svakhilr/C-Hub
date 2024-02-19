from django.shortcuts import render,redirect
from vendor.forms import VendorRegistrationForm,VendorDocumentsForm
from django.contrib.auth import  login,logout
from django.contrib.auth.decorators import login_required
from django.http import Http404

import sweetify

from users.models import CompanyProfile
from users.forms import UserLoginForm
from products.models import Product
from products.forms import ProductForm

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

def vendor_signin(request):
    
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate_user()
            if user:
        
                if user.company.is_verified:
                    login(request,user)
                    sweetify.success(request , "Authenticated")
                    return redirect("vendor-dashboard")
                else:
                    sweetify.error(request , "Account not verified")
                    return redirect('vendor-signin')
            sweetify.error(request,"Invalid Credentials")
            return redirect('vendor-signin')
    form = UserLoginForm()
    return render(request , 'vendor/signin.html' , {"form":form})

def vendor_signout(request):
    logout(request)
    sweetify.info(request, 'Logged Out', button='Ok', timer=3000)
    return redirect('vendor-signin')



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

@login_required(login_url="/vendor/signin/")
def vendor_dashboard(request):
    company = request.user.company
    context = {"company":company}
    return render(request,"vendor/dashboard.html",context)

@login_required(login_url="/vendor/signin/")
def vendor_products(request):
    print("company product")
    company = request.user.company
    print(company)
    products = Product.objects.filter(company=company)
    print(products)
    context ={"products":products}
    return render(request, 'vendor/product.html', context)

def product_view(request,product_id):
    
    try:
        product = Product.objects.get(id=product_id)
        
    except Product.DoesNotExist:
        raise Http404("Product does not exists")
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
    
    form = ProductForm(instance = product)
    context = {
        "form":form,
        "product":product
    }

    return render(request, 'vendor/product_view.html',context)


def add_product(request):
    company = request.user.company
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product_form = form.save(commit=False) 
            product_form.company = company
            product_form.save()
            sweetify.success(request , "Product Added")
            return redirect('vendor-dashboard')
    
    form = ProductForm()
    context = {
        'form':form
    }
    return render(request,'vendor/add_product.html',context )

def remove_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    sweetify.success(request, "Product Deleted")
    return redirect("vendor-products")

    

        
