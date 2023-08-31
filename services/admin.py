from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin): #conf extendida sobre admin
    readonly_fields=('created', 'updated')

admin.site.register(Service, ServiceAdmin)