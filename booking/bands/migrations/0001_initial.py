# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-07 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('booking_fee', models.FloatField(default=0)),
                ('bio', models.TextField()),
                ('raider', models.TextField()),
                ('contact', models.EmailField(max_length=254)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Bands',
                'verbose_name': 'Band',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Genres',
                'verbose_name': 'Genre',
            },
        ),
        migrations.AddField(
            model_name='bands',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.Genre'),
        ),
    ]
