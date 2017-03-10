from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    owner = models.ForeignKey(
        'auth.User',
        related_name="genres",
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ('title',)

class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    owner = models.ForeignKey(
        'auth.User',
        related_name="theaters",
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ('state',)

class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='films', #instead of film_set, you can just use films
        on_delete=models.CASCADE,
        null=True
    )
    theaters = models.ManyToManyField(Theater)

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title
