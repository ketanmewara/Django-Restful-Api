from rest_framework import viewsets
from . import models
from . import serializer

class PodcastViewset(viewsets.ModelViewSet):
    queryset = models.Podcast.objects.all()
    serializer_class = serializer.PodcastSerializer


class SongViewset(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializer.SongSerializer

class AudiobookViewset(viewsets.ModelViewSet):
    queryset = models.AudioBook.objects.all()
    serializer_class = serializer.AudioSerializer

