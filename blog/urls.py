from django.urls import path
from . import views
from django.views.generic import TemplateView




urlpatterns = [
    path('blog', views.gettingblog, name='blog'),
    path('post/<str:pk>/', views.oneblog, name='blogviewer'),
   #
]
