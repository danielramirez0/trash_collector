from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from datetime import date
from django.conf import settings

from .models import Customer


@login_required
def index(request):
    # The following line will get the logged-in user (if there is one) within any view function
    logged_in_user = request.user
    try:
        # This line will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=logged_in_user)

        today = date.today()

        context = {
            'logged_in_customer': logged_in_customer,
            'today': today
        }
        return render(request, 'customers/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('customers:create'))


@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        city_from_form = request.POST.get('city')
        zip_from_form = request.POST.get('zip_code')
        country_from_form = request.POST.get('country')
        weekly_from_form = request.POST.get('weekly_pickup')
        latitude_from_form = request.POST.get('latitude')
        longitude_from_form = request.POST.get('longitude')
        new_customer = Customer(
            name=name_from_form,
            user=logged_in_user,
            address=address_from_form,
            city=city_from_form,
            zip_code=zip_from_form,
            country=country_from_form,
            weekly_pickup=weekly_from_form,
            latitude=latitude_from_form,
            longitude=longitude_from_form,
            )
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'api_key': settings.GOOGLE_API_KEY
        }
        return render(request, 'customers/create.html', context)


@login_required
def suspend_service(request):
    logged_in_user = request.user
    logged_in_customer = Customer.objects.get(user=logged_in_user)
    if request.method == "POST":
        start_from_form = request.POST.get('start')
        end_from_form = request.POST.get('end')
        logged_in_customer.suspend_start = start_from_form
        logged_in_customer.suspend_end = end_from_form
        logged_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'logged_in_customer': logged_in_customer
        }
        return render(request, 'customers/suspend.html', context)


@login_required
def one_time_pickup(request):
    logged_in_user = request.user
    logged_in_customer = Customer.objects.get(user=logged_in_user)
    if request.method == "POST":
        date_from_form = request.POST.get('date')
        logged_in_customer.one_time_pickup = date_from_form
        logged_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'logged_in_customer': logged_in_customer
        }
        return render(request, 'customers/one_time.html', context)


@login_required
def edit_profile(request):
    logged_in_user = request.user
    logged_in_customer = Customer.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        city_from_form = request.POST.get('city')
        state_from_form = request.POST.get('state')
        zip_from_form = request.POST.get('zip_code')
        country_from_form = request.POST.get('country')
        weekly_pickup_from_form = request.POST.get('weekly_pickup')
        latitude_from_form = request.POST.get('latitude')
        longitude_from_form = request.POST.get('longitude')
        logged_in_customer.name = name_from_form
        logged_in_customer.address = address_from_form
        logged_in_customer.city = city_from_form
        logged_in_customer.state = state_from_form
        logged_in_customer.zip_code = zip_from_form
        logged_in_customer.country = country_from_form
        logged_in_customer.weekly_pickup = weekly_pickup_from_form
        logged_in_customer.latitude = latitude_from_form
        logged_in_customer.longitude = longitude_from_form
        logged_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'logged_in_customer': logged_in_customer,
            'api_key': settings.GOOGLE_API_KEY
        }
        return render(request, 'customers/edit_profile.html', context)
