from django.shortcuts import render , HttpResponse
from . import models
# Create your views here.
def home(request):
    context = {}
   
       
    students = models.Student.objects.all().order_by("id")
   
    context ['students'] = students
 
   

    return render (request,'index.html',context)

def about (request):
   return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def studentDetails(request, id):
    context = {}
    students = models.Student.objects.filter(id=id)
    for student in students:
        student.prefix_str = getModelChoice(
            student.prefix, models.prefix_choices)

        context['student'] = student

    return render(request, 'details.html', context)


def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice[1]