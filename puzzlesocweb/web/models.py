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

class Event(models.Model):
    # Date time
    # From this we can extrapolate other attributes e.g. past / in progress / future
    startingDateTime = models.DateTimeField("Starting date and time of the event")
    endingDateTime = models.DateTimeField("Ending date and time of the event")

    # Short alphanumerical id for website to display, e.g magical_arcade_machine
    url = models.CharField(max_length=30)

    name = models.CharField(max_length=60)
    shortDescription = models.CharField(max_length=300)
    longDescription = models.CharField(max_length=2000)

    location = models.CharField(max_length=60)
    interactable = models.BooleanField(verbose_name="Whether this event is interactable on our website")


class OrderedEvent(Event):
    class Meta:
        ordering = ["startingDateTime", "endingDateTime"]
        proxy = True


# class Puzzle(models.Model):
    # Interactable Puzzles on our website   