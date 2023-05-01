from django.urls import path
from . import views

urlpatterns = [
    path('team', views.our_team, name='our_team'),
]
