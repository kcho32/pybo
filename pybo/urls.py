from django.contrib import admin
from django.urls import path

from pybo import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
]
