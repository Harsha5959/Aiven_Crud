from django.shortcuts import render,redirect
from app1.models import Employees
from app1.forms import Employee_form
from app1.forms1 import Employee_update_form
from django.http import HttpResponse


def details(request):
    data = Employees.objects.all()
    context = {
        'data':data
    }
    return render(request,'home.html',context)

def emp_form(request):
    form = Employee_form()

    if request.method == 'POST':
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Inavalid Data")
    else:
        form = Employee_form()

    context = {
        'form' : form
    }
    return render(request,'register.html',context)


def update(request,id):
    data = Employees.objects.get(id=id)

    if request.method == "POST":
        form = Employee_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Employee_update_form(instance=data)
    context = {
        'form' : form 
    }
    return render(request,'update.html',context)


def delete(request,id):
    data = Employees.objects.get(id=id)
    data.delete()
    return redirect('home')