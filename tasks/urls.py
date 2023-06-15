from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('<int:tasks_id>', views.detail, name='detail'),
]