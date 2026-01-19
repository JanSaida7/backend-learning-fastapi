import time
from typing import Callable, Any

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


#The Timer Decorator
def execution_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    # *args, **kwargs means "Accept ANY arguments"
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@execution_timer
def heavy_calculation(n: int) -> int:
    print(f"Calculating sum of range {n}...")
    time.sleep(1)
    return sum(range(n))

if __name__ == "__main__":
    print("--- APP STARTS ---")

    get_user_data()


    print("\n--- TIMER TEST ---")
    total = heavy_calculation(1000000)
    print(f"Result: {total}")