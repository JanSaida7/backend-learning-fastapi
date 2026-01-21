#Importing the math functions from math_utils module

from Day2.math_utils import calculate_circle_area, add_numbers

def run_app():  
    print("--- APP_STARTED ---", flush=True)

    try:
        #Testing Addition 
        sum_result = add_numbers(10, 20)
        print(f"Sum of 10 and 20 is: {sum_result}", flush=True)

        #Testing Circle Area Calculation
        radius = 5.0
        area = calculate_circle_area(radius)    
        print(f"Area of circle with radius {radius} is: {area}", flush=True)

    except ValueError as e:
        print(f"Error: {e}", flush=True)    

    print("--- APP_ENDED ---", flush=True)

if __name__ == "__main__":
    run_app()