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

#  python manage.py inspectdb
# 这是一个自动生成的django模型模块。
# 您必须手动执行以下操作才能清除此问题：
# *重新排列模型顺序
# *确保每个模型都有一个主关键字为真的字段
# * 确保每个foreignkey的“on-delete”设置为所需的行为。
# *如果希望允许Django创建、修改和删除表，请删除“managed=false”行。
# 请随意重命名模型，但不要重命名db_表值或字段名。
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PyserverArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    body = models.TextField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pyServer_article'


class PyserverPerson(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pyServer_person'


class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    mobile_phone = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    register_time = models.DateTimeField()

    class Meta:
        db_table = 'user_info'