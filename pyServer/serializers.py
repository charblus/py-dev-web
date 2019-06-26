# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import UserInfo
class userinfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserInfo
    fields = ('name','mobile_phone','gender','email','register_time')
