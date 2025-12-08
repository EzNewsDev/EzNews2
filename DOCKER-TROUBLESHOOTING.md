# Docker Troubleshooting - Frontend Connection Issue

## Current Status

### ✅ Working Containers
- **MySQL**: Healthy, accessible on port 3307
- **Backend**: Running, all APIs working
  - Test: `curl http://localhost:5000/api/articles` ✅
  - Database seeded with 15 Indonesian news articles ✅
  - Gunicorn workers operational ✅

### ❌ Frontend Issue
- **Vite Server**: Running INSIDE container (logs show "VITE v5.4.21 ready")
- **Browser Access**: `ERR_CONNECTION_REFUSED` on http://localhost:5173
- **Port Mapping**: 5173:5173 configured
- **Binding**: Vite set to `0.0.0.0` ✅

## Fixes Attempted

1. ✅ Fixed PostCSS config (CommonJS → ESM syntax)
2. ✅ Fixed circular dependencies in Admin page imports
3. ✅ Rebuilt frontend container from scratch (no cache)
4. ✅ Updated Vite config to bind `host: '0.0.0.0'`
5. ✅ Verified Vite running inside container
6. ❌ Browser still cannot connect

## Diagnostic Results

### Inside Container
```bash
docker logs eznews2_frontend
# Shows: VITE v5.4.21  ready in 413 ms
# ➜  Local:   http://localhost:5173/
# ➜  Network: http://172.18.0.4:5173/
```

### From Host (Windows)
```bash  
curl http://localhost:5173
# Result: Connection Refused
```

### Browser Console
```
net::ERR_CONNECTION_REFUSED
net::ERR_EMPTY_RESPONSE
```

## Possible Causes

1. **Windows Docker Desktop Networking**
   - Hyper-V networking issue
   - Port not properly forwarded to WSL/VM

2. **Windows Firewall**
   - Blocking port 5173 for containers
   - Need to allow Docker port access

3. **Docker Compose Port Mapping**
   - May need different port mapping syntax for Windows
   - Try `127.0.0.1:5173:5173` instead of `5173:5173`

4. **Vite HMR WebSocket**
   - WebSocket connection for hot reload failing
   - May need additional config for Docker

## Recommended Next Steps

### Option A: Run Frontend Manually (Isolate Issue)
```bash
cd frontend  
npm install
npm run dev
```
This will determine if issue is Docker-specific or code-related.

### Option B: Check Docker Desktop Settings
- Open Docker Desktop → Settings → Resources
- Verify port 5173 is not blocked
- Check Windows Firewall  

### Option C: Alternative Port Mapping
Update `docker-compose.yml`:
```yaml
frontend:
  ports:
    - "127.0.0.1:5173:5173"  # Explicitly bind to localhost
```

### Option D: Use Production Build Instead
Build static files and serve with nginx (skip Vite dev server):
```dockerfile
# Multi-stage build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

### Option E: Use Backend API Directly
Backend is 100% working. Can test with:
- Postman
- curl
- Python requests
- Any HTTP client

## Workaround for Now

While troubleshooting frontend Docker:

**Test Backend API:**
```bash
# Get articles
curl http://localhost:5000/api/articles

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@eznews.com", "password": "Admin123!"}'
```

**Access Database:**
```bash
mysql -h 127.0.0.1 -P 3307 -u eznews_user -peznews_password eznews2
```

## Summary

- Backend containerization: ✅ 100% Working
- Frontend containerization: ⚠️ Container runs, but not accessible from host
- Likely cause: Windows Docker networking / port forwarding issue
- Backend can be used standalone while debugging frontend
