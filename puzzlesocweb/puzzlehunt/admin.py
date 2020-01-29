from django.contrib import admin
from .models import Puzzle, PuzzleType, Document, DocumentType

admin.site.register(Puzzle)
admin.site.register(PuzzleType)
admin.site.register(Document)
admin.site.register(DocumentType)
