import math
from fractions import Fraction


def proper_fractions_slow_slow_slow(denominator):
    """
    Based on the fractions module, it creates an instance of Fraction, and then
    checks the denominator, since it is automatically reduced
    :param denominator: Denominator of reduced fractions
    :return: number of reduced fractions with that denominator
    """
    # stupid thing
    reduced_fractions = 0
    for numerator in range(1, denominator):
        if Fraction(numerator=numerator, denominator=denominator).denominator == denominator:
            reduced_fractions = reduced_fractions + 1
    return reduced_fractions


def proper_fractions_slow(denominator):
    """
    Based on the definition of reduced fractions, it counts all numbers going
    from 1 to denominator which gcd (Greatest Common Divisor) is equal to 1
    :param denominator: Denominator of reduced fractions
    :return: number of reduced fractions with that denominator
    """
    reduced_fractions = 0
    for numerator in range(1, denominator):
        if math.gcd(numerator, denominator) == 1:
            reduced_fractions = reduced_fractions + 1
    return reduced_fractions


def proper_fractions_slow_slow(denominator):
    """
    Based on https://en.wikipedia.org/wiki/Euler%27s_totient_function#Fourier_transform, it
    computes the phi function using cosines and gcd
    :param denominator: Denominator of reduced fractions
    :return: number of reduced fractions with that denominator
    """
    # Eulero phi function
    phi = 0
    if denominator > 1:
        for numerator in range(1, denominator + 1):
            phi += math.gcd(numerator, denominator) * math.cos(2*math.pi*numerator/denominator)
    return round(phi)
