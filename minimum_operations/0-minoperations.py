#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to achieve n H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Find prime factors of n
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        operations += n

    return operations
