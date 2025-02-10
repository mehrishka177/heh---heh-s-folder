def is_even(n):
    """
    Function to check if a number is even using bitwise operation.
    A number is even if its least significant bit (LSB) is 0.
    """
    return (n & 1) == 0  # If the least significant bit is 0, it's even

def is_odd(n):
    """
    Function to check if a number is odd using bitwise operation.
    A number is odd if its least significant bit (LSB) is 1.
    """
    return (n & 1) == 1  # If the least significant bit is 1, it's odd

def check_number(num):
    """
    Function to determine if a number is odd or even and print the result.
    """
    if is_even(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

def main():
    """
    Main function to get user input and check the number.
    """
    try:
        num = int(input("Enter a number: "))
        check_number(num)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
