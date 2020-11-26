from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Bootstrap(app)
toolbar = DebugToolbarExtension(app)

# blueprint registration
from .main import bp as main_bp
app.register_blueprint(main_bp)
