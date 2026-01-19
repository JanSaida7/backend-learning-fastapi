import time

def my_logger(func_to_decorate):
    def wrapper(*args, **kwargs):
        print("LOG: Starting process...")
        func_to_decorate(*args, **kwargs)
        print("LOG: Process finished.")
    return wrapper

#APPLY THE DECORATOR HERE
@my_logger
def get_user_data():
    print("Fetching data from database...")
    time.sleep(1.5)
    print("Data fetched!")

if __name__ == "__main__":
    print("--- APP STARTS ---")


    get_user_data()