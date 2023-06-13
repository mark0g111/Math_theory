from django.shortcuts import render
from .models import Theory


def home(request):
    return render(request, 'theory/home.html')


def theory(request):
    theorys = Theory.objects.all()
    return render(request, 'theory/theory.html', {'theorys': theorys})
