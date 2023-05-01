from .models import Car
from users.models import profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatevehicles(request, allvehicles, results):
    page = request.GET.get('page')
    results = 6
    paginator = Paginator(allvehicles, results)
    try:
     allvehicles = paginator.page(page)
    except PageNotAnInteger:
        page =1
        allvehicles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        allvehicles = paginator.page(page)
    leftIndex = (int(page) -4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages +1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, allvehicles

def searchcars(request):
    
    model = ''
    type = ''
    transmission = ''

    if request.GET.get('model'):
        model = request.GET.get('model')

    if request.GET.get('transmission'):
        transmission = request.GET.get('transmission')

    if request.GET.get('max_price'):
        max_price = request.GET.get('max_price')
    # filter the Car objects based on the search criteria
    allvehicles = Car.objects.filter(transmission__icontains=transmission,model__name__icontains=model)
    return allvehicles,model,transmission