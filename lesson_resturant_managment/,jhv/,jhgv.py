def is_nth_bit_set(num, n):
    """
    Check if the nth bit of a number is set or not.
    
    :param num: The number to check.
    :param n: The bit position to check (0-based indexing).
    :return: True if the nth bit is set, False otherwise.
    """
    if n < 0:
        raise ValueError("Bit position cannot be negative.")
    
    # Shift 1 to the nth position and perform bitwise AND with num
    return (num & (1 << n)) != 0

# Example usage
number = 10  # Binary: 1010
position = 3

if is_nth_bit_set(number, position):
    print(f"The {position}th bit is set in {number}.")
else:
    print(f"The {position}th bit is not set in {number}.")
