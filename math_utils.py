import math

def calculate_circle_area(radius: float) -> float:
    """
    Returns the area of a circle given the radius.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    return math.pi * (radius ** 2)

def add_numbers(a: int, b: int) -> int:
    return a + b

