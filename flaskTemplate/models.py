#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/3/1 17:46'
@email = 'qjyyn@qq.com'
'''
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy

mongodb = MongoEngine()
mysqldb = SQLAlchemy()

class ParagraphContentMongo(mongodb.Document):
    tag = mongodb.StringField(max_length=50,null=False,verbose_name="标签")
    ptag = mongodb.StringField(max_length=50,default="",verbose_name="段落标签")
    cut = mongodb.IntField(default=0,verbose_name="分词")
    create = mongodb.DateTimeField(auto_now_add=True)

    meta = {'collection': 'nlp_paragraphcontentmongo'}

class UserToken(mysqldb.Model):
    id = mysqldb.Column(mysqldb.Integer, primary_key=True)
    token = mysqldb.Column(mysqldb.String(200))
    endtime = mysqldb.Column(mysqldb.Integer())
    user = mysqldb.Column(mysqldb.String(200))
