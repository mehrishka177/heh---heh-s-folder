def flip_bits(n):
    """
    Flip the bits of an integer.
    
    Parameters:
    n (int): The input integer whose bits are to be flipped.
    
    Returns:
    int: The integer with its bits flipped.
    """
    # Calculate the number of bits in the integer
    num_bits = n.bit_length()
    
    # Create a bitmask with all bits set to 1 for the length of the integer
    bitmask = (1 << num_bits) - 1
    
    # Flip the bits using XOR with the bitmask
    flipped = n ^ bitmask
    
    return flipped

# Example usage
input_number = 29  # Binary: 11101
flipped_number = flip_bits(input_number)
print(f"The flipped bits of {input_number} (binary: {bin(input_number)}) is {flipped_number} (binary: {bin(flipped_number)})")

# Additional example with a larger number
input_number_large = 1023  # Binary: 1111111111
flipped_number_large = flip_bits(input_number_large)
print(f"The flipped bits of {input_number_large} (binary: {bin(input_number_large)}) is {flipped_number_large} (binary: {bin(flipped_number_large)})")

# Explanation of the bit flipping process
"""
The bit flipping process works by using a bitmask.
For an integer n, we first calculate the number of bits required to represent n.
We then create a bitmask with all bits set to 1 for the length of the integer.
By performing an XOR operation between the integer and the bitmask, we flip all the bits of the integer.
For example, for the integer 29 (binary: 11101):
- The number of bits is 5.
- The bitmask is 11111 (binary) or 31 (decimal).
- The XOR operation between 11101 and 11111 results in 00010 (binary) or 2 (decimal).
"""

# Additional function to print the binary representation of a number
def print_binary_representation(n):
    print(f"Decimal: {n}, Binary: {bin(n)}")

# Print the binary representation of the original and flipped numbers
print("Binary representation of the original and flipped numbers:")
print_binary_representation(input_number)
print_binary_representation(flipped_number)
print_binary_representation(input_number_large)
print_binary_representation(flipped_number_large)

# Additional example with a negative number
input_number_negative = -29  # Binary: -11101
flipped_number_negative = flip_bits(input_number_negative)
print(f"The flipped bits of {input_number_negative} (binary: {bin(input_number_negative)}) is {flipped_number_negative} (binary: {bin(flipped_number_negative)})")

# Print the binary representation of the original and flipped negative number
print("Binary representation of the original and flipped negative number:")
print_binary_representation(input_number_negative)
print_binary_representation(flipped_number_negative)

# Explanation of handling negative numbers
"""
Flipping bits of negative numbers can be tricky due to the way negative numbers are represented in binary (two's complement).
In two's complement, the most significant bit (MSB) is used as the sign bit.
When flipping bits of a negative number, the result may not be straightforward and can lead to unexpected results.
For example, for the integer -29 (binary: -11101):
- The number of bits is 5.
- The bitmask is 11111 (binary) or 31 (decimal).
- The XOR operation between -11101 and 11111 results in -10000 (binary) or -16 (decimal).
"""

# Additional function to handle flipping bits of negative numbers
def flip_bits_negative(n):
    """
    Flip the bits of a negative integer.
    
    Parameters:
    n (int): The input negative integer whose bits are to be flipped.
    
    Returns:
    int: The integer with its bits flipped.
    """
    if n >= 0:
        return flip_bits(n)
    
    # Calculate the number of bits in the positive equivalent of the integer
    num_bits = (-n).bit_length()
    
    # Create a bitmask with all bits set to 1 for the length of the integer
    bitmask = (1 << num_bits) - 1
    
    # Flip the bits using XOR with the bitmask and negate the result
    flipped = (~n) & bitmask
    
    return flipped

# Example usage with the additional function for negative numbers
flipped_number_negative_corrected = flip_bits_negative(input_number_negative)
print(f"The correctly flipped bits of {input_number_negative} (binary: {bin(input_number_negative)}) is {flipped_number_negative_corrected} (binary: {bin(flipped_number_negative_corrected)})")

# Print the binary representation of the correctly flipped negative number
print("Binary representation of the correctly flipped negative number:")
print_binary_representation(flipped_number_negative_corrected)