
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def emp_list (request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employees/employee_list.html',context )


def emp_form(request,id =0):
    if request.method == 'GET':
        if id==0:      
            form = EmployeeForm()
        else:
            employee= Employee.objects.get(id =id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employees/employee_form.html',{'form': form })
    else :
        if id ==0:

            form = EmployeeForm(request.POST)
        else :
            employee= Employee.objects.get(id =id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def emp_delete(request,id):
    employee= Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employee/list')
    
