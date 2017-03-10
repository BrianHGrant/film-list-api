from django.contrib import admin

from films.models import Film, Theater, Genre

admin.site.register(Film)
admin.site.register(Theater)
admin.site.register(Genre)
