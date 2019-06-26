# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from MeiziSerializer import serializers
# from MeiziSerializer import MeiziSerializer

from .models import Person, UserInfo
from pyServer.serializers import userinfoSerializer
# from pyServer import serializers as serializers
# Create your views here.
def index(request):
  return HttpResponse(u"逍遥超儿")

def create(request):
  Person.objects.create(name='xiaoli', age=18)
  s = Person.objects.get(name='xiaoli')
  return HttpResponse(str(s))

def userinfo(request):
  userinfo = UserInfo.objects.all()
  serializer = userinfoSerializer(userinfo, many=True)
  return HttpResponse(serializer.data)

