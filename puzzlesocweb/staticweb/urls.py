from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('puzzles/<int:id>', views.puzzle, name='puzzle-view'),
]
