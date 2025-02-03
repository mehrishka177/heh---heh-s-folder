def find_lcm(a, b):
    # Find the greater number
    greater = max(a, b)
    
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

# Example usage
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"LCM of {a} and {b} is {find_lcm(a, b)}")