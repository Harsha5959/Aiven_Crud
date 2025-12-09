from django.db import models

class Employees(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_age = models.IntegerField()
    Employee_email = models.EmailField(unique=True)
    Employee_mobile = models.BigIntegerField()
    Employee_Department = models.CharField(max_length=50)
    Employee_Join_Date = models.DateField()

    class Meta:
        db_table = 'crud_employees' 
