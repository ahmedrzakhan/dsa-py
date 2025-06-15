# https://leetcode.com/problems/powx-n/

# TC - O(log N), SC - O(1)
def myPow(x: float, n: int) -> float:
    # Handle edge case for n = 0
    if n == 0:
        return 1.0

    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n

    # Initialize result
    result = 1.0
    current_product = x

    # Binary exponentiation
    while n > 0:
        # If n is odd, multiply result by current_product
        if n % 2 == 1:
            result *= current_product
        # Square the current_product
        current_product *= current_product
        # Integer divide n by 2
        n //= 2

    return result

def myPow2(x: float, n: int) -> float:
    return x ** n

# Test cases
print(f"Test 1: {myPow(2.00000, 10)}")  # Expected: 1024.00000
print(f"Test 2: {myPow(2.10000, 3)}")   # Expected: 9.26100
print(f"Test 3: {myPow(2.00000, -2)}")  # Expected: 0.25000

# Test cases
print(f"Test 1: {myPow2(2.00000, 10)}")  # Expected: 1024.00000
print(f"Test 2: {myPow2(2.10000, 3)}")   # Expected: 9.26100
print(f"Test 3: {myPow(2.00000, -2)}")  # Expected: 0.25000