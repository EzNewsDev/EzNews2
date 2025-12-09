from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.user import User
from email_validator import validate_email, EmailNotValidError
from app.utils.validators import validate_password_strength

bp = Blueprint('users', __name__)


@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get user profile"""
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify(user.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update user profile"""
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        
        # Update full name
        if 'full_name' in data and data['full_name'].strip():
            if len(data['full_name'].strip()) < 2:
                return jsonify({'error': 'Full name must be at least 2 characters'}), 400
            user.full_name = data['full_name'].strip()
        
        # Update email
        if 'email' in data and data['email'] != user.email:
            try:
                validate_email(data['email'])
                # Check if email already exists
                if User.query.filter_by(email=data['email']).first():
                    return jsonify({'error': 'Email already in use'}), 400
                user.email = data['email']
            except EmailNotValidError:
                return jsonify({'error': 'Invalid email format'}), 400
        
        # Update avatar
        if 'avatar_url' in data:
            user.avatar_url = data['avatar_url']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Profile updated successfully',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    """Change user password"""
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        
        # Validate old password
        if not user.check_password(data.get('old_password', '')):
            return jsonify({'error': 'Current password is incorrect'}), 400
        
        # Validate new password
        password_errors = validate_password_strength(data.get('new_password', ''))
        if password_errors:
            return jsonify({'error': password_errors[0]}), 400
        
        if data['new_password'] != data.get('confirm_new_password'):
            return jsonify({'error': 'New passwords do not match'}), 400
        
        # Update password
        user.set_password(data['new_password'])
        db.session.commit()
        
        return jsonify({'message': 'Password changed successfully'}), 200
        
        return jsonify({'message': 'Password changed successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('', methods=['GET'])
@jwt_required()
def get_users():
    """Get all users (admin only)"""
    try:
        email = get_jwt_identity()
        current_user = User.query.filter_by(email=email).first()
        
        if not current_user or current_user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        users = User.query.all()
        
        return jsonify({
            'users': [user.to_dict() for user in users]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    """Delete user (admin only)"""
    try:
        email = get_jwt_identity()
        current_user = User.query.filter_by(email=email).first()
        
        if not current_user or current_user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Prevent deleting self
        if user.id == current_user.id:
            return jsonify({'error': 'Cannot delete your own account'}), 400
        
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({'message': 'User deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
