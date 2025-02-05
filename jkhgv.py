def sieve_of_eratosthenes(limit):
    # Create a list to mark the primality of numbers
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers

    for number in range(2, int(limit ** 0.5) + 1):
        if primes[number]:
            # Mark all multiples of number as non-prime
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False

    # Extracting the prime numbers
    return [num for num, is_prime in enumerate(primes) if is_prime]

# Example usage:
limit = 50
prime_numbers = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")
