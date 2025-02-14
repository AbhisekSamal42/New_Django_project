from django.shortcuts import render, HttpResponse
from emp_app.models import *
from datetime import datetime

def index(request):
    return render(request, 'emp_app/index.html')

def view_all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'emp_app/view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        dept_name = request.POST.get('dept_name', '')
        role_name = request.POST.get('role_name', '')
        salary = int(request.POST.get('salary', 0))
        bonus = int(request.POST.get('bonus', 0))
        phone_no = int(request.POST.get('phone_no', 0))
        hire_date = request.POST.get('hire_date', '')

        try:
            hire_date = datetime.strptime(hire_date, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Invalid date format! Please use YYYY-MM-DD.")

        try:
            department = Department.objects.get(dept_name=dept_name)
            role = Role.objects.get(role_name=role_name)
        except Department.DoesNotExist:
            return HttpResponse("Department does not exist.")
        except Role.DoesNotExist:
            return HttpResponse("Role does not exist.")

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_name=department,
            role_name=role,
            salary=salary,
            bonus=bonus,
            phone_no=phone_no,
            hire_date=hire_date
        )
        new_emp.save()
        return HttpResponse("Employee added successfully!")

    return render(request, 'emp_app/add_emp.html')

def remove_emp(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return HttpResponse("Employee removed successfully.")
        except Employee.DoesNotExist:
            return HttpResponse("Employee not found.")
    return render(request, 'emp_app/remove_emp.html')

def filter_emp(request):
    if request.method == "POST":
        dept_name = request.POST.get('dept_name', '')
        role_name = request.POST.get('role_name', '')
        min_salary = request.POST.get('min_salary', 0)
        max_salary = request.POST.get('max_salary', 1000000)

        emps = Employee.objects.all()

        if dept_name:
            emps = emps.filter(dept_name__dept_name=dept_name)
        if role_name:
            emps = emps.filter(role_name__role_name=role_name)
        if min_salary and max_salary:
            emps = emps.filter(salary__gte=min_salary, salary__lte=max_salary)

        context = {'emps': emps}
        return render(request, 'emp_app/view_all_emp.html', context)
    return render(request, 'emp_app/filter_emp.html')
