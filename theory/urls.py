from django.urls import path
from . import views

app_name = 'theory'

urlpatterns = [
    path('', views.theory, name='theory'),
    path('<int:theory_id>', views.detail, name='detail'),
]