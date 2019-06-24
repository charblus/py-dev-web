# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Person
# Create your views here.
def index(request):
  return HttpResponse(u"逍遥超儿")

def create(request):
  Person.objects.create(name='xiaoli', age=18)
  s = Person.objects.get(name='xiaoli')
  return HttpResponse(str(s))
