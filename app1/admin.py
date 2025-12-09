from django.contrib import admin

# Register your models here.
from app1.models import Employees

class employees_Admin(admin.ModelAdmin):
    list_display = ['Employee_name','Employee_age','Employee_email']

admin.site.register(Employees,employees_Admin)
