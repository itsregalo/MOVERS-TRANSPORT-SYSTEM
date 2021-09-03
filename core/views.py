from django.shortcuts import render
from .models import *

# Create your views here.

def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')

def Employers(request, *args, **kwargs):
    drivers = Driver.objects.all()
    loaders = Loader.objects.all()

    context = {
        'drivers':drivers,
        'loaders':loaders
    }
    return render(request, 'core/employers.html', context)




