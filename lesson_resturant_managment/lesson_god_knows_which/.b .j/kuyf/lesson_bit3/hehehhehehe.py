import math

def powerset(s):
    """
    Generate the powerset of a given set using bitwise operators.
    
    Parameters:
    s (list): The input list for which to generate the powerset.
    
    Returns:
    list: A list of lists, where each list is a subset of the input list.
    """
    x = len(s)
    powerset_list = []
    
    # Iterate over the range from 0 to 2^x (exclusive)
    for i in range(1 << x):
        subset = []
        
        # Check each bit position
        for j in range(x):
            # If the j-th bit of i is set, include s[j] in the subset
            if i & (1 << j):
                subset.append(s[j])
        
        # Add the subset to the powerset list
        powerset_list.append(subset)
    
    return powerset_list

# Example usage
input_set = [1, 2, 3]
result = powerset(input_set)
print(f"The powerset of {input_set} is {result}")

# Additional example with a larger set
input_set_large = ['a', 'b', 'c', 'd']
result_large = powerset(input_set_large)
print(f"The powerset of {input_set_large} is {result_large}")

# Explanation of the bitwise approach
"""
The bitwise approach works by treating each subset as a binary number.
For a set of size n, there are 2^n possible subsets.
Each bit in the binary number represents whether an element is included in the subset (1) or not (0).
For example, for the set [1, 2, 3]:
- 000 (binary) -> [] (empty subset)
- 001 (binary) -> [1]
- 010 (binary) -> [2]
- 011 (binary) -> [1, 2]
- 100 (binary) -> [3]
- 101 (binary) -> [1, 3]
- 110 (binary) -> [2, 3]
- 111 (binary) -> [1, 2, 3]
"""

# Additional function to print the powerset in a more readable format
def print_powerset(powerset):
    for subset in powerset:
        print(subset)

# Print the powerset of the larger set in a readable format
print("Powerset of the larger set:")
print_powerset(result_large)