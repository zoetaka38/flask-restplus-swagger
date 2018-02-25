#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# instantiate the extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    from project.api import api
    
    # set up extensions
    api.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    db.create_all(app=app)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app


if __name__ == '__main__':
    from flask.cli import FlaskGroup
    app = create_app()
    cli = FlaskGroup(create_app=create_app)
    cli()