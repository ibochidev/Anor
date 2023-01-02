from django.urls import path

from .views import base, index, createCar

urlpatterns = [
    path('', base, name='base'),
    path('create/', createCar, name='create'),
    path('index/', index,  name='index')
]