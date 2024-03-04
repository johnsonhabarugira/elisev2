from django.shortcuts import render
from blog.models import Post, Comment
from products.models import Car
from .models import BannerImage
import requests

def home(request):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')


    banner_images = BannerImage.objects.filter(active=True)
    featurecars= Car.objects.filter(featured=True).order_by('-created')[:3]
    blogpost= Post.objects.all()
    context = {
        'featurecars': featurecars,
        'blogpost': blogpost,
        'banner_images': banner_images,
        'country': country,
    }
    return render(request, 'home/index.html', context)

