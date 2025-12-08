from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.article import Article
from app.models.category import Category
from app.models.tag import Tag
from app.models.user import User
from app.models.admin_log import AdminLog
from app.utils.auth_helpers import admin_required, get_current_user
from app.utils.validators import validate_article_data
from app.services.export import generate_article_pdf, generate_article_txt
from datetime import datetime
from io import BytesIO
import math

bp = Blueprint('articles', __name__)


@bp.route('', methods=['GET'])
def get_articles():
    """Get articles with search and pagination"""
    try:
        # Get query parameters
        search = request.args.get('search', '')
        category_id = request.args.get('category_id', type=int)
        date_from = request.args.get('date_from')
        date_to = request.args.get('date_to')
        page = request.args.get('page', 1, type=int)
        page_size = request.args.get('limit', 10, type=int)
        
        # Build query
        query = Article.query
        
        # Apply filters
        if search:
            query = query.filter(
                (Article.title.contains(search)) | 
                (Article.content.contains(search))
            )
        
        if category_id:
            query = query.filter_by(category_id=category_id)
        
        if date_from:
            date_from_obj = datetime.fromisoformat(date_from.replace('Z', '+00:00'))
            query = query.filter(Article.published_date >= date_from_obj)
        
        if date_to:
            date_to_obj = datetime.fromisoformat(date_to.replace('Z', '+00:00'))
            query = query.filter(Article.published_date <= date_to_obj)
        
        # Sort by published date (newest first)
        query = query.order_by(Article.published_date.desc())
        
        # Get current user for bookmark status
        current_user = get_current_user()
        user_id = current_user.id if current_user else None
        
        # Paginate
        total = query.count()
        total_pages = math.ceil(total / page_size)
        articles = query.offset((page - 1) * page_size).limit(page_size).all()
        
        return jsonify({
            'items': [article.to_dict(include_content=False, user_id=user_id) for article in articles],
            'total': total,
            'page': page,
            'limit': page_size,
            'pages': total_pages
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """Get single article by ID"""
    try:
        article = Article.query.get(article_id)
        
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        
        # Get current user for bookmark status
        current_user = get_current_user()
        user_id = current_user.id if current_user else None
        
        return jsonify(article.to_dict(include_content=True, user_id=user_id)), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('', methods=['POST'])
@admin_required
def create_article():
    """Create new article (admin only)"""
    try:
        data = request.get_json()
        
        # Validate
        errors = validate_article_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Create article
        article = Article(
            title=data['title'],
            content=data['content'],
            category_id=data['category_id'],
            author_name=data['author_name'],
            source_url=data.get('source_url'),
            image_url=data.get('image_url'),
            published_date=datetime.fromisoformat(data['published_date'].replace('Z', '+00:00'))
        )
        
        # Add tags
        if data.get('tag_ids'):
            tags = Tag.query.filter(Tag.id.in_(data['tag_ids'])).all()
            article.tags = tags
        
        db.session.add(article)
        db.session.commit()
        
        # Log admin action
        email = get_jwt_identity()
        admin = User.query.filter_by(email=email).first()
        log = AdminLog(
            admin_user_id=admin.id,
            action_type='CREATE',
            article_id=article.id,
            description=f'Created article: {article.title}'
        )
        db.session.add(log)
        db.session.commit()
        
        return jsonify({
            'message': 'Article created successfully',
            'article': article.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:article_id>', methods=['PUT'])
@admin_required
def update_article(article_id):
    """Update article (admin only)"""
    try:
        article = Article.query.get(article_id)
        
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        
        data = request.get_json()
        
        # Update fields
        if 'title' in data:
            article.title = data['title']
        if 'content' in data:
            article.content = data['content']
        if 'category_id' in data:
            article.category_id = data['category_id']
        if 'author_name' in data:
            article.author_name = data['author_name']
        if 'source_url' in data:
            article.source_url = data['source_url']
        if 'image_url' in data:
            article.image_url = data['image_url']
        if 'published_date' in data:
            article.published_date = datetime.fromisoformat(data['published_date'].replace('Z', '+00:00'))
        
        # Update tags
        if 'tag_ids' in data:
            tags = Tag.query.filter(Tag.id.in_(data['tag_ids'])).all()
            article.tags = tags
        
        db.session.commit()
        
        # Log admin action
        email = get_jwt_identity()
        admin = User.query.filter_by(email=email).first()
        log = AdminLog(
            admin_user_id=admin.id,
            action_type='UPDATE',
            article_id=article.id,
            description=f'Updated article: {article.title}'
        )
        db.session.add(log)
        db.session.commit()
        
        return jsonify({
            'message': 'Article updated successfully',
            'article': article.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:article_id>', methods=['DELETE'])
@admin_required
def delete_article(article_id):
    """Delete article (admin only)"""
    try:
        article = Article.query.get(article_id)
        
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        
        title = article.title
        
        # Log admin action before deleting
        email = get_jwt_identity()
        admin = User.query.filter_by(email=email).first()
        log = AdminLog(
            admin_user_id=admin.id,
            action_type='DELETE',
            description=f'Deleted article: {title}'
        )
        db.session.add(log)
        
        db.session.delete(article)
        db.session.commit()
        
        return jsonify({'message': 'Article deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:article_id>/export', methods=['GET'])
@jwt_required()
def export_article(article_id):
    """Export article as PDF or TXT"""
    try:
        article = Article.query.get(article_id)
        
        if not article:
            return jsonify({'error': 'Article not found'}), 404
        
        format_type = request.args.get('format', 'pdf')  # pdf or txt
        include_summary = request.args.get('include_summary', 'false').lower() == 'true'
        
        # Get summary data if requested
        summary_data = None
        if include_summary and request.args.get('summary'):
            import json
            summary_data = json.loads(request.args.get('summary'))
        
        if format_type == 'pdf':
            pdf_data = generate_article_pdf(article, include_summary, summary_data)
            return send_file(
                BytesIO(pdf_data),
                mimetype='application/pdf',
                as_attachment=True,
                download_name=f'{article.title[:50]}.pdf'
            )
        else:  # txt
            txt_data = generate_article_txt(article, include_summary, summary_data)
            return send_file(
                BytesIO(txt_data),
                mimetype='text/plain',
                as_attachment=True,
                download_name=f'{article.title[:50]}.txt'
            )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
