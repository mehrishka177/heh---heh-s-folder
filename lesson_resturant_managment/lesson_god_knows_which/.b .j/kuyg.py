# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the numbers are equal without using the comparison operator
if (num1 ^ num2) != 0:
    print("The two numbers are equal!")
else:
    print("The two numbers are not equal.")
