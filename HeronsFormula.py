#39.Area of the triangle using herons formula
import math

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2  # Calculate semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Example usage:
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))
triangle_area = area_of_triangle(side_a, side_b, side_c)
print("Area of the triangle:", triangle_area)