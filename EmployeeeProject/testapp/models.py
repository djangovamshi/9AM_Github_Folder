from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_blood_group = models.CharField(max_length=60)
    emp_mobile = models.BigIntegerField(unique=True)
    emp_address = models.CharField(max_length=60)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,)

    def __str__(self):
        return self.emp_name