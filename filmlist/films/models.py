from __future__ import unicode_literals

from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('title',)
