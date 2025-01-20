# Program to check the relationship between two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    relationship = "Greater than"
elif num1 < num2:
    relationship = "Less than"
else:
    relationship = "Equal"

if num1 % 2 == 0 and num2 % 2 == 0:
    parity = "Even"
elif num1 % 2 != 0 and num2 % 2 != 0:
    parity = "Odd"
else:
    parity = "Mixed"

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Relationship: {relationship}")
print(f"Both numbers are {parity}.")
