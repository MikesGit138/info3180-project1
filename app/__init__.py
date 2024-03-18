from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')
db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db) 
from app import views