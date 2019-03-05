#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/3/1 16:56'
@email = 'qjyyn@qq.com'
'''
SECRET_KEY = 'dev'
MONGODB_SETTINGS = {
    'db': 'flaskTemplate',
    'authentication_source': "admin",
    'host': 'mongodb',
    'port': 27017,
    'username': 'root',
    'password': 'root',
}
MYSQLDB_SETTINGS = {
    "username": "root",
    "password": "root",
    "port": 3306,
    "host": 'mysqldb',
    "db": "flaskTemplate",
}
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(MYSQLDB_SETTINGS['username'], MYSQLDB_SETTINGS['password'],
                                                          MYSQLDB_SETTINGS['host'], MYSQLDB_SETTINGS['port'],
                                                          MYSQLDB_SETTINGS['db'])
ES_HOST = 'elasticsearch'
ES_PORT = '9200'
#celery
BROKER_URL = 'amqp://root:root@rabbitmq//'
CELERY_RESULT_BACKEND = 'elasticsearch://%s:%s/celery_task/celery' % (ES_HOST, ES_PORT)
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

DEBUG = True