import time
from typing import Callable

def my_logger(func_to_decorate: Callable[[], None]) -> Callable[[], None]:
    def wrapper():
        print("LOG: Starting process...")
        func_to_decorate()
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