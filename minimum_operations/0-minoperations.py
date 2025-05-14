#!/usr/bin/python3
def minOperations(n):
    # If n is less than 2 or not an integer, it's impossible
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    # Find prime factors of n
    while n > 1:
        # If divisor divides n evenly
        if n % divisor == 0:
            n = n // divisor
            operations += divisor
        else:
            # Try next divisor
            divisor += 1

    return operations

# Test cases
print(f"Min # of operations to reach 4 char: {minOperations(4)}")
print(f"Min # of operations to reach 12 char: {minOperations(12)}")
