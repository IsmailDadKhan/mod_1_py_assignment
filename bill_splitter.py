# Program to split the bill
total_bill = int(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))

share = total_bill / num_people
print(f"Total Bill: {total_bill:.2f}")
print(f"Number of People: {num_people}")
print(f"Each Person Pays: {share:.2f}")
