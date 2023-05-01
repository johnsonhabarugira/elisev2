from django.urls import path
from .views import terms

urlpatterns = [
    path('terms/', terms, name='terms'),
]
