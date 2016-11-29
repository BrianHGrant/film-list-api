from rest_framework import serializers
from films.models import Film, Theater, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'film_set')

class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theaters')

class TheaterSerializer(serializers.ModelSerializer):
    film_set = FilmSerializer(many=True)
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'film_set')


class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)
    theaters = TheaterSerializer(many=True)
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theaters')
