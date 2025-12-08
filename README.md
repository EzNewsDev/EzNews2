# EzNews2 - Full-Stack News Portal

Portal berita lengkap dengan fitur AI Summary, bookmark, export, dan manajemen admin.

## 🚀 Tech Stack

### Backend
- **Flask** - Web framework Python
- **SQLAlchemy** - ORM untuk MySQL
- **MySQL** - Database
- **JWT** - Authentication
- **ReportLab** - PDF generation

### Frontend
- **React 18** - UI library
- **Tailwind CSS** - Styling (matching Figma design)
- **React Router** - Navigation
- **Axios** - HTTP client

## 📋 Features

### User Features
- ✅ Register & Login (JWT-based)
- ✅ Browse & Search News
- ✅ Read Full Articles
- ✅ AI Summary with Filters (Who/When/Where/What/Why/How)
- ✅ Bookmark Articles
- ✅ Export Articles (PDF/TXT)
- ✅ Profile Management
- ✅ Forgot Password Flow

### Admin Features
- ✅ Article CRUD
- ✅ Category & Tag Management
- ✅ User Management
- ✅ Admin Action Logging

### Design
- ✅ Figma-based Auth Pages
- ✅ Light/Dark Mode
- ✅ Responsive Design
- ✅ HCI Principles
- ✅ Accessibility (ARIA, keyboard navigation)

## 🐳 Quick Start with Docker (Recommended)

### Prerequisites
- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Docker Compose

### Start Application
```bash
# Clone and navigate to project
cd EzNews2

# Start all services (MySQL + Backend + Frontend)
docker-compose up

# Or run in background
docker-compose up -d
```

**That's it!** Access:
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000

**Default Login:**
- Admin: admin@eznews.com / Admin123!
- User: user@eznews.com / User123!

See [DOCKER.md](DOCKER.md) for complete Docker guide.

---

## 🛠️ Manual Setup (Without Docker)

### Prerequisites
- Python 3.8+
- Node.js 18+
- MySQL 8.0+

### Backend Setup

1. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Configure environment:
```bash
copy .env.example .env
# Edit .env with your database credentials
```

3. Create database:
```sql
CREATE DATABASE eznews2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. Seed database:
```bash
python seed.py
```

5. Run server:
```bash
python run.py
```

Backend will run at `http://localhost:5000`

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run development server:
```bash
npm run dev
```

Frontend will run at `http://localhost:5173`

---

## 👤 Default Accounts

After seeding the database:

- **Admin**: admin@eznews.com / Admin123!
- **User**: user@eznews.com / User123!

## 📁 Project Structure

```
EzNews2/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic
│   │   └── utils/           # Helpers
│   ├── Dockerfile           # Backend container
│   ├── config.py
│   ├── run.py
│   ├── seed.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── contexts/        # State management
│   │   ├── pages/          # Pages
│   │   ├── utils/          # API client
│   │   └── index.css       # Tailwind styles
│   ├── Dockerfile           # Frontend container
│   ├── package.json
│   └── tailwind.config.js
├── docker-compose.yml       # Docker orchestration
├── DOCKER.md               # Docker guide
└── README.md
```

## 🎨 Design System

The application uses the Figma design system with:
- **Primary Color**: Navy Blue (#2E3B7D)
- **Secondary Color**: Light Blue (#3B9DD9)
- **Decorative Patterns**: Geometric circles
- **Typography**: Inter font family
- **Components**: Matching Figma auth pages

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Current user
- `POST /api/auth/forgot-password` - Request reset
- `POST /api/auth/reset-password` - Reset password

### Articles
- `GET /api/articles` - List with search & pagination
- `GET /api/articles/:id` - Detail
- `POST /api/articles` - Create (admin)
- `PUT /api/articles/:id` - Update (admin)
- `DELETE /api/articles/:id` - Delete (admin)
- `GET /api/articles/:id/export` - Export PDF/TXT

### Bookmarks
- `GET /api/bookmarks` - User bookmarks
- `POST /api/bookmarks` - Add bookmark
- `DELETE /api/bookmarks/:id` - Remove

### AI Summary
- `POST /api/summarize` - Generate summary with filters

See `backend/README.md` for complete API documentation.

## 🔒 Security

- ✅ Password hashing (Werkzeug)
- ✅ JWT authentication
- ✅ Role-based access control
- ✅ Input validation & sanitization
- ✅ CORS configuration
- ✅ Environment variables for secrets

## 📱 Responsive Design

The application is fully responsive:
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🐳 Docker Deployment

See [DOCKER.md](DOCKER.md) for:
- Docker setup guide
- Docker commands
- Development workflow with containers
- Database management
- Troubleshooting

## 📝 Sample Data

The database seeder includes:
- 15 realistic Indonesian news articles
- 7 categories (Politik, Ekonomi, Teknologi, Olahraga, Kesehatan, Hiburan, Pendidikan)
- 8 tags
- 2 user accounts (admin & regular user)
- Sample bookmarks

## 🚧 Development Status

- ✅ Backend API (100%)
- ✅ Authentication System (100%)
- ✅ Database & Seeder (100%)
- ✅ Frontend Infrastructure (100%)
- ✅ Auth Pages (100% - Figma-based)
- ✅ Docker Setup (100%)
- 🚧 Public Pages (Home completed, others stubbed)
- 🚧 User Pages (Stubbed)
- 🚧 Admin Pages (Stubbed)

## 📖 Documentation

- [DOCKER.md](DOCKER.md) - Docker deployment guide
- [backend/README.md](backend/README.md) - Backend API documentation
- [frontend/README.md](frontend/README.md) - Frontend documentation

## 📖 License

© 2024 EzNews. All rights reserved.
