from flask import Blueprint, request, jsonify
from app import db
from app.models.category import Category
from app.utils.auth_helpers import admin_required

bp = Blueprint('categories', __name__)


@bp.route('', methods=['GET'])
def get_categories():
    """Get all categories with article counts"""
    try:
        from app.models.article import Article
        from sqlalchemy import func
        
        # Query categories with article count
        results = db.session.query(Category, func.count(Article.id).label('count')) \
            .outerjoin(Article) \
            .group_by(Category.id) \
            .all()
        
        categories_data = []
        for cat, count in results:
            data = cat.to_dict()
            data['article_count'] = count
            categories_data.append(data)
            
        # Sort by article count descending
        categories_data.sort(key=lambda x: x['article_count'], reverse=True)
            
        return jsonify({
            'categories': categories_data
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('', methods=['POST'])
@admin_required
def create_category():
    """Create category (admin only)"""
    try:
        data = request.get_json()
        
        if not data.get('name') or not data.get('slug'):
            return jsonify({'error': 'Name and slug are required'}), 400
        
        # Check if already exists
        if Category.query.filter_by(slug=data['slug']).first():
            return jsonify({'error': 'Category with this slug already exists'}), 400
        
        category = Category(
            name=data['name'],
            slug=data['slug']
        )
        
        db.session.add(category)
        db.session.commit()
        
        return jsonify({
            'message': 'Category created successfully',
            'category': category.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:category_id>', methods=['PUT'])
@admin_required
def update_category(category_id):
    """Update category (admin only)"""
    try:
        category = Category.query.get(category_id)
        
        if not category:
            return jsonify({'error': 'Category not found'}), 404
        
        data = request.get_json()
        
        if 'name' in data:
            category.name = data['name']
        
        if 'slug' in data:
            # Check if slug is taken by another category
            existing = Category.query.filter_by(slug=data['slug']).first()
            if existing and existing.id != category_id:
                return jsonify({'error': 'Slug already in use'}), 400
            category.slug = data['slug']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Category updated successfully',
            'category': category.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:category_id>', methods=['DELETE'])
@admin_required
def delete_category(category_id):
    """Delete category (admin only)"""
    try:
        category = Category.query.get(category_id)
        
        if not category:
            return jsonify({'error': 'Category not found'}), 404
        
        # Check if category has articles
        if category.articles:
            return jsonify({'error': 'Cannot delete category with existing articles'}), 400
        
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({'message': 'Category deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
