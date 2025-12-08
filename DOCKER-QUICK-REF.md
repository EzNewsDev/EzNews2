# 🐳 Docker Quick Reference

## Start Application
```bash
docker-compose up        # Foreground with logs
docker-compose up -d     # Background (detached)
```

## Stop Application
```bash
docker-compose stop      # Stop containers
docker-compose down      # Stop and remove containers
docker-compose down -v   # Stop, remove containers + volumes (⚠️ deletes data)
```

## View Logs
```bash
docker-compose logs           # All services
docker-compose logs -f        # Follow logs (live)
docker-compose logs backend   # Specific service
```

## Rebuild
```bash
docker-compose up --build              # Rebuild all
docker-compose up --build backend      # Rebuild specific service
```

## Execute Commands
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

## Access Points
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000
- **MySQL**: localhost:3307

## Default Login
- **Admin**: admin@eznews.com / Admin123!
- **User**: user@eznews.com / User123!

## Troubleshooting
```bash
# Check status
docker-compose ps

# Restart service
docker-compose restart backend

# Clean restart
docker-compose down
docker-compose up --build

# Nuclear option (remove everything)
docker-compose down -v
docker system prune -a
docker-compose up --build
```

## Database
```bash
# Backup
docker-compose exec mysql mysqldump -u eznews_user -peznews_password eznews2 > backup.sql

# Restore
docker-compose exec -T mysql mysql -u eznews_user -peznews_password eznews2 < backup.sql
```

---
📚 Full guide: [DOCKER.md](DOCKER.md)
