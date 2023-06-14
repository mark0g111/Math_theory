from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.questions, name='questions'),
    path('<int:questions_id>', views.detail, name='detail'),
]