# -*- coding: utf-8 -*-

from flask_restplus import Api


from project.api.todo import todo_namespace
from project.api.user import user_namespace

# API情報を指定して初期化
api = Api(
    title='Test API',
    version='1.0',
    description='Swaggerを統合したREST APIのサンプル'
)


api.add_namespace(todo_namespace)
api.add_namespace(user_namespace)