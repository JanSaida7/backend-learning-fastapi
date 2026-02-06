# user_repository.py
from database import get_db_connection
from typing import List, Tuple, Any

def create_user(username: str, email: str):
    conn = get_db_connection()
    if not conn:
        return

    cur = conn.cursor()
    try:
        query = "INSERT INTO users (username, email) VALUES (%s, %s);"
        cur.execute(query, (username, email))
        conn.commit()
        print(f"✅ User '{username}' saved to database.")
    except Exception as e:
        print(f"❌ Error saving user: {e}")
    finally:
        cur.close()
        conn.close()

def get_all_users() -> List[Tuple[Any, ...]]:
    conn = get_db_connection()
    if not conn:
        return [] # Return empty list if connection fails

    cur = conn.cursor()
    try:
        cur.execute("SELECT id, username, email FROM users;")
        users = cur.fetchall()
        return users # RETURN the data, don't print it here!
    except Exception as e:
        print(f"❌ Error fetching users: {e}")
        return []
    finally:
        cur.close()
        conn.close()