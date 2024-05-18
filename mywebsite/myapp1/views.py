from django.http import HttpResponse
from django.shortcuts import redirect, render

from myapp1.models import Student


# Create your views here.
def say_hi(request):
    # return HttpResponse("hello world")
    return render(request,'hello.html')

def greet_user(request):
    return render(request,"hello.html",{"name":"Aman Tiwari"})

# def index(request):
#     return render(request,"index.html",{"name":"Aman Tiwari"})

def index(request):
    # template=loader.get_template("index.html")
    # return HttpResponse(template.render())
    studentsObj=Student.objects.all()
    return render(request,"index.html",{"students":studentsObj})

def form_update(request):
    
    if(request.POST):
        form_data=request.POST.dict()
        print(form_data)
    name=form_data.get("name")
    mobileno=form_data.get("mobileno")
    # print(name,mobileno)
    Student.objects.create(name=name,mobileno=mobileno)
    return redirect("home")