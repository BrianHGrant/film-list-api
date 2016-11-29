from films.models import Film
from films.serializers import FilmSerializer, TheaterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer, FilmWriteSerializer

class FilmList(APIView):
    """
    List all films, or create a new film.
    """
    def get(self, request, format=None):
        films = Film.objects.all()
        serialized_films = FilmSerializer(films, many=True)
        return Response(serialized_films.data)

    def post(self, request, format=None):
        film = FilmSerializer(data=request.data)
        if film.is_valid():
            film.save()
            return Response(film.data, status=status.HTTP_201_CREATED)
        return Response(film.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDetail(APIView):
    """
    Retrieve, update or delete a film instance.
    """
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        film = self.get_object(pk)
        serialized_film = FilmSerializer(film)
        return Response(serialized_film.data)

    def put(self, request, pk, format=None):
        film = self.get_object(pk)
        serialized_film = FilmSerializer(film, data=request.data)
        if serialized_film.is_valid():
            serialized_film.save()
            return Response(serialized_film.data)
        return Response(serialized_film.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        film = self.get_object(pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TheaterList(APIView):
    """
    List all theaters, or create a new theater.
    """
    def get(self, request, format=None):
        theaters = Theater.objects.all()
        serialized_theaters = TheaterSerializer(theaters, many=True)
        return Response(serialized_theaters.data)

    def post(self, request, format=None):
        theater = TheaterSerializer(data=request.data)
        if theater.is_valid():
            theater.save()
            return Response(theater.data, status=status.HTTP_201_CREATED)
        return Response(theater.errors, status=status.HTTP_400_BAD_REQUEST)

class TheaterDetail(APIView):
    """
    Retrieve, update or delete a theater instance.
    """
    def get_object(self, pk):
        try:
            return Theater.objects.get(pk=pk)
        except Theater.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        theater = self.get_object(pk)
        serialized_theater = TheaterSerializer(theater)
        return Response(serialized_theater.data)

    def put(self, request, pk, format=None):
        theater = self.get_object(pk)
        serialized_theater = TheaterSerializer(theater, data=request.data)
        if serialized_theater.is_valid():
            serialized_theater.save()
            return Response(serialized_theater.data)
        return Response(serialized_theater.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        theater = self.get_object(pk)
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def theater_list(request, format=None):
#     """
#     List all snippets, or create a new theater.
#     """
#     if request.method == 'GET':
#         theaters = Theater.objects.all()
#         serializedtheater = TheaterSerializer(theaters, many=True)
#         return Response(serializedtheater.data)
#
#     elif request.method == 'POST':
#         serializedtheater = TheaterSerializer(data=request.data)
#         if serializedtheater.is_valid():
#             serializedtheater.save()
#             return Response(serializedtheater.data, status=status.HTTP_201_CREATED)
#         return Response(serializedtheater.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'POST'])
# def genre_list(request, format=None):
#     """
#     List all snippets, or create a new genre.
#     """
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         serializedgenre = GenreSerializer(genres, many=True)
#         return Response(serializedgenre.data)
#
#     elif request.method == 'POST':
#         serializedgenre = GenreSerializer(data=request.data)
#         if serializedgenre.is_valid():
#             serializedgenre.save()
#             return Response(serializedgenre.data, status=status.HTTP_201_CREATED)
#         return Response(serializedgenre.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PATCH'])
# def film_theaters_list(request, pk, format=None):
#     """
#     List all snippets for theaters with a film.
#     """
#     try:
#         film = Film.objects.get(pk=pk)
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         theaters = film.theaters.all()
#         serializer = TheaterSerializer(theaters, many=True)
#         return Response(serializer.data)
#     if request.method == 'PATCH':
#         theater_id = int(request.data["theater"])
#         theater = Theater.objects.get(id=theater_id)
#         film.theaters.add(theater)
#         serializer = TheaterSerializer(theater)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
# @api_view(['GET', 'PATCH'])
# def theater_films_list(request, pk, format=None):
#     """
#     List all snippets for a theater's films.
#     """
#     try:
#         theater = Theater.objects.get(pk=pk)
#     except Theater.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         films = theater.film_set.all()
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data)
#     if request.method == 'PATCH':
#         film_id = int(request.data["film"])
#         film = Film.objects.get(id=film_id)
#         theater.film_set.add(film)
#         serializer = FilmSerializer(film)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
#
#
#
# @api_view(['GET', 'PATCH'])
# def film_genre_list(request, pk, format=None):
#     """
#     List all snippets for a film's genre.
#     """
#     try:
#         film = Film.objects.get(pk=pk)
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         genre = film.genre
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data)
#     if request.method == 'PATCH':
#         genre_id = int(request.data["genre"])
#         genre = Genre.objects.get(id=genre_id)
#         film.genre = genre
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
# @api_view(['GET', 'PATCH'])
# def genre_films_list(request, pk, format=None):
#     """
#     List all snippets for films in specific genre.
#     """
#     try:
#         genre = Genre.objects.get(pk=pk)
#     except Genre.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         films = genre.film_set.all()
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data)
#     if request.method == 'PATCH':
#         film_id = int(request.data["film"])
#         film = Film.objects.get(id=film_id)
#         genre.film_set.add(film)
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
#
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def theater_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a theater instance.
#     """
#     try:
#         theater = Theater.objects.get(pk=pk)
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TheaterSerializer(theater)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TheaterSerializer(theater, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         theater.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def genre_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a genre instance.
#     """
#     try:
#         genre = Genre.objects.get(pk=pk)
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = GenreSerializer(genre, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         genre.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
