from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Theory


def home(request):
    return render(request, 'theory/home.html')


def theory(request):
    theorys = Theory.objects.all()
    return render(request, 'theory/theory.html', {'theorys': theorys})

def detail(request, theory_id):
    theory = get_object_or_404(Theory, pk=theory_id)
    return render(request, 'theory/detail.html', {'theory':theory})
