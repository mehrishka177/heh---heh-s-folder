def bitwise_operations(a, b):
    print(f"a = {a}, b = {b}")
    print(f"a & b (AND) = {a & b}")
    print(f"a | b (OR) = {a | b}")
    print(f"a ^ b (XOR) = {a ^ b}")
    print(f"~a (NOT a) = {~a}")
    print(f"~b (NOT b) = {~b}")
    print(f"a << 1 (Left Shift) = {a << 1}")
    print(f"b >> 1 (Right Shift) = {b >> 1}")

# Example usage
a = 5  # 0b0101
b = 3  # 0b0011
bitwise_operations(a, b)