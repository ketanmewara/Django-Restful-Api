from rest_framework import serializers
from .models import Podcast,Song,AudioBook


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = '__all__'