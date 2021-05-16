import math


def proper_fractions_ultimate_fast(denominator):
    """
    Computing the number of reduced fractions is equivalent to computing
    the Euler's totient function. Infact, computing the number of numerators on
    which the formula "GCD(num, denominator) == 1" is true, it's equivalent to computing
    how many coprime numbers of the denominator are present. Check this link
    (https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula)
    :param denominator: Denominator of reduced fractions
    :return: number of reduced fractions with that denominator
    """
    # Simple base case, because 1 is not a prime number
    if denominator <= 1:
        return 0
    # given the formula, phi starts from the number itself
    phi = denominator
    # it's used for optimizing the while loop
    upper_limit = int(math.ceil(math.sqrt(denominator)))
    # the first prime number to start from is the number 2 (1 is not a prime number)
    # the idea is to iterate over prime numbers starting from the bottom
    factor = 2
    # instead of using "while factor*factor <= denominator", since the upper_limit is computed
    # only one time, instead of continuously computing factor*factor for each loop
    while factor <= upper_limit:
        # found a prime factor
        if denominator % factor == 0:
            # wipe it from existence (divide until that factor is gone from the denominator)
            # and don't encounter it never again
            while denominator % factor == 0:
                denominator = denominator // factor
            # since the denominator has changed, I recompute the upper limit again
            upper_limit = int(math.ceil(math.sqrt(denominator)))
            # the actual update to the phi formula
            phi *= (1 - 1 / factor)
        # don't wanna get into an infinite loop, no? Just increase by 1
        factor += 1
    # at this point, it may happen that no other factors are found. Given that the while stops
    # at most to the square root of the denominator (updated or not), this means that the
    # remaining denominator must be a prime number, and therefore it must be a prime factor
    # of the denominator itself
    if denominator > 1:
        phi *= (1 - 1 / denominator)
    # print(int(phi))
    return int(phi)
