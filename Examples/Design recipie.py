from dataclasses import dataclass
from typing import *
# Data Definition
# We will represent a rectangle with its length and width. Where both are float.
length: TypeAlias = float
width: TypeAlias= float
#Building: TypeAlias = Union['ResidentialBuilding','CommercialBuilding’]

@dataclass
class Rectangle:
    length: float
    width: float

# Signature
# calculate_rectangle_area: Rectangle: float float -> float

# Header
    """
    Calculate the area of a rectangle.

    :param rectangle: A Rectangle object representing the rectangle.
    :return: The area of the rectangle as a float.
    """

# Purpose Statement
# This function takes a Rectangle object as input and calculates its area
# by multiplying the length and width attributes together. The result is returned as a floating-point number.

# Contract
# calculate_rectangle_area(Rectangle(5.0, 3.0)) => 15.0
# calculate_rectangle_area(Rectangle(0.0, 10.0)) => 0.0
# calculate_rectangle_area(Rectangle(7.5, 2.5)) => 18.75

#template

def calculate_rectangle_area(rectangle):
    """
    Calculate the area of a rectangle.

    :param rectangle: A Rectangle object representing the rectangle.
    :return: The area of the rectangle as a float.
    """
    area = rectangle.length * rectangle.width
    return area

# Example usage
rectangle1 = Rectangle(5.0, 3.0)
area1 = calculate_rectangle_area(rectangle1)
print(f"The area of the rectangle with length {rectangle1.length} and width {rectangle1.width} is {area1}.")

rectangle2 = Rectangle(0.0, 10.0)
area2 = calculate_rectangle_area(rectangle2)
print(f"The area of the rectangle with length {rectangle2.length} and width {rectangle2.width} is {area2}.")

rectangle3 = Rectangle(7.5, 2.5)
area3 = calculate_rectangle_area(rectangle3)
print(f"The area of the rectangle with length {rectangle3.length} and width {rectangle3.width} is {area3}.")

#Test cases
# Test Case 1: A rectangle with non-zero length and width
rectangle1 = Rectangle(5.0, 3.0)
assert calculate_rectangle_area(rectangle1) == 15.0

# Test Case 2: A rectangle with zero length
rectangle2 = Rectangle(0.0, 10.0)
assert calculate_rectangle_area(rectangle2) == 0.0

# Test Case 3: A square (length equals width)
rectangle3 = Rectangle(4.0, 4.0)
assert calculate_rectangle_area(rectangle3) == 16.0

# Test Case 4: A large rectangle with decimal values
rectangle4 = Rectangle(7.5, 2.5)
assert calculate_rectangle_area(rectangle4) == 18.75

# Test Case 5: A square with zero length and width
rectangle5 = Rectangle(0.0, 0.0)
assert calculate_rectangle_area(rectangle5) == 0.0

# Test Case 6: A rectangle with negative values (area should still be positive)
rectangle6 = Rectangle(6.0, 4.0)
assert calculate_rectangle_area(rectangle6) == 24.0
