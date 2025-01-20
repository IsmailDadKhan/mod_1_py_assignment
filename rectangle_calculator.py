# Program to calculate area and perimeter of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
