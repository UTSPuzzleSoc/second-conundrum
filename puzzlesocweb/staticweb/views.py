from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from puzzlesocweb.puzzlehunt.models import Puzzle

def index(request):
    puzzle_list = Puzzle.objects.all().order_by("-title")
    template = loader.get_template('index.html')
    context = RequestContext(request, { 'puzzles' : puzzle_list })
    return render(request, 'index.html', { 'puzzles' : puzzle_list })

def custom_404(request):
    return render(request, '404.html', {}, status=404)
