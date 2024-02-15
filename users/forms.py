from django.contrib.auth.forms import UserCreationForm 
from django import forms
from phonenumber_field.formfields import PhoneNumberField


from .models import CompanyProfile,CustomerProfile,CustomUser


class CompanyProfileForm(forms.ModelForm):
    

    class Meta:
        model = CompanyProfile
        fields = ('user','company_name','description','company_address',
                  'country','verification_status')
        

class CustomerRegistrationForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))

    password2= forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    phone_number = PhoneNumberField(region="IN")
    class Meta:
        model=CustomUser
        widgets = {
            
            # 'last_name'    : forms.TextInput(attrs = {'placeholder': 'last-name'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
        }
        fields=['full_name','email','phone_number','password','password2']


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
        print(commit)
        user = CustomUser.objects.create_user(self.cleaned_data["email"],self.cleaned_data["password"])
        user.phone_number = self.cleaned_data["phone_number"]
        user.save()
        print(user)
        val = self.cleaned_data
        print(val)
        return user
        