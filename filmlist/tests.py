from django.test import TestCase
from films.models import Film

# Create your tests here.
class FilmTestCase(TestCase):
    def GetFilms(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/films')
        assert response.status_code == 200
