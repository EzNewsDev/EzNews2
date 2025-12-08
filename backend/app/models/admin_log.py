from app import db
from datetime import datetime


class AdminLog(db.Model):
    __tablename__ = 'admin_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    admin_user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    action_type = db.Column(db.String(50), nullable=False)  # CREATE, UPDATE, DELETE
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id', ondelete='SET NULL'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'admin_user': {
                'id': self.admin_user.id,
                'name': self.admin_user.full_name
            } if self.admin_user else None,
            'action_type': self.action_type,
            'article_id': self.article_id,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
