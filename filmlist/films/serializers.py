from rest_framework import serializers
from films.models import Film, Theater, Genre
from django.contrib.auth.models import User


class FilmSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'owner')
        depth = 1

    """
    The untyped ReadOnlyField is always read-only,
    and will be used for serialized representations,
    but will not be used for updating model instances when they are deserialized.
    """

class GenreFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title')

class GenreSerializer(serializers.ModelSerializer):
    film_set = GenreFilmSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Genre
        fields = ('id', 'title', 'description', 'film_set', 'owner')

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
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'film_set', 'owner')

class TheaterWriteSerializer(serializers.ModelSerializer):
    film_set = serializers.PrimaryKeyRelatedField(queryset=Theater.objects.all(), many=True, allow_null=True)
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'film_set')

class UserSerializer(serializers.ModelSerializer):
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'films')
