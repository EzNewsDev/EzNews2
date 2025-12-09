from app import create_app
from app.models.article import Article

app = create_app()

with app.app_context():
    article = Article.query.get(1)
    if article:
        print(f"Article: {article.title}")
        print(f"Tags (DB): {[tag.name for tag in article.tags]}")
        print(f"To Dict: {article.to_dict()['tags']}")
    else:
        print("Article 1 not found")
