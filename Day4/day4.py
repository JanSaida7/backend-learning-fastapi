import time

def get_user_data():
    print("Fetching data from database...")
    time.sleep(1.5)
    print("Data Fetched!")

if __name__ == "__main__":
    print("--- APP STARTED ---")
    get_user_data()