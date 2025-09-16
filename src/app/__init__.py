from flask import Flask
from flask_login import LoginManager
from src.app.config import Config
from src.app.models import db, Usuarios

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # CONFIGURAÇÃO O FLASK-LOGIN
    lm = LoginManager()
    
    lm.init_app(app)
    lm.login_view = "auth.login"
    lm.login_message = "Acesso negado, faça o login primeiro."
    lm.login_message_category = "danger"
    
    @lm.user_loader
    def load_user(id):
        return Usuarios.query.get(int(id))
    
    # REGISTRANDO BLUEPRINTS
    
    from src.app.routes.home import home_route
    from src.app.routes.auth import auth_route
    
    app.register_blueprint(home_route)
    app.register_blueprint(auth_route)
    
    return app