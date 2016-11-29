"""filmlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from films import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^films$', views.FilmList.as_view()),
    url(r'^films/(?P<pk>[0-9]+)$', views.FilmDetail.as_view()),
    # url(r'^films/(?P<pk>[0-9]+)/theaters$', views.film_theaters_list),
    url(r'^theaters$', views.TheaterList.as_view()),
    url(r'^theaters/(?P<pk>[0-9]+)$', views.TheaterDetail.as_view()),
    # url(r'^theaters/(?P<pk>[0-9]+)/films$', views.theater_films_list),
    url(r'^genres$', views.GenreList.as_view()),
    url(r'^genres/(?P<pk>[0-9]+)$', views.GenreDetail.as_view()),
    # url(r'^genres/(?P<pk>[0-9]+)/films$', views.genre_films_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
