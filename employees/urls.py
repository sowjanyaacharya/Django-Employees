from django.urls import path
from . import views
#here we used the list for passing the url patterns
urlpatterns = [ 
   path('<int:pk>/', views.employee_details,name = 'employee_details'),  #here by using the pk we are fetching the employees likee...employeees/pk/ then it calls the view function we can also name it by using name paramenter as we can use to pass that name for url
]