from django.shortcuts import render
from .forms import CustomerRegistrationForm



def customer_signup(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST )
        if form.is_valid():
            form.save()
            return
    form = CustomerRegistrationForm()
    return render(request,'home/customer_signup.html' , {'form':form})

