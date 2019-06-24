# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length = 200)
  url = models.CharField(max_length = 200)
  body = models.TextField()
  create_date = models.DateTimeField()

  def __unicode__(self):
    return self.title

class Person(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()

  def __unicode__(self):
    return self.name