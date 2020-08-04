from django.db import models

# Create your models here.
class Emp(models.Model):
	department=[('Tesing','Testing'),('System Administration','System Administration'),('Network Administration','Network Administration'),('Development','Development')] 
	empid=models.IntegerField(null=False,primary_key=True)
	name=models.CharField(max_length=50,null=True)
	age=models.IntegerField(null=True)
	salary=models.FloatField(null=True)
	desig=models.CharField(max_length=50,null=True)
	phno=models.IntegerField(null=True)
	email=models.EmailField(max_length=50,null=True)
	dept=models.CharField(max_length=50,null=True,choices=department)
