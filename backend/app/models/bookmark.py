from app import db
from datetime import datetime


class Bookmark(db.Model):
    __tablename__ = 'bookmarks'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Unique constraint to prevent duplicate bookmarks
    __table_args__ = (db.UniqueConstraint('user_id', 'article_id', name='unique_user_article_bookmark'),)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'article': self.article.to_dict(include_content=False),
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
