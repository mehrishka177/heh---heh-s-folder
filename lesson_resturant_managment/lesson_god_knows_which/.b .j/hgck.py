def find_factors(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

# Example usage
num = int(input("Enter a number: "))
print(f"Factors of {num}: {find_factors(num)}")

