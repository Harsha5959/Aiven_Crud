from django import forms
from app1.models import Employees

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'