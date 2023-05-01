from django.urls import path
from . import views
from .views import about

urlpatterns = [
    path('about', views.about, name='about'),
]
