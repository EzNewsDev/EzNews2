from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models.user import User


def admin_required(fn):
    """Decorator to require admin role"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        user = User.query.filter_by(email=identity).first()
        
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        
        return fn(*args, **kwargs)
    return wrapper


def get_current_user():
    """Get current authenticated user"""
    try:
        verify_jwt_in_request()
        identity = get_jwt_identity()
        return User.query.filter_by(email=identity).first()
    except:
        return None
