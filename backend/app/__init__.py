from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()


def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins=app.config['CORS_ORIGINS'], supports_credentials=True)
    
    # Register blueprints
    from app.routes import auth, articles, users, categories, tags, summary, bookmarks
    
    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    app.register_blueprint(articles.bp, url_prefix='/api/articles')
    app.register_blueprint(users.bp, url_prefix='/api/users')
    app.register_blueprint(categories.bp, url_prefix='/api/categories')
    app.register_blueprint(tags.bp, url_prefix='/api/tags')
    app.register_blueprint(summary.bp, url_prefix='/api')
    app.register_blueprint(bookmarks.bp, url_prefix='/api/bookmarks')
    
    # Health check endpoint
    @app.route('/api/health')
    def health():
        return {'status': 'ok', 'message': 'EzNews2 API is running'}
    
    return app
