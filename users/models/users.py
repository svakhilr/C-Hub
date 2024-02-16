from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from ..managers import CustomUserManager




class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add = True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

    @property
    def is_customer(self):
        try:
            self.customer
            return True
        except:
            return False
    

    @property
    def is_company(self):
        try:
            self.company
            return True
        except:
            return False

    @property    
    def name(self):
        if self.is_company:
            return self.company.company_name
        else:
            return self.customer.name


