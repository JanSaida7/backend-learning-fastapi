# main.py
from user_repository import create_user, get_all_users
import sys

def main():
    while True:
        print("\n=== 👥 USER MANAGEMENT SYSTEM ===")
        print("1. List All Users")
        print("2. Create New User")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            users = get_all_users()
            print("\n--- Current Users ---")
            for u in users:
                # u is (id, username, email)
                print(f"ID: {u[0]} | Name: {u[1]} <{u[2]}>")

        elif choice == "2":
            name = input("Enter Username: ")
            email = input("Enter Email: ")
            create_user(name, email)

        elif choice == "3":
            print("Goodbye!")
            sys.exit()

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()