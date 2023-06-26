import os

from flask import Flask
from flask_session import Session



def cria_app():
    template_dir = os.path.abspath("./app/static/templates")
    app = Flask(__name__, template_folder=template_dir)
    app.config['SECRET_KEY'] = '1fjopiasiophjdawbhujiogdfnjk'
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    from .views import views
    
    app.register_blueprint(views, url_prefix="/")

    return app