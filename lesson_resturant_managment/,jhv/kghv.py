# Binary Operations in Python
def decimal_to_binary(decimal):
    """
    Converts a decimal number to binary.
    :param decimal: int
    :return: str (binary representation)
    """
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    """
    Converts a binary number to decimal.
    :param binary: str
    :return: int (decimal representation)
    """
    return int(binary, 2)

def add_binary(bin1, bin2):
    """
    Adds two binary numbers.
    :param bin1: str (binary number)
    :param bin2: str (binary number)
    :return: str (binary result)
    """
    decimal_sum = int(bin1, 2) + int(bin2, 2)
    return bin(decimal_sum)[2:]

def binary_operations():
    """
    Demonstrates basic binary operations.
    """
    print("\nBinary Operations")
    
    # Convert decimal to binary
    decimal_number = int(input("Enter a decimal number: "))
    binary_result = decimal_to_binary(decimal_number)
    print(f"Decimal {decimal_number} in binary is {binary_result}")

    # Convert binary to decimal
    binary_number = input("Enter a binary number: ")
    decimal_result = binary_to_decimal(binary_number)
    print(f"Binary {binary_number} in decimal is {decimal_result}")

    # Add two binary numbers
    binary1 = input("Enter the first binary number: ")
    binary2 = input("Enter the second binary number: ")
    binary_sum = add_binary(binary1, binary2)
    print(f"The sum of {binary1} and {binary2} is {binary_sum}")

if __name__ == "__main__":
    binary_operations()