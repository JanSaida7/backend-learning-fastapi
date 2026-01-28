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

-- 2. Insert Posts linked to Users
-- Assuming User ID 1 is 'alice' and User ID 2 is 'bob'

INSERT INTO posts (title, content, user_id)
VALUES ('Hello World', 'This is my First post!', 1);

INSERT INTO posts (title, content, user_id) 
VALUES ('FastAPI is cool', 'I am learning backend dev.', 1);

INSERT INTO posts (title, content, user_id) 
VALUES ('SQL is hard', 'But I am getting better at it.', 2);

-- 3. INNER JOIN
-- Combines rows where there is a match in BOTH tables.

SELECT 
    users.username,
    posts.title,
    posts.created_at
FROM users
INNER JOIN posts ON user_id = posts.user_id

-- 4. LEFT JOIN
-- Shows ALL users, even if they haven't posted anything.

SELECT 
	users.username,
	posts.title
FROM users
	LEFT JOIN posts ON users.id = posts.user_id