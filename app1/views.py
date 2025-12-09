from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from app1.models import Employees
from app1.forms import Employee_form
from app1.forms1 import Employee_update_form
from django.http import HttpResponse


def details(request):
    data = Employees.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home.html', context)


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
        'form': form
    }
    return render(request, 'register.html', context)


def update(request, id):
    data = get_object_or_404(Employees, id=id)

    if request.method == "POST":
        form = Employee_update_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Employee_update_form(instance=data)

    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def delete(request, id):
    employee = get_object_or_404(Employees, id=id)

    # 🚨 Hardcoded credentials for delete
    CORRECT_USERNAME = "Harsha"      # <-- change to whatever you like
    CORRECT_PASSWORD = "12345"         # <-- change to whatever you like

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            # ✅ Credentials match → delete and redirect
            employee.delete()
            messages.success(request, "Employee deleted successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    # GET request → show the authentication + confirmation page
    context = {
        "employee": employee
    }
    return render(request, "delete_confirm.html", context)
