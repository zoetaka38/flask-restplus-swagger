from flask_restplus import Namespace, fields, Resource

from project import db
from project.models import ToDo

# Namespaceの初期化と登録
todo_namespace = Namespace('todo', description='ToDoのエンドポイント')

# JSONモデルの定義
todo = todo_namespace.model('ToDo', {
    'user_id': fields.Integer(
        required=True,
        description='ToDoを登録したユーザーID',
        example=0
    ),
    'id': fields.Integer(
        required=True,
        description='ToDoのID',
        example=1
    ),
    'title': fields.String(
        required=True,
        description='ToDoタイトル',
        example='起きる'
    ),
    'description': fields.String(
        required=True,
        description='ToDoの詳細',
        example='朝7時に起きたい'
    )
})


# Endpoints
@todo_namespace.route('/')
class ToDoList(Resource):
    # todoモデルを利用して結果をパースしてリストで返す
    @todo_namespace.marshal_list_with(todo)
    def get(self):
        """
        一覧取得
        """
        return ToDo.query.all()

    @todo_namespace.marshal_with(todo)
    @todo_namespace.expect(todo, validate=True)
    def post(self):
        """
        ToDo登録
        """
        # ちょっとやっかいなので実装はまた今度
        pass


@todo_namespace.route('/<int:todo_id>')
class ToDoController(Resource):
    # todoモデルを利用して結果をパースして単体で返す
    @todo_namespace.marshal_with(todo)
    def get(self, todo_id):
        """
        ToDo詳細
        """
        # ただし1個も見つからなかったら404を返す
        return ToDo.query.filter(ToDo.id == todo_id).first_or_404()

    def delete(self, todo_id):
        """
        ToDo削除
        """
        # 見つからなかったときの処理してないけど許して
        target_todo = ToDo.query.filter(ToDo.id == todo_id).first()
        db.session.delete(target_todo)
        return {'message': 'Success'}, 200

