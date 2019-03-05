#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/3/1 15:14'
@email = 'qjyyn@qq.com'
'''
from flaskTemplate.models import UserToken
from flask import current_app
from flask import jsonify
from flask import request
import functools
import time

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "token" not in current_app.config:
            update_token()
        current_token = request.args.get('token')
        app_token = current_app.config['token']
        if current_token in app_token and app_token[current_token]['endtime'] > time.time():
            return view(**kwargs)
        else:
            return jsonify({"status": '-400', "msg": "token不存在或过期！"})

    return wrapped_view


def update_token():
    user_token = UserToken.query.all()
    token_dict = {}
    for token in user_token:
        token_dict[token.token] = {"user": token.user, "endtime": token.endtime}
    current_app.config['token'] = token_dict
    return jsonify({"status": 0, "msg": "更新成功"})
