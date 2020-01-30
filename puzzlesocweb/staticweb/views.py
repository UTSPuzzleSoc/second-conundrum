from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from puzzlesocweb.puzzlehunt.models import Puzzle

@require_http_methods(["GET"])
def index(request):
    return render(request, 'index.html', {'puzzles': Puzzle})
