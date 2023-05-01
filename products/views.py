
from django.shortcuts import render, get_object_or_404
from .models import Car
from users.models import profile
from django.http import HttpResponse
import uuid
from .utils import searchcars, paginatevehicles
from urllib.parse import urlencode

""""""

def car_listing(request):
    allvehicles , model, type = searchcars(request)
    custom_range, allvehicles = paginatevehicles(request, allvehicles,6)
    context = {
        'allvehicles': allvehicles,
        'type':type,
        'model':model,
        'custom_range':custom_range
    }
    return render(request, 'cars/cars.html', context)

   
def onecar(request, pk):
    viewcar = Car.objects.select_related('dealer').get(id=pk)
    message = f"I'm interested in buying the car/spareparts from your website  . Could you please provide more information?"
    mobile = viewcar.dealer.phone_number # Replace with dynamic mobile number
    params = {'text': message, 'phone': mobile}
    whatsapp_url = f"https://wa.me/{mobile}?{urlencode(params)}"
    context = {
        'viewcar': viewcar,
        'whatsapp_url': whatsapp_url,
    }
    return render(request, 'cars/single-car.html', context)
    
