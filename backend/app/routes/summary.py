from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.article import Article
from app.services.ai_summary import generate_summary

bp = Blueprint('summary', __name__)


@bp.route('/summarize', methods=['POST'])
@jwt_required()
def create_summary():
    """Generate AI summary for article"""
    try:
        data = request.get_json()
        
        # Get content
        content = None
        if data.get('article_id'):
            article = Article.query.get(data['article_id'])
            if not article:
                return jsonify({'error': 'Article not found'}), 404
            content = article.content
        elif data.get('content'):
            content = data['content']
        else:
            return jsonify({'error': 'Either article_id or content is required'}), 400
        
        # Get filters
        filters = data.get('filters', ['who', 'when', 'where', 'what', 'why', 'how'])
        length = data.get('length', 'medium')
        
        # Generate summary
        summary = generate_summary(content, filters, length)
        
        return jsonify(summary), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
