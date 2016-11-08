from rest_framework import serializers
from films.models import Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')
