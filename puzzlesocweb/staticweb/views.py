from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from puzzlesocweb.puzzlehunt.models import Puzzle

def index(request):
    puzzle_list = Puzzle.objects.all().order_by("-title")
    return render(request, 'index.html', { 'puzzles' : puzzle_list })

def custom_404(request):
    return render(request, '404.html', {}, status=404)

def puzzle(request, id):
    puzzle_obj = get_object_or_404(Puzzle, id=id)
    return render(request, 'view_puzzle.html', {'puzzle' : puzzle_obj})
