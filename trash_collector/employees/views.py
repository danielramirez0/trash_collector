from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.db.models import Q
from datetime import date


from .models import Employee
# Create your views here.


@login_required
def index(request):
    logged_in_user = request.user
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    today = date.today()
    try:
        logged_in_employee = Employee.objects.get(user=logged_in_user)
        assigned_customers = Customer.objects.filter(
            zip_code=logged_in_employee.zip_code
        ).filter(Q(weekly_pickup=today.strftime('%A')) | Q(one_time_pickup=today)
                 ).exclude(suspend_start__lte=today, suspend_end__gte=today
                           ).exclude(date_of_last_pickup=today)

        context = {
            'logged_in_employee': logged_in_employee,
            'today': today,
            'assigned_customers': assigned_customers,
            'all_customers': Customer.objects.all()
        }
        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))


@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        zip_from_form = request.POST.get('zip_code')
        new_employee = Employee(name=name_from_form,
                                user=logged_in_user, zip_code=zip_from_form)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


@login_required
def edit_profile(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/edit_profile.html', context)


@login_required
def customers(request, filter_prop, filter_value):
    logged_in_user = request.user
    Customer = apps.get_model('customers.Customer')
    if filter_prop == 'All':
        customers_list = Customer.objects.all()
        display_title = 'All Customers'
    else:
        if filter_prop == 'zip_code':
            customers_list = Customer.objects.filter(zip_code=filter_value)
            display_title = f"Customers in Zip code {filter_value}"
        elif filter_prop == 'balance':
            customers_list = Customer.objects.filter(balance=filter_value)
            display_title = f"Customers with balances of ${filter_value}"
        elif filter_prop == 'weekly_pickup':
            customers_list = Customer.objects.filter(weekly_pickup=filter_value)
            display_title = f"Customers with weekly pickup day of {filter_value}"
    today = date.today()
    try:
        logged_in_employee = Employee.objects.get(user=logged_in_user)
        context = {
            'logged_in_employee': logged_in_employee,
            'today': today,
            'all_customers': customers_list,
            'display_title': display_title,
        }
        return render(request, 'employees/customers.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))
