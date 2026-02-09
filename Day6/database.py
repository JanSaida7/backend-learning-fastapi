#database.py
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Factory function to create a database connection."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"❌ Database Connection Failed: {e}")
        return None