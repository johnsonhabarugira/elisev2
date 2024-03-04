
from django.shortcuts import render, get_object_or_404
from .models import Car,Part
from users.models import profile
from django.http import HttpResponse
import uuid
from .utils import searchcars, paginatevehicles,paginatepart
from urllib.parse import urlencode
import requests

""""""

def car_listing(request):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')


    allvehicles , title= searchcars(request)
    #custom_range, allvehicles = paginatevehicles(request, allvehicles,6)
    context = {
        'allvehicles': allvehicles,
        'title':title,
    }
    return render(request, 'cars/cars.html', context)

   
def onecar(request, pk):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')


    viewcar = Car.objects.select_related('dealer').get(id=pk)
    message = f"I'm interested in buying the car/spareparts from your website  . Could you please provide more information?"
    mobile = viewcar.dealer.phone_number # Replace with dynamic mobile number
    params = {'text': message, 'phone': mobile}
    whatsapp_url = f"https://wa.me/{mobile}?{urlencode(params)}"
    
    # Increment page visits
    viewcar.page_visits += 1
    viewcar.save()
    context = {
        'viewcar': viewcar,
        'whatsapp_url': whatsapp_url,
        'country': country,
    }
    return render(request, 'cars/single-car.html', context)
 
def part_list(request):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')

    parts = searchcars(request)
    custom_range, parts = paginatepart(request, parts,6)
    query = request.GET.get('q')


    


    if query:
        custom_range, parts = paginatepart(request, parts,6)
        parts = Part.objects.filter(name__icontains=query)
    else:
        parts = Part.objects.all()
        custom_range, parts = paginatepart(request, parts,6)
    context = {
        'parts': parts,
        'query': query,
        'country': country,
    }
    return render(request, 'parts/parts.html',context)


    
def part_detail(request, part_id):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')
    part = Part.objects.select_related('dealer').get(pk=part_id)
    context = {'part': part,
        'country': country,}
    return render(request, 'parts/part_detail.html', context)
