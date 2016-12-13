from films.models import Film, Theater, Genre
from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer, FilmWriteSerializer, GenreWriteSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from films.permissions import IsOwnerOrReadOnly


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     year_prod = request.GET.get('year_prod', ' ')
    #     year_prod__gte = request.GET.get('year_prod__gte', ' ')
    #     title = request.GET.get('title', ' ')
    #     films = Film.objects.all()
    #     if year_prod != ' ':
    #         films = Film.objects.filter(year_prod=year_prod)
    #     if year_prod__gte != ' ':
    #         films = Film.objects.filter(year_prod__gte=year_prod__gte)
    #     if title != ' ':
    #         films = films.filter(title__istartswith=title)
    #     serialized_films = FilmSerializer(films, many=True)
    #     return Response(serialized_films.data)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return FilmWriteSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys() #get the keys from url
        filter_dict = {}  #create empty dictonary to hold values
        if(k): # checks if keys exist
            for key, value in request.GET.items(): # loops through all keys
                filter_dict[key] = value # adds the values =  filter type of object
            films = Film.objects.filter(**filter_dict) #returns the films filtered by selection
            serialized_films = FilmSerializer(films, many=True) # return the serialized film objects
            return Response(serialized_films.data) #returns to client
        else:
            return Response(FilmSerializer(Film.objects.all(),many=True).data) # if no keys, returns unfiltered list of films

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            theaters = Theater.objects.filter(**filter_dict)
            serialized_theaters = TheaterSerializer(theaters, many=True)
            return Response(serialized_theaters.data)
        else:
            return Response(TheaterSerializer(Theater.objects.all(), many=True).data)

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return GenreWriteSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            genres = Genre.objects.filter(**filter_dict)
            serialized_genres = GenreSerializer(genres, many=True)
            return Response(serialized_genres.data)
        else:
            return Response(GenreSerializer(Genre.objects.all(), many=True).data)


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      permissions.IsAdminUser,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      permissions.IsAdminUser,)
