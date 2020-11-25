from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Bootstrap(app)

from ml_runner import views
