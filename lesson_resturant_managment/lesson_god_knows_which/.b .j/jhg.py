def find_two_odd_numbers(arr):
    """
    Function to find two numbers in an array that appear an odd number of times.
    
    Args:
        arr (list): List of integers.
        
    Returns:
        tuple: Two odd-occurring numbers.
    """
    # Step 1: XOR all elements in the array
    xor_all = 0
    for num in arr:
        xor_all ^= num

    # Step 2: Find the rightmost set bit in xor_all
    rightmost_set_bit = xor_all & -xor_all

    # Step 3: Divide numbers into two groups and XOR within each group
    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2

# Example usage
arr = [4, 3, 4, 5, 3, 5, 7, 11]
odd_numbers = find_two_odd_numbers(arr)
print("The two odd-occurring numbers are:", odd_numbers)