from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from employees.models import Employee 


# Create your views here.
def employee_details(request,pk):   
    #try:
     #   employee = Employee.objects.get(pk=pk)
      #  print(employee)
    #except:
     #   raise Http404 we can write these set of lines of codes in one single line
    employee = get_object_or_404(Employee,pk = pk)   #get_object_or_404 is used to render both if found detail means detail else 404 error
    context = {
        'employee' : employee,
    }
    return render(request,'employees_detail.html',context)

