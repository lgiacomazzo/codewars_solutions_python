import math

cache_prime = {}


# checking for prime
def _is_prime(number):
    """
    Checks if a number is prime. After the factor 2, it checks for all odd factors
    :param number: number to check for primality
    :return: True or false
    """
    # assuming n is at least 2
    # checking for 2

    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # iterating loop till square root of n
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        # checking for factor
        if number % i == 0:
            return False
    return True


def is_prime(number):
    """
    Checks if a number is prime. Memoization technique is used (maybe useless now,
    I don't want to change)
    :param number: number to check for primality
    :return: True or false
    """
    if number not in cache_prime:
        cache_prime[number] = _is_prime(number)
    return cache_prime[number]


def proper_fractions_fast(denominator):
    """
    Based on https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula,
    it computes the denominator prime factors without any factorization,
    and then it computes the euler's product formula
    :param denominator: Denominator of reduced fractions
    :return: number of reduced fractions with that denominator
    """
    # computing the number of reduced fractions is equivalent to computing
    # the Euler's totient function
    phi = denominator
    d_is_prime = True
    for num in range(2, denominator):
        if denominator % num == 0 and is_prime(num):
            d_is_prime = False
            # print(num)
            phi *= (1 - 1 / num)
    if d_is_prime:
        phi = denominator - 1
    # print(int(phi))
    return int(phi)


def factorize(number):
    """
    Factorization is based on the 6k +-1 deterministic primality test
    (https://en.wikipedia.org/wiki/Primality_test#Python_code). Apart from 2 and 3,
    all prime factors can be expressed as 6k +- 1, for some k integer.
    :param number: number to factorize
    :return: list of prime factors
    """
    factors = []
    # quello per 2
    temp_number = number
    factor = 2
    if temp_number % factor == 0:
        factors.append(factor)
        while temp_number % factor == 0:
            temp_number //= factor

    # quello per 3
    factor = 3
    if temp_number % factor == 0:
        factors.append(factor)
        while temp_number % factor == 0:
            temp_number //= factor
    # quello per 6k +- 1
    factor = 5
    while factor <= temp_number:
        if temp_number % factor == 0:
            factors.append(factor)
            while temp_number % factor == 0:
                temp_number //= factor
        factor += 2
        if temp_number % factor == 0:
            factors.append(factor)
            while temp_number % factor == 0:
                temp_number //= factor
        factor += 4
    return factors


def proper_fractions_fast_fast(denominator):
    """
    Based on https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula,
    it factorizes the denominator prime factors, and then it computes the euler's product formula
    :param denominator: Denominator of reduced fractions
    :return: number of reduced fractions with that denominator
    """
    phi = denominator
    list_of_prime_factors = factorize(denominator)
    d_is_prime = len(list_of_prime_factors) == 0 or list_of_prime_factors[0] == denominator
    if d_is_prime:
        phi = denominator - 1
    else:
        for num in list_of_prime_factors:
            phi *= (1 - 1 / num)
    # print(int(phi))
    return int(phi)
