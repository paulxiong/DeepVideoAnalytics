# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdnapp', '0018_remove_annotation_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('tfgraph_url', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Indexer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('tfgraph_url', models.TextField(blank=True, default='')),
            ],
        ),
    ]