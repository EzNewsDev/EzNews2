# EzNews2 Backend - Flask API

Backend API untuk aplikasi portal berita EzNews2 menggunakan Flask, SQLAlchemy, dan MySQL.

## Tech Stack

- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **MySQL** - Database
- **Flask-JWT-Extended** - JWT authentication
- **Flask-CORS** - Cross-origin resource sharing
- **ReportLab** - PDF generation

## Prerequisites

- Python 3.8+
- MySQL 8.0+
- pip

## Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and update the values:

```bash
copy .env.example .env
```

Edit `.env` file:
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=eznews2
JWT_SECRET_KEY=your-secret-key
```

### 3. Create Database

Create a new MySQL database:

```sql
CREATE DATABASE eznews2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Seed Database

Run the seeder to create tables and populate with sample data:

```bash
python seed.py
```

This will create:
- Admin user: `admin@eznews.com` / `Admin123!`
- Regular user: `user@eznews.com` / `User123!`
- 7 categories
- 8 tags
- 15 Indonesian news articles
- Sample bookmarks

### 5. Run Development Server

```bash
python run.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user
- `POST /api/auth/forgot-password` - Request password reset
- `POST /api/auth/reset-password` - Reset password with token

### Articles
- `GET /api/articles` - List articles (with search & pagination)
- `GET /api/articles/:id` - Get article detail
- `POST /api/articles` - Create article (admin only)
- `PUT /api/articles/:id` - Update article (admin only)
- `DELETE /api/articles/:id` - Delete article (admin only)
- `GET /api/articles/:id/export?format=pdf|txt` - Export article

### Users
- `GET /api/users/profile` - Get user profile
- `PUT /api/users/profile` - Update profile
- `PUT /api/users/password` - Change password
- `GET /api/users` - List all users (admin only)
- `DELETE /api/users/:id` - Delete user (admin only)

### Categories
- `GET /api/categories` - List categories
- `POST /api/categories` - Create category (admin only)
- `PUT /api/categories/:id` - Update category (admin only)
- `DELETE /api/categories/:id` - Delete category (admin only)

### Tags
- `GET /api/tags` - List tags
- `POST /api/tags` - Create tag (admin only)
- `PUT /api/tags/:id` - Update tag (admin only)
- `DELETE /api/tags/:id` - Delete tag (admin only)

### Bookmarks
- `GET /api/bookmarks` - Get user bookmarks
- `POST /api/bookmarks` - Add bookmark
- `DELETE /api/bookmarks/:id` - Remove bookmark

### AI Summary
- `POST /api/summarize` - Generate AI summary with filters

## Project Structure

```
backend/
├── app/
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # API route handlers
│   ├── services/        # Business logic
│   └── utils/           # Helper functions
├── config.py            # Configuration
├── run.py              # Application entry point
├── seed.py             # Database seeder
└── requirements.txt    # Dependencies
```

## Database Schema

- **users**: User accounts with roles (admin/user)
- **categories**: Article categories
- **tags**: Article tags
- **articles**: News articles
- **article_tags**: Many-to-many relationship
- **bookmarks**: User bookmarks
- **admin_logs**: Admin action audit trail

## Authentication

Uses JWT tokens. Include token in Authorization header:
```
Authorization: Bearer <token>
```

## Docker Support

Environment variables are used for all configuration (database, secrets) to support Docker deployment.
