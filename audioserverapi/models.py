from django.db import models

# Create your models here.
class Podcast(models.Model):
    Name = models.CharField(max_length = 100, blank = False)
    duration = models.IntegerField()
    Uploadedtime = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participant = models.CharField(max_length=100)

class Song(models.Model):
    Name = models.CharField(max_length = 100, blank = False)
    duration = models.IntegerField()
    Uploadedtime = models.DateTimeField(auto_now_add=True)

class AudioBook(models.Model):
    duration = models.IntegerField()
    Uploadedtime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=10)

    