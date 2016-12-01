from rest_framework import serializers
from films.models import Film, Theater, Genre


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')
        depth = 1

class GenreFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title')

class GenreSerializer(serializers.ModelSerializer):
    film_set = GenreFilmSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'film_set')

class GenreWriteSerializer(serializers.ModelSerializer):
    film_set = serializers.PrimaryKeyRelatedField(queryset=Film.objects.all(), many=True, allow_null=True)
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'film_set')

class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')

class TheaterFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title')

class TheaterSerializer(serializers.ModelSerializer):
    film_set = FilmSerializer(many=True, read_only=True)
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'film_set')

class TheaterWriteSerializer(serializers.ModelSerializer):
    film_set = serializers.PrimaryKeyRelatedField(queryset=Theater.objects.all(), many=True, allow_null=True)
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'film_set')
