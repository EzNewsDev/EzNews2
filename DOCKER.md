# EzNews2 - Docker Deployment Guide

Complete guide untuk menjalankan EzNews2 menggunakan Docker dan Docker Compose.

## 📋 Prerequisites

Pastikan sudah terinstall:
- **Docker Desktop** (Windows/Mac) atau **Docker Engine** (Linux)
- **Docker Compose** (biasanya sudah include di Docker Desktop)

Cek instalasi:
```bash
docker --version
docker-compose --version
```

## 🚀 Quick Start

### 1. Clone Repository & Navigate
```bash
cd c:\xampp\htdocs\EzNews2
```

### 2. Start All Services
```bash
docker-compose up
```

Atau run di background:
```bash
docker-compose up -d
```

### 3. Access Application

Tunggu beberapa detik untuk seeding database, kemudian akses:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000
- **MySQL**: localhost:3307 (dari host machine)

### 4. Login

Default credentials setelah seeding:
- **Admin**: admin@eznews.com / Admin123!
- **User**: user@eznews.com / User123!

## 🛠️ Docker Commands

### Start Services
```bash
# Foreground (dengan logs)
docker-compose up

# Background
docker-compose up -d

# Rebuild containers
docker-compose up --build
```

### Stop Services
```bash
# Stop containers
docker-compose stop

# Stop dan remove containers
docker-compose down

# Stop, remove containers, dan hapus volumes (⚠️ data akan hilang)
docker-compose down -v
```

### View Logs
```bash
# All services
docker-compose logs

# Follow logs
docker-compose logs -f

# Specific service
docker-compose logs backend
docker-compose logs frontend
docker-compose logs mysql
```

### Run Commands in Containers
```bash
# Backend shell
docker-compose exec backend sh

# Re-seed database
docker-compose exec backend python seed.py

# Frontend shell
docker-compose exec frontend sh

# MySQL shell
docker-compose exec mysql mysql -u eznews_user -peznews_password eznews2
```

## 📦 Container Details

### MySQL Container
- **Image**: mysql:8.0
- **Container Name**: eznews2_mysql
- **Host Port**: 3307 → Container Port: 3306
- **Database**: eznews2
- **User**: eznews_user
- **Password**: eznews_password
- **Persistent Volume**: mysql_data

### Backend Container
- **Image**: Custom (Python 3.11)
- **Container Name**: eznews2_backend
- **Host Port**: 5000 → Container Port: 5000
- **Framework**: Flask + Gunicorn
- **Workers**: 4
- **Auto-reload**: Enabled (via volume mount)

### Frontend Container
- **Image**: Custom (Node.js 18)
- **Container Name**: eznews2_frontend
- **Host Port**: 5173 → Container Port: 5173
- **Build Tool**: Vite
- **Hot Reload**: Enabled (via volume mount)

## 🔄 Development Workflow

### Making Code Changes

**Frontend Changes:**
- Edit files di `./frontend/src/`
- Vite akan auto-reload (hot module replacement)
- Refresh browser untuk melihat perubahan

**Backend Changes:**
- Edit files di `./backend/`
- Gunicorn dengan `--reload` akan restart otomatis
- API changes langsung apply

**Database Changes:**
- Edit `seed.py` untuk ubah seed data
- Re-run seeder:
  ```bash
  docker-compose exec backend python seed.py
  ```

### Rebuild Containers

Jika ada perubahan di `Dockerfile` atau `requirements.txt` / `package.json`:

```bash
# Rebuild specific service
docker-compose up --build backend
docker-compose up --build frontend

# Rebuild all
docker-compose up --build
```

## 🗄️ Database Management

### Reset Database
```bash
# Stop containers
docker-compose down

# Remove volumes (⚠️ akan hapus semua data)
docker-compose down -v

# Start fresh
docker-compose up
```

### Backup Database
```bash
docker-compose exec mysql mysqldump -u eznews_user -peznews_password eznews2 > backup.sql
```

### Restore Database
```bash
docker-compose exec -T mysql mysql -u eznews_user -peznews_password eznews2 < backup.sql
```

### Access MySQL from Host
```bash
mysql -h 127.0.0.1 -P 3307 -u eznews_user -peznews_password eznews2
```

Atau gunakan GUI tools (MySQL Workbench, DBeaver, etc):
- Host: localhost
- Port: 3307
- User: eznews_user
- Password: eznews_password
- Database: eznews2

## 🌐 Network Configuration

All containers berada di network `eznews_network`:
- Backend dapat akses MySQL via hostname `mysql:3306`
- Frontend dapat akses Backend via `http://localhost:5000` (dari browser)
- Internal communication menggunakan Docker network

## 📝 Environment Variables

Environment variables di-manage via `docker-compose.yml`. Untuk custom configuration:

1. Copy `.env.docker` ke `.env`:
   ```bash
   copy .env.docker .env
   ```

2. Edit `.env` sesuai kebutuhan

3. Docker Compose akan auto-load `.env` file

## 🔒 Security Notes

**Development Setup:**
- Default passwords untuk development saja
- JWT secret simple
- Debug mode enabled

**Production Setup:**
- Ganti semua passwords dan secrets
- Set `FLASK_ENV=production`
- Gunakan reverse proxy (nginx)
- Enable HTTPS
- Gunakan Docker secrets untuk credentials

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Check what's using the port
netstat -ano | findstr :5173
netstat -ano | findstr :5000
netstat -ano | findstr :3307

# Change port in docker-compose.yml if needed
```

### Database Connection Failed
```bash
# Check MySQL health
docker-compose ps
docker-compose logs mysql

# Wait for MySQL to be ready (healthcheck)
# Backend auto-waits for MySQL healthcheck
```

### Frontend Can't Connect to Backend
- Ensure `VITE_API_URL` points to `http://localhost:5000/api`
- Check CORS settings in backend
- Check browser console for errors

### Container Keeps Restarting
```bash
# Check logs
docker-compose logs [service-name]

# Common issues:
# - Missing dependencies
# - Syntax errors in code
# - Database connection failed
```

### Clean Restart
```bash
# Nuclear option - remove everything
docker-compose down -v
docker system prune -a

# Rebuild from scratch
docker-compose up --build
```

## 📊 Resource Usage

Default configuration:
- **MySQL**: ~400MB RAM
- **Backend**: ~200MB RAM
- **Frontend**: ~300MB RAM
- **Total**: ~1GB RAM

Adjust di `docker-compose.yml` jika perlu:
```yaml
services:
  backend:
    deploy:
      resources:
        limits:
          memory: 512M
```

## 🚢 Production Deployment

Untuk production, gunakan:
1. Multi-stage build untuk frontend (static build)
2. nginx untuk serve frontend + reverse proxy
3. Docker secrets untuk credentials
4. External MySQL (managed service)
5. Logging & monitoring
6. Health checks
7. Auto-restart policies

Lihat `docker-compose.prod.yml` (jika ada) untuk production config.

## 👥 Team Collaboration

### Sharing Setup
Tim member hanya perlu:
```bash
git clone <repository>
cd EzNews2
docker-compose up
```

Tidak perlu install Python, Node.js, atau MySQL!

### Consistent Environment
Semua developer menggunakan:
- Same Python version (3.11)
- Same Node.js version (18)
- Same MySQL version (8.0)
- Same dependencies

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask with Docker](https://flask.palletsprojects.com/en/latest/deploying/)
- [Vite Docker Guide](https://vitejs.dev/guide/troubleshooting.html#dev-server)

---

Happy Coding! 🎉
