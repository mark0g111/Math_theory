from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Tasks


def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


def detail(request, tasks_id):
    tasks = get_object_or_404(Tasks, pk=tasks_id)
    return render(request, 'tasks/detail.html', {'tasks': tasks})
