#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    @Time    : 2019/3/2 14:54
#    @Author  : Redheat
#    @Site    :
#    @File    : tasks.py
#    @Software: PyCharm
from celery import Celery

celery_app = Celery()
celery_app.config_from_object("flaskTemplate.settings")

@celery_app.task
def celery_tasks(arg):
    print("celery 后端程序:{}".format(arg))
    return True
