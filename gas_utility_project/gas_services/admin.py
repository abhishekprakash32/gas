from django.contrib import admin

# Register your models here.
from .models import Customer, ServiceRequest

admin.site.register(Customer)
admin.site.register(ServiceRequest)
