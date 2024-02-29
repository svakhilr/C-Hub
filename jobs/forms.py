
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import authenticate

from users.models import CustomUser, WorkerProfile,JobProfile
from django_countries.fields import CountryField


class WorkerProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = WorkerProfile
        fields = ('profile_name','profile_pic',)
        

class WorkerLoginForm(forms.Form):
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
        

class WorkerRegistrationForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))

    password2= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    profile_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Profile Name'}))

    phone_number = PhoneNumberField(region="IN")
    
    
    class Meta:
        model=CustomUser
        widgets = {
            
            # 'last_name'    : forms.TextInput(attrs = {'placeholder': 'last-name'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
        }
        fields=['profile_name','email','phone_number','password','password2']


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
        WorkerProfile.objects.create(user=user,profile_name = cleaned_data["profile_name"])
        return user
    

class JobProfileForm(forms.ModelForm):

    class Meta:
        model = JobProfile
        fields = ('job_profile_pic','description','job_category','max_amount_per_hour','is_negotiable')
    



    
    

