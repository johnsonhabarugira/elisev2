from django.urls import path
from .views import current_country

urlpatterns = [
    # other URL routes...
    path('current-country/', current_country, name='current_country'),
]
