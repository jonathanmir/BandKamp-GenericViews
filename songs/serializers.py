from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
        depth = 2

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
