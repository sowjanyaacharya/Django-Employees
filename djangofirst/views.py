from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):  #this is the view for homepage
   employees = Employee.objects.all()   #this is the query to fetch the all employees
   #print(employees)
   # return HttpResponse('<h1>Hellooooo</h1>')
   context = {
      'employees': employees,  #context is mainly used to pass them back to the html page
   }
   return render(request,'home.html',context)   #render is used to return the html  page it takes 3 parameters