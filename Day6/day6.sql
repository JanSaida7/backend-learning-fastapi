-- day6.sql

-- Goal: Create a "users" table to store account information.
-- This file contains raw SQL commands.

-- day6.sql

-- 1. Create the Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Insert dummy data (Optional, but good to save)
INSERT INTO users (username, email, is_active) 
VALUES ('alice', 'alice@example.com', true);

INSERT INTO users (username, email, is_active) 
VALUES ('bob', 'bob@example.com', false);

-- 3. Read Data (Select)

-- Get everything
SELECT * FROM users;

-- Get only specific columns
SELECT username, email FROM users;
add .

-- Filter data (Where clause)
SELECT * FROM users WHERE is_active = true;

-- 4. Update Data
-- Bob paid his subscription, let's activate him.
UPDATE users 
SET is_active = true 
WHERE username = 'bob';

-- 5. Delete Data
-- Charlie cancelled his account.
DELETE FROM users 
WHERE username = 'charlie';