from django.shortcuts import render,redirect
from .forms import CustomerRegistrationForm,UserLoginForm

from django.contrib.auth import  login,logout,authenticate

import sweetify



def customer_signup(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            sweetify.success(request, 'Account was successfuly registered')
            return redirect("/")
    form = CustomerRegistrationForm()
    return render(request,'home/customer_signup.html' , {'form':form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate_user()
            if user is not None:
                login(request,user)
                sweetify.success(request, 'Account was successfuly registered')
                return redirect("/")
        else:
            sweetify.warning(request, 'Invalid Credentials')
    form = UserLoginForm()
    return render(request,'home/customer_login.html',{'form':form})





def user_logout(request):
    print("logout")
    logout(request)
    sweetify.info(request, 'Logged Out', button='Ok', timer=3000)
    return redirect('home')


