from flask import Flask
from config import DevConfig,Config
from flask_bootstrap import Bootstrap

app =Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(DevConfig)
app.config.from_object(Config)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

