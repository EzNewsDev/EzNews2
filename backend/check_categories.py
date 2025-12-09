
from app import create_app, db
from app.models.category import Category

app = create_app()

with app.app_context():
    categories = Category.query.all()
    print(f"Total Categories: {len(categories)}")
    for cat in categories:
        print(f"- {cat.id}: {cat.name} ({cat.slug})")
