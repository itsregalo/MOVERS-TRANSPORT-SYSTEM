from django.shortcuts import render

def IndexView(request, *args, **kwargs):
    return render(request, 'admin/index.html')