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



    
def paginatepart(request, parts, results):
    page = request.GET.get('page')
    results = 2
    paginator = Paginator(parts, results)
    try:
     parts = paginator.page(page)
    except PageNotAnInteger:
        page =1
        parts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        parts = paginator.page(page)
    leftIndex = (int(page) -4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages +1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, parts





def searchcars(request):
    
    title = ''

    if request.GET.get('title'):
        title = request.GET.get('title')

    # filter the Car objects based on the search criteria
    allvehicles = Car.objects.filter(title__icontains=title).select_related('model')
    return allvehicles,title