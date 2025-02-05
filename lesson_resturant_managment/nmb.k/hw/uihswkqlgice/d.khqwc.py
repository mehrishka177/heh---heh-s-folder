def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes

# Example usage
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Prime numbers:", find_primes(start, end))