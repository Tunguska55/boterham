# __version__ = '0.1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import ProdConfig, DevConfig, TestConfig

app = Flask(__name__)

if app.config.get("FLASK_ENV") == "production":
    app.config.from_object(ProdConfig)
elif app.config.get("FLASK_ENV") == "testing":
    app.config.from_object(TestConfig)
else:
    app.config.from_object(DevConfig)

db = SQLAlchemy(app)

from boterham import routes