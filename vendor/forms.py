
from typing import Any
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import authenticate

from users.models import CompanyProfile,CompanyDocuments,CustomUser
from django_countries.fields import CountryField


class CompanyProfileForm(forms.ModelForm):
    

    class Meta:
        model = CompanyProfile
        fields = ('user','company_name','description','company_address',
                  'country','verification_status')
        

class VendorLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))

    def authenticate_user(self):
        print(self.cleaned_data)
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user = authenticate(username=email, password=password)
        return user
        

class VendorRegistrationForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))

    password2= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    phone_number = PhoneNumberField(region="IN")
    description  = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    
    class Meta:
        model=CustomUser
        widgets = {
            
            # 'last_name'    : forms.TextInput(attrs = {'placeholder': 'last-name'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
        }
        fields=['company_name','email','phone_number','password','password2','description',]


    # to override the class property
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        data = super().clean()
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 and password2:
            if password1 != password2:
                print("validation error")
                raise forms.ValidationError("password does't match! ")
        return data
    
    def save(self, commit=True):
        user = CustomUser.objects.create_user(self.cleaned_data["email"],self.cleaned_data["password"])
        user.phone_number = self.cleaned_data["phone_number"]
        user.save()
        cleaned_data = self.cleaned_data
        c =CompanyProfile.objects.create(user=user,company_name = cleaned_data["company_name"],
            description=cleaned_data["description"],company_address="kjhkhskdhk")
        return user
    

class VendorDocumentsForm(forms.ModelForm):
    class Meta:
        model = CompanyDocuments
        fields = ('adhar_card','liscence')

    
    

