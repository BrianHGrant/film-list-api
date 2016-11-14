from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('title',)

class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    class Meta:
        ordering = ('state',)

class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    theaters = models.ManyToManyField(Theater)

    class Meta:
        ordering = ('year_prod',)
