-- Initialize database
-- This file runs automatically when MySQL container starts for the first time

-- Ensure database exists
CREATE DATABASE IF NOT EXISTS eznews2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Grant privileges
GRANT ALL PRIVILEGES ON eznews2.* TO 'eznews_user'@'%';
FLUSH PRIVILEGES;

USE eznews2;

-- Tables will be created by SQLAlchemy when seed.py runs
