# -*- coding: utf-8 -*-


from project.api.todo import todo_namespace
from project.api.user import user_namespace
from project.api.api import api

api.add_namespace(todo_namespace)
api.add_namespace(user_namespace)