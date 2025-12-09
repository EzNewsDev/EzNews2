from app import create_app
from app.models.user import User

app = create_app()
with app.app_context():
    user = User.query.filter_by(email='user@eznews.com').first()
    if user:
        print(f"User found: {user.email}")
        is_valid = user.check_password('User123!')
        print(f"Password 'User123!' valid: {is_valid}")
    else:
        print("User not found")
