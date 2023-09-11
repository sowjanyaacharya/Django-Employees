from django.contrib import admin
from .models import Employee

# Register your models here.
#This is inside the employee app we had created the app by using python manage.py startapp appname(employees)
admin.site.register(Employee)   #here we need to register the employee table in the admin panel
