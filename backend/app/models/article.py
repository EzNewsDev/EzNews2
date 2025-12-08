from app import db
from datetime import datetime
from app.models.tag import article_tags


class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    author_name = db.Column(db.String(100), nullable=False)
    source_url = db.Column(db.String(500), nullable=True)
    published_date = db.Column(db.DateTime, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    tags = db.relationship('Tag', secondary=article_tags, lazy='subquery',
                          backref=db.backref('articles', lazy=True))
    bookmarks = db.relationship('Bookmark', backref='article', lazy=True, cascade='all, delete-orphan')
    admin_logs = db.relationship('AdminLog', backref='article', lazy=True)
    
    def to_dict(self, include_content=True, user_id=None):
        """Convert to dictionary"""
        from app.models.bookmark import Bookmark
        
        result = {
            'id': self.id,
            'title': self.title,
            'category': self.category.to_dict() if self.category else None,
            'image_url': self.image_url,
            'author_name': self.author_name,
            'source_url': self.source_url,
            'published_date': self.published_date.isoformat() if self.published_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'tags': [tag.to_dict() for tag in self.tags],
            'is_bookmarked': False
        }
        
        if include_content:
            result['content'] = self.content
        
        # Check if bookmarked by user
        if user_id:
            bookmark = Bookmark.query.filter_by(user_id=user_id, article_id=self.id).first()
            result['is_bookmarked'] = bookmark is not None
        
        return result
