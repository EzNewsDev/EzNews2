from flask import Blueprint, request, jsonify
from app import db
from app.models.tag import Tag
from app.utils.auth_helpers import admin_required

bp = Blueprint('tags', __name__)


@bp.route('', methods=['GET'])
def get_tags():
    """Get all tags"""
    try:
        tags = Tag.query.all()
        return jsonify({
            'tags': [tag.to_dict() for tag in tags]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('', methods=['POST'])
@admin_required
def create_tag():
    """Create tag (admin only)"""
    try:
        data = request.get_json()
        
        if not data.get('name') or not data.get('slug'):
            return jsonify({'error': 'Name and slug are required'}), 400
        
        # Check if already exists
        if Tag.query.filter_by(slug=data['slug']).first():
            return jsonify({'error': 'Tag with this slug already exists'}), 400
        
        tag = Tag(
            name=data['name'],
            slug=data['slug']
        )
        
        db.session.add(tag)
        db.session.commit()
        
        return jsonify({
            'message': 'Tag created successfully',
            'tag': tag.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:tag_id>', methods=['PUT'])
@admin_required
def update_tag(tag_id):
    """Update tag (admin only)"""
    try:
        tag = Tag.query.get(tag_id)
        
        if not tag:
            return jsonify({'error': 'Tag not found'}), 404
        
        data = request.get_json()
        
        if 'name' in data:
            tag.name = data['name']
        
        if 'slug' in data:
            # Check if slug is taken by another tag
            existing = Tag.query.filter_by(slug=data['slug']).first()
            if existing and existing.id != tag_id:
                return jsonify({'error': 'Slug already in use'}), 400
            tag.slug = data['slug']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Tag updated successfully',
            'tag': tag.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:tag_id>', methods=['DELETE'])
@admin_required
def delete_tag(tag_id):
    """Delete tag (admin only)"""
    try:
        tag = Tag.query.get(tag_id)
        
        if not tag:
            return jsonify({'error': 'Tag not found'}), 404
        
        db.session.delete(tag)
        db.session.commit()
        
        return jsonify({'message': 'Tag deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
