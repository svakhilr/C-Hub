from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CompanyProfileForm
from .models import CustomUser,CompanyProfile,CompanyDocuments,CustomerProfile
from products.models import Product




@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):

    list_display = ('email','phone_number', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('phone_number', )}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('phone_number',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email',  'phone_number')
    ordering = ('email',)


class CompanyDocumentsInlineAdmin(admin.StackedInline):
    model = CompanyDocuments

class ProductInlineAdmin(admin.TabularInline):
    model = Product
    extra= 0

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    form = CompanyProfileForm
    inlines = [CompanyDocumentsInlineAdmin,ProductInlineAdmin]


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(CompanyDocuments)
class CompanyDocumentAdmin(admin.ModelAdmin):
    pass
    

    
