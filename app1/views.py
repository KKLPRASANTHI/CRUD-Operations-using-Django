from django.shortcuts import render,redirect
from app1.models import Emp
from django.http import HttpResponse
# Create your views here.
def store(request):
	if request.method=="POST":
		empid=request.POST['empid']
		name=request.POST['name']
		age=request.POST['age']
		salary=request.POST['salary']
		desig=request.POST['desig']
		phno=request.POST['phno']
		email=request.POST['email']
		dept=request.POST['dept']
		Emp.objects.create(empid=empid,name=name,age=int(age),salary=float(salary),desig=desig,phno=int(phno),email=email,dept=dept)
		#return HttpResponse('<h1 style="color:powderble;text-align:center">DONE</h1>')
		return redirect('/display')
	return render(request,'app1/store.html')
def display(request):
	data=Emp.objects.all()
	return render(request,'app1/display.html',{'info':data})
def delete(request,name):
	Emp.objects.filter(name=name).delete()
	return redirect('/display')
	#return Httpresponse(name+"Deleted Successfully...!!")
def update(request,empid):
	data=Emp.objects.get(empid=empid)
	#department=['Testing','System Administration','Network Administration','Development'] 
	if request.method=="POST":
		empid=request.POST['empid']
		name=request.POST['name']
		age=request.POST['age']
		salary=request.POST['salary']
		desig=request.POST['desig']
		phno=request.POST['phno']
		email=request.POST['email']
		dept=request.POST['dept']
		data.empid=empid
		data.name=name
		data.age=age
		data.salary=salary
		data.desig=desig
		data.phno=phno
		data.email=email
		data.dept=dept
		data.save()
		return redirect('/display')
	# except:
	# 	return HttpResponse("<Center><div>Employee Already Exists</div></Center>")
	return render(request,'app1/update.html',{"mydata":data})
