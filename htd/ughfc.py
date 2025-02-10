def count_bits(n):
    """Returns the number of bits set to 1 in the binary representation of n.
    
    Args:
        n (int): The integer to analyze.
    
    Returns:
        int: The count of bits set to 1.
    """
    binary_representation = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    count = binary_representation.count('1')
    
    print(f"Binary representation of {n} is {binary_representation}")
    print(f"Number of bits set to 1: {count}")
    
    return count

# Example usage
if __name__ == "__main__":
    num = 29  # Binary: 11101
    result = count_bits(num)
    print(f"Number of bits in {num}: {result}")