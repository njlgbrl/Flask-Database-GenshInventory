from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

dbase = SQLAlchemy(app)
migrate = Migrate(app, dbase)

loginManager = LoginManager(app)
loginManager.init_app(app)
loginManager.login_view = 'login'

from app import views, models
from app.users import users
from app.merchants import merchant

app.register_blueprint(users)
app.register_blueprint(merchant)