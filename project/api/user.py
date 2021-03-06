from flask_restplus import Namespace, fields, Resource

from project.api.api import api

# Namespaceの初期化と登録
from project.api.todo import todo
from project import db
from project.models import User, ToDo

user_namespace = Namespace('users', description='ユーザー関連のエンドポイント')

# JSONモデルの定義
user = user_namespace.model('User', {
    'id': fields.Integer(
        required=True,
        description='',
        example=0
    ),
    'name': fields.String(
        required=True,
        description='',
        example='Aruneko'
    ),
    'email': fields.String(
        required=True,
        description='',
        example='aruneko@example.com'
    )
})


@user_namespace.route('/')
class UserList(Resource):
    @user_namespace.marshal_list_with(user)
    def get(self):
        """
        ユーザー一覧
        """
        return User.query.all()

    @user_namespace.marshal_with(user)
    @user_namespace.expect(user)
    def post(self):
        """
        ユーザー登録
        """
        userdata = User(
            id=api.payload['id'],
            name=api.payload['name'],
            email=api.payload['email'],
        )
        db.session.add(userdata)
        db.session.commit()
        return api.payload


@user_namespace.route('/<int:user_id>')
class UserController(Resource):
    @user_namespace.marshal_with(user)
    def get(self, user_id):
        """
        ユーザー詳細
        """
        return User.query.filter(User.id == user_id).first_or_404()

    def delete(self, user_id):
        """
        ユーザー削除
        """
        target_user = User.query.filter(User.id == user_id).first()
        db.session.delete(target_user)
        return {'message': 'Success'}, 200


@user_namespace.route('/<int:user_id>/todo')
class ToDoByUser(Resource):
    @user_namespace.marshal_list_with(todo)
    def get(self, user_id):
        """
        ユーザーごとのToDo取得
        """
        return ToDo.query.filter(ToDo.user_id == user_id).all()