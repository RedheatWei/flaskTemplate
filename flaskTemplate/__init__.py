#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/3/1 14:21'
@email = 'qjyyn@qq.com'
'''
import flask

app = flask.Flask(__name__)
app.config.from_pyfile("settings.py")

from flaskTemplate.models import mongodb, mysqldb

mongodb.init_app(app)
mysqldb.init_app(app)

from public.views import update_token
from index.views import index
from index.views import celery_task

app.add_url_rule('/index', view_func=index) #首页需要登录
app.add_url_rule('/celery_task', view_func=celery_task) #celery任务
app.add_url_rule('/update_token', view_func=update_token) #更新token
