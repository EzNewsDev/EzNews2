import re
from email_validator import validate_email, EmailNotValidError


def validate_password_strength(password):
    """Validate password strength"""
    errors = []
    if len(password) < 8:
        errors.append('Password must be at least 8 characters')
    if not re.search(r'[A-Z]', password):
        errors.append('Password must contain at least one uppercase letter')
    if not re.search(r'[a-z]', password):
        errors.append('Password must contain at least one lowercase letter')
    if not re.search(r'\d', password):
        errors.append('Password must contain at least one number')
    if not re.search(r'[@$!%*?&]', password):
        errors.append('Password must contain at least one special character (@$!%*?&)')
    return errors


def validate_registration_data(data):
    """Validate user registration data"""
    errors = []
    
    # Check required fields
    if not data.get('full_name') or len(data.get('full_name', '').strip()) < 2:
        errors.append('Full name must be at least 2 characters')
    
    # Validate email
    try:
        validate_email(data.get('email', ''))
    except EmailNotValidError:
        errors.append('Invalid email format')
    
    # Validate password
    password = data.get('password', '')
    password_errors = validate_password_strength(password)
    errors.extend(password_errors)
    
    # Check password confirmation
    if password != data.get('confirm_password', ''):
        errors.append('Passwords do not match')
    
    return errors


def validate_article_data(data):
    """Validate article data"""
    errors = []
    
    if not data.get('title') or len(data.get('title', '').strip()) < 5:
        errors.append('Title must be at least 5 characters')
    
    if not data.get('content') or len(data.get('content', '').strip()) < 50:
        errors.append('Content must be at least 50 characters')
    
    if not data.get('category_id'):
        errors.append('Category is required')
    
    if not data.get('author_name') or len(data.get('author_name', '').strip()) < 2:
        errors.append('Author name is required')
    
    return errors
