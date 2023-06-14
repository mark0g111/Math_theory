from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Question


def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions/questions.html', {'questions': questions})


def detail(request, questions_id):
    questions = get_object_or_404(Question, pk=questions_id)
    return render(request, 'questions/detail.html', {'questions': questions})
