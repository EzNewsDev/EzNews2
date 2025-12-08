# EzNews2 Frontend - React + Tailwind CSS

Frontend aplikasi portal berita EzNews2 menggunakan React, React Router, dan Tailwind CSS.

## Tech Stack

- **React 18** - UI library
- **Vite** - Build tool & dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router DOM** - Routing
- **Axios** - HTTP client
- **React Toastify** - Notifications
- **date-fns** - Date formatting

## Prerequisites

- Node.js 18+
- npm or yarn

## Setup Instructions

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment

Copy `.env` and update if needed:

```
VITE_API_URL=http://localhost:5000/api
```

### 3. Run Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### 4. Build for Production

```bash
npm run build
```

Build output will be in `dist/` folder.

## Features

### Authentication Pages (Figma-based Design)
- ✅ Login page  with decorative patterns
- ✅ Register page with validation
- ✅ Forgot Password flow
- ✅ Social login UI (Google, Facebook)

### Design System
- **Colors**: Navy Blue (#2E3B7D) and Light Blue (#3B9DD9)
- **Decorative Patterns**: Geometric circles on side panels
- **Light/Dark Mode**: Theme toggle with localStorage persistence
- **Responsive**: Mobile, tablet, and desktop support

### Pages
- **Home**: Landing page with latest news
- **News List**: Browse and search articles
- **News Detail**: Read article with AI summary
- **Profile**: User profile management
- **Bookmarks**: User's saved articles
- **Admin Panel**: Article, category, tag, and user management

### Components
- Navbar with role-based navigation
- Logo component (EZN with plane icon)
- Decorative pattern component
- Protected routes (User & Admin)

## Project Structure

```
frontend/
├── src/
│   ├── components/      # Reusable components
│   ├── contexts/        # React contexts (Auth, Theme)
│   ├── pages/          # Page components
│   │   ├── Auth/       # Authentication pages
│   │   ├── User/       # User pages
│   │   └── Admin/      # Admin pages
│   ├── utils/          # Utilities (API client)
│   ├── App.jsx         # Main app with routing
│   ├── main.jsx        # Entry point
│   └── index.css       # Global styles
├── index.html
├── package.json
├── tailwind.config.js
└── vite.config.js
```

## Available Routes

### Public
- `/` - Home
- `/news` - News list
- `/news/:id` - News detail
- `/login` - Login
- `/register` - Register
- `/forgot-password` - Forgot password

### Protected (Logged in)
- `/profile` - User profile
- `/bookmarks` - User bookmarks

### Admin Only
- `/admin` - Admin dashboard
- `/admin/articles` - Article management
- `/admin/articles/new` - Create article
- `/admin/articles/edit/:id` - Edit article
- `/admin/categories` - Category management
- `/admin/tags` - Tag management
- `/admin/users` - User management

## Theme System

Toggle between light and dark modes using the theme switch in navbar. Preference is saved to localStorage.

## Authentication Flow

1. User registers or logs in
2. Backend returns JWT token
3. Token stored in localStorage
4. API client auto-includes token in requests
5. Protected routes check authentication
6. Admin routes verify admin role

## Next Steps for Full Implementation

The current implementation includes:
- ✅ Complete backend API
- ✅ Authentication system
- ✅ Figma-based auth pages
- ✅ Home page
- 🚧 News pages (stub)
- 🚧 User pages (stub)
- 🚧 Admin pages (stub)

To complete the application, enhance the stub pages with full CRUD functionality, search/filter UI, AI summary panel, bookmark actions, and export features.
