from django.db import models

class Puzzle(models.Model):
    title = models.CharField(max_length=200, help_text='Enter the puzzle\'s title')
    created = models.DateTimeField('date created')
    puzzle_type = models.ForeignKey('PuzzleType', on_delete=models.SET_NULL, null=True)
    puzzle_text = models.CharField(max_length=1000, help_text='Enter the puzzle text here')
    answer = models.CharField(max_length=1000, help_text='The answer for the puzzle.')
    case_sensitive = models.BooleanField(default=False)
    difficulty = models.ForeignKey('PuzzleDifficulty', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('puzzle-detail', args=[str(self.id)])

class PuzzleType(models.Model):
    name = models.CharField(max_length=100, help_text='Puzzle category (ie. Rebus)')

    def __str__(self):
        return self.name

class PuzzleDifficulty(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the document')
    document = models.FileField(upload_to='document_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(
        max_length=255, blank=True, help_text='Optional description for the document.'
        )
    document_type = models.ForeignKey('DocumentType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('document-detail', args=[str(self.id)])

class DocumentType(models.Model):
    name = models.CharField(max_length=100, help_text='Document type (ie. jpg, png)')

    def __str__(self):
        return self.name
    