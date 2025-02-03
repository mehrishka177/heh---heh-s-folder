number = int(input("Enter your number:"))

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reverssed_number * 10 + digits
    number //= 10
    
if original_number == reversed_number:
    print("Palindrome")
else:
    print("Not a palindrome")