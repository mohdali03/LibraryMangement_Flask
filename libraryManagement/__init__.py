from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_jwt_extended import JWTManager
db = SQLAlchemy()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    
    
    from .books.routes import books
    from .Member.routes import member
    from .author.routes import author
    from .auth.routes import auth
    app.register_blueprint(books)
    app.register_blueprint(auth)
    app.register_blueprint(member)
    app.register_blueprint(author)

    return app