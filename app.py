from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login  import current_user
# import pymysql

from datetime import datetime as dt

db = SQLAlchemy()
bcrypt = Bcrypt()
# pymysql.install_as_MySQLdb()
app = Flask(__name__)


def create_app(test_config=None):
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    # survey.db
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///survey.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'warning'
    login_manager.init_app(app)
    import model
    @login_manager.user_loader
    def load_user(user_id):
        return model.User.query.get(int(user_id))

    # Register blueprints:
    import main
    import auth
    import errors

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(errors.error)
    return app
