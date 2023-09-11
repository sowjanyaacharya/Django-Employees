from django.db import models

# Create your models here.
class Employee(models.Model):    #table name
    first_name = models.CharField(max_length=100)  #field name
    last_name = models.CharField(max_length=100)
    #designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img')
    email = models.EmailField(unique=True)  #to keep unigue
    phone = models.CharField(max_length=12,blank = True)  #optional field 
    created_at = models.DateTimeField(auto_now_add=True)
    upadted_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):   #to display the employee name wise rather than employee object1
        return self.first_name
