from django.urls import path
from . import views
from django.views.generic import TemplateView




urlpatterns = [
    path('vehicles/', views.car_listing, name='vehicles'),
    path('vehicle/<str:pk>/', views.onecar, name='carviewer'),
    path('parts/', views.part_list, name='parts'),
    path('parts/<int:part_id>/', views.part_detail, name='part_detail'),
    #path('part/<str:pk>/', views.onecar, name='part'),
]
