from django.urls import path
from . import views
from django.views.generic import TemplateView




urlpatterns = [
    path('vehicles/', views.car_listing, name='vehicles'),
    path('vehicle/<str:pk>/', views.onecar, name='carviewer'),
    #path('parts/', views.parts_listing, name='parts'),
    #path('part/<str:pk>/', views.onecar, name='part'),
]
