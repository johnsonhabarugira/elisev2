from django.shortcuts import render
import requests

def current_country(request):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')
    return render(request, 'geolocation/current_country.html', {'country': country})
