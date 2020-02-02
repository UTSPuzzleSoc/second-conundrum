from django.contrib import admin
from .models import Puzzle, PuzzleType, Document, DocumentType, PuzzleDifficulty

admin.site.register(Puzzle)
admin.site.register(PuzzleType)
admin.site.register(PuzzleDifficulty)
admin.site.register(Document)
admin.site.register(DocumentType)
