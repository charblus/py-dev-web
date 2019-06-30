# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# from MeiziSerializer import serializers
# from MeiziSerializer import MeiziSerializer

from .models import Person, UserInfo
import time
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


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
# 默认情况下，只有 GET 方法会被接受。其他方法将以 "405 Method Not Allowed" 进行响应。要使用其他方法，请指定视图允许的方法


@api_view(['GET', 'POST'])
def clock(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) })
    