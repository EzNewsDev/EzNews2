from app import create_app, db
from app.models import User, Article, Category, Tag, Bookmark, AdminLog

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Create shell context for flask shell command"""
    return {
        'db': db,
        'User': User,
        'Article': Article,
        'Category': Category,
        'Tag': Tag,
        'Bookmark': Bookmark,
        'AdminLog': AdminLog
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
