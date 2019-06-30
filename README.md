### python django 入坑指南

```
python -v    查看python 版本
python -m django --version  查看django 版本
```

[Anaconda 介绍、安装、使用及常用命令并介绍了conda pip virtualnev ](https://www.jianshu.com/p/f456f414bb3b)

## 开发
* [搭建django 项目 ]( https://www.jianshu.com/p/d671c8cb274f)
1.  `django-admin startproject 项目名称`  （注：项目名称  不支持_-分割符分开形式 推荐驼峰写法 ）
2.   创建程序app：`django-admin startapp 程序名称`  (一般一个项目有多个app, 当然通用的app也可以在多个项目中使用。)
3.   生成指定数据库SQL脚本：`python manage.py makemigrations`
4.   自动执行SQL脚本到数据库：`python manage.py migrate`
5.   创建超级管理员：`python mangae.py createsuperuser`
6.   运行程序：`python manage.py runserver`

```
pyDevWeb                        项目名称
├── pyDevWeb                    主项目文档
│   ├── __init__.py             网址入口，
│   ├── __init__.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   ├── urls.pyc
│   ├── wsgi.py
│   └── wsgi.pyc
├── pyServer                  一个app site 名称      
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── admin.py
│   ├── admin.pyc
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── models.pyc
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── README.md

```

```

Django 目录结构
urls.py
网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。
views.py
处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
models.py
与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。
forms.py
表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作，当然你也可以不使用。
templates 文件夹
views.py 中的函数渲染templates中的Html模板，得到动态内容的网页，当然可以用缓存来提高速度。
admin.py
后台，可以用很少量的代码就拥有一个强大的后台。
settings.py
Django 的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。
```


* 添加model（在app下的models.py创建表） 运行命令生成对应的表
```
python manage.py makemigrations    
# 1. 创建更改的文件
python manage.py migrate
# 2. 将生成py文件应用到数据库
python manage.py runserver
```
### 接口api
* rest-framework

```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```



## 库管理
安装插件 `pip install pymysql`

1. 各种库列表
* `pymysql ` 连接mysql
* `reqiests` 用reqiests get等方法下载网页
* `lxml` 用lxml etree 解析网页,在爬虫过程中，使用的是lxml的xpath查找对应的字段。
* `re` re模块：核心函数和方法 regex object  几乎所有的 re模块函数都可以作为 regex 对象的方法。(见下【Python各种库的说明】中)
 
 [Python各种库的说明](https://www.jianshu.com/p/2a39451845aa?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)


 ## FQA
 1. python中为什么加上中文注释就会报错
 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。python中默认的编码格式ASCII,(python菜鸟教程中python中文编码有解释) 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行:

 ```python
  #!/usr/bin/env python   //为了告诉Linux系统，这个是python可执行程序
  # _*_ coding:utf-8 _*_  //为了告诉python解释器，按照utf-8编码读取源代码，否则，你在源代码中写的中文输出可能会由乱码
```

注意：当你的代码中没有_*_ coding:utf-8_*_  时，你的代码中若存在中文注释，那么你执行这段代码时，你就会报错，因此在你写代码的时候，最好加上
`_*_ coding:utf-8 _*_ `
形成习惯


## ERRER
1. ` django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3`
> 这是说我版本低的意思吗 我明安装的最新的1.3.13 
网上查了下， 让我到`__init__.py`中加上
```python
# -*- coding: utf-8 -*-
import pymysql
pymysql.install_as_MySQLdb()  # 修复django找不到MySQLdb

```
然后执行
`python manage.py makemigrations`和`python manage.py migrate`同步数据库

然而还是报错 后来我把`__init__.py`加的注释一行 success
```python
# -*- coding: utf-8 -*-
import pymysql
# pymysql.install_as_MySQLdb()  # 修复django找不到MySQLdb

```
合着是我的写法是低版本的写法，迭


### api接口开发

[利用 Django REST framework 编写 RESTful API](https://www.cnblogs.com/bayueman/p/6647641.html)

[ API 指南（3-2）：基于方法的视图（@api_view()） ](https://www.jianshu.com/p/291450f2435c)


[Django接入Swagger，生成Swagger接口文档-操作解析](https://www.jianshu.com/p/c53de96f3ff1)


[django中文网](https://www.django.cn/course/show-27.html)


## 启动项目
```
conda info -e
激活py37环境  conda activate py37
退出环境     conda deactivate
python manage.py runserver
```