from django.db import models
from .users import CustomUser

from django_countries.fields import CountryField


class CompanyProfile(models.Model):
    PENDING = 'pending'
    VERIFIED = 'verified'
    REJECTED = 'rejected'

    VERIFICATION_STATUS = (
        (PENDING,'Pending'),
        (VERIFIED,'Verified'),
        (REJECTED,'Rejected')
    )
    user = models.OneToOneField(CustomUser,
    on_delete = models.CASCADE,
    related_name ='company')
    company_name = models.CharField(max_length = 100)
    description = models.TextField(null=True,blank=True)
    verification_status = models.CharField(
        max_length = 20,
        choices = VERIFICATION_STATUS,
        default = PENDING
    )
    company_address = models.TextField()
    # country = CountryField(null=True)
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
class CompanyDocuments(models.Model):
    
    company = models.OneToOneField(CompanyProfile, 
        on_delete = models.CASCADE,
        related_name = 'company_documents')
    
    adhar_card = models.FileField(upload_to='company/adhar',null=True)
    liscence   = models.FileField(upload_to='company/liscence',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Documents of {self.company.company_name}"
    

