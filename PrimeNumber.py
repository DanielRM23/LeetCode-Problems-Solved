def isPrime(n: int):
    if n < 2:
        return False  # This is because 0 and 1 are not primes
    elif n == 2:
        return True  # This is because 2 is the only prime which is even
    elif n % 2 == 0:
        return False  # Discard even numbers

    # We are looking for a number that can divide to n
    # to do that we use a Theorem:
    # If "n" is a composite integer, then "n" has at least a prime divisor less than or equal to sqrt(n)
    # Instead the Theorem, we use the contrapositive Theorem:
    # If "n" has no prime divisors less than or equal to sqrt(n), then "n" is a prime number.

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2

    return True
