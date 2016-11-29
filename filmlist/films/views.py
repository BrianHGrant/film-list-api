from films.models import Film, Theater, Genre
from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer, FilmWriteSerializer

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        year_prod = request.GET.get('year_prod', ' ')
        year_prod__gte = request.GET.get('year_prod__gte', ' ')
        title = request.GET.get('title', ' ')
        films = Film.objects.all()
        if year_prod != ' ':
            films = Film.objects.filter(year_prod=year_prod)
        if year_prod__gte != ' ':
            films = Film.objects.filter(year_prod__gte=year_prod__gte)
        if title != ' ':
            films = films.filter(title__istartswith=title)
        serialized_films = FilmSerializer(films, many=True)
        return Response(serialized_films.data)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
