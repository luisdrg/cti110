 # Luis Rivera Gonzalez
 # 2/18/2025
# P2LAB1 
# Using f-strings to display circle calculations
import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))

# Calculate diameter, circumference, area
diameter = (2*radius)
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Print diameter, circumference, area
print(f"\nThe diameter of the circle is {diameter:.1f}\n")
print(f"The circumference of the circle is {circumference:.2f}\n")
print(f"The area of the circle is {area:.3f}")