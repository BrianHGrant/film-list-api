# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 04:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0007_auto_20161213_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genres', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='theater',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='theaters', to=settings.AUTH_USER_MODEL),
        ),
    ]
