from django.db import models


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
    