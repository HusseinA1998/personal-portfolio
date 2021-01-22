from django.shortcuts import render
from .models import Design


def home(request):
    designs = Design.objects.all()
    return render(request, 'portfolio/home.html', context={'des': designs})
