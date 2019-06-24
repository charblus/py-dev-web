# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-22 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]