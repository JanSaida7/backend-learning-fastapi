#day9.py
import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

# 1. Load the passwords from .env file (works regardless of CWD)
DOTENV_PATH = Path(__file__).with_name(".env")
load_dotenv(DOTENV_PATH)

def get_db_connection():
    """Establishes a connection to the database."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        return conn
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return None
    
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        print("✅ Successfully connected to PostgreSQL!")
        connection.close() # Always close the line when done

# ... imports and get_db_connection ...

def get_all_users():
    conn = get_db_connection()
    if not conn:
        return 
    # The "Cursor" is like your mouse pointer in the DB
    cur = conn.cursor()

    cur.execute("SELECT id, username, email FROM users;")

    # Fetch results
    users = cur.fetchall()

    print("\n--- SYSTEM USERS ---")
    for user in users:
        # user is a tuple: (1, 'alice', 'alice@email.com')
        print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]}")


    cur.close()
    conn.close()

if __name__ == "__main__":
    # connection check removed to keep it clean
    get_all_users()