from django.shortcuts import render , HttpResponse
from . import models
# Create your views here.
def home(request):
    context = {}
   
       
    students = models.Student.objects.all()
   
    context ['students'] = students
 
   

    return render (request,'index.html',context)

def about (request):
   return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")