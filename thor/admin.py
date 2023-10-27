from django.contrib import admin
from .models import contact
from django.contrib.admin.sites import AdminSite

# Register your models here.

class Contact_data(admin.ModelAdmin):
    list_display= ('name', 'email', 'subject', 'message')
    
  
admin.site.register(contact, Contact_data)