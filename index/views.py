#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/3/1 18:02'
@email = 'qjyyn@qq.com'
'''
from flask import jsonify
from flaskTemplate.tasks import celery_tasks
from public.views import login_required
from flask import request

# celery 启动
# export FORKED_BY_MULTIPROCESSING=1
# celery.exe worker -A flaskTemplate.tasks --loglevel=info

@login_required
def index():
    return jsonify({"status": 0, "msg": "验证后打开首页!", "data": ""})

def celery_task():
    arg = request.args.get('arg')
    task = celery_tasks.delay(arg)
    return jsonify({"status": 0, "msg": "发布成功!", "data": task.id})