from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.bookmark import Bookmark
from app.models.article import Article
from app.models.user import User

bp = Blueprint('bookmarks', __name__)


@bp.route('', methods=['GET'])
@jwt_required()
def get_bookmarks():
    """Get user's bookmarks"""
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        bookmarks = Bookmark.query.filter_by(user_id=user.id).order_by(Bookmark.created_at.desc()).all()
        
        return jsonify({
            'bookmarks': [bookmark.to_dict() for bookmark in bookmarks]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('', methods=['POST'])
@jwt_required()
def add_bookmark():
    """Add bookmark"""
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        article_id = data.get('article_id')
        
        if not article_id:
            return jsonify({'error': 'Article ID is required'}), 400
        
        # Check if article exists
        article = Article.query.get(article_id)
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        
        # Check if already bookmarked
        existing = Bookmark.query.filter_by(user_id=user.id, article_id=article_id).first()
        if existing:
            return jsonify({'message': 'Article already bookmarked'}), 200
        
        # Create bookmark
        bookmark = Bookmark(
            user_id=user.id,
            article_id=article_id
        )
        
        db.session.add(bookmark)
        db.session.commit()
        
        return jsonify({
            'message': 'Bookmark added successfully',
            'bookmark': bookmark.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:article_id>', methods=['DELETE'])
@jwt_required()
def remove_bookmark(article_id):
    """Remove bookmark"""
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        bookmark = Bookmark.query.filter_by(user_id=user.id, article_id=article_id).first()
        
        if not bookmark:
            return jsonify({'error': 'Bookmark not found'}), 404
        
        db.session.delete(bookmark)
        db.session.commit()
        
        return jsonify({'message': 'Bookmark removed successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
