import random


def random_number(n: int) -> int:
    """
    Returns a n-bit random number

    Parameters:
        argument1 (int): number of bits
    Returns:
        int: random number between 2^(n - 1) + 1, and 2^n - 1
    """
    return random.randrange(2**(n-1) + 1, 2**n - 1)


def primality_test(number: int) -> bool:
    """
    Returns a True if the number is "probably" a prime.
    Uses Miller-Rabin probabilistic primality test algorithm. For more: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    Parameters:
        argument1 (int): number to check
    Returns:
        bool: True if the number is prime, False if compound
    """

    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False

    def check_prime(a, s, d, n):
        x = pow(a, d, n)  # (a^d) mod n
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    k = 20  # Number of rounds to perform the primality test, the greater the k the greater the probability

    s = 0
    d = number - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, number - 1)
        if not check_prime(a, s, d, number):
            return False
    return True


def generate_prime(nbits=1024) -> int:
    """
    Returns a prime number.

    Parameters:
        argument1 (int): number of bits
    Returns:
        int: Returns a prime number
    """

    number = random_number(nbits)
    while True:
        if primality_test(number):
            return number
        number = random_number(nbits)


def gcd(a: int, b: int) -> int:
    """
    Computes the greatest common divisor of two numbers using euclidean algorithm
    """
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def compute_totient(p: int, q: int) -> int:
    """
    Calculates the Carmichael's Totient Function.
    λ(n) = lcm(p − 1, q − 1).
    For more: https://en.wikipedia.org/wiki/Carmichael_function

    Parameters:
        argument1 (int): first prime p
        argument2 (int): second prime q
    Returns:
        int: Returns the Totient number.
    """
    absolute_product = abs((p - 1) * (q - 1))
    lcm = absolute_product // gcd(p - 1, q - 1)
    return lcm


def choose_e(totient: int) -> int:
    """
    Choose a number e such that 1 < e < totient AND gcd(e, totient) == 1

    Parameters:
        argument1 (int): totient of n
    Returns:
        int: Returns the calculated value of e that satisfies the above conditions.
    """
    for i in range(totient - 1, 1, -1):  # start from the end in order to get the largest value of e
        if gcd(i, totient) == 1:
            return i
    return 0


def extended_gcd(a, b):
    """
    Implements the extended gcd algoirthm. For more: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    """
    output "Bézout coefficients:", (old_s, old_t)
    output "greatest common divisor:", old_r
    output "quotients by the gcd:", (t, s)
    """

    return old_r, old_s, old_t  # gcd, bezout coefficients


def modular_inverse(a, b):
    """
    Calculate modular inverse. Because e and totient are co prime, modular inverse is one of the coefficients of bezout identity
    """
    gcd, x, y = extended_gcd(a, b)

    if x < 0:
        x += b

    return x


def determine_d(e: int, totient: int):
    """
    Determine the value of d such that: de = 1 mod (totient)

    Parameters:
        argument1 (int): e
        argument2 (int): Totient
    Returns:
        int: Returns an interger that satisfies the above condition
    """
    return modular_inverse(e, totient)
