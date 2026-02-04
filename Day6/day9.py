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
