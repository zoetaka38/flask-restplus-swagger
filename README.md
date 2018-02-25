# Flask + RESTPlus + SwaggerAPI

FlaskとRESTPlusを使って、RESTFulAPIを作成し、Swagger定義書の公開までを行うためのフレームワーク・テンプレート

## お試し方法

```bash
git clone https://github.com/zoetaka38/flask-restplus-swagger.git
cd flask-restplus-swagger
docker-compose up --build
```

## 開発方法

1. テストの記述
    * `project/tests/test*.py`として作成します。
2. DB構造の定義
    * `project/models`以下に作成します。
3. NamespaceとJSONモデルの定義
    * `project/api/*.py`として作成します。
4. エンドポイントの追加
    * 3番のファイルにエンドポイントを追加します。


