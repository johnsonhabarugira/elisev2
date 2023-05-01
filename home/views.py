from django.shortcuts import render
from blog.models import Post, Comment
from products.models import Car

def home(request):
    featurecars= Car.objects.all()
    blogpost= Post.objects.all()
    context = {
        'featurecars': featurecars,
        'blogpost': blogpost,
    }
    return render(request, 'home/index.html', context)

