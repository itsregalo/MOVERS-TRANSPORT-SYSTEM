import imp
from django.urls import path
from .views import *

app_name = 'admin-dash'

urlpatterns = [
    path('', IndexView, name='index')
]
