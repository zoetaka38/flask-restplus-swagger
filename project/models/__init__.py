# -*- coding: utf-8 -*-

import datetime

from project import db


# Userスキーマの定義
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(
            self, id, name, email,
            created_at=datetime.datetime.utcnow()):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at


# ToDoスキーマの定義
class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(
            self, id, user_id, title, description,
            created_at=datetime.datetime.utcnow()):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.created_at = created_at
