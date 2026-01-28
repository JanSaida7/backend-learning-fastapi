-- day7.sql

-- 1. Create Posts Table
-- "user_id" is the Foreign Key. It links to the "id" column in the "users" table.
-- ON DELETE CASCADE means: If User 1 is deleted, delete all their posts too.

CREATE TABLE posts {
  id SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  content TEXT,  
  user_id INTEGER REFERENCES user(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
};