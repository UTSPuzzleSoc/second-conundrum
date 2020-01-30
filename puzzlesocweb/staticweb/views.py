from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from puzzlesocweb.puzzlehunt.models import Puzzle

def index(request):
    return render(request, 'index.html', {'puzzles': Puzzle})

def custom_404(request):
    return render(request, '404.html', {}, status=404)
