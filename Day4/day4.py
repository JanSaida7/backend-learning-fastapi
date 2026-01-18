import time

# 1. The Wrapper Factory
def my_logger(func):  # Changed from func_to_decorate
    def wrapper():
        print("LOG: Starting process...")
        func()  # Updated reference
        print("LOG: Process finished.")
    return wrapper

def get_user_data():
    print("Fetching data from database...")
    time.sleep(1.5)
    print("Data Fetched!")

if __name__ == "__main__":
    print("--- APP STARTED ---")
    
    # 2. The Manual Decoration
    # We wrap the function manually
    secure_function = my_logger(get_user_data)

    # 3. Run the NEW function
    secure_function()