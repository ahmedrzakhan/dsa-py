# https://leetcode.com/problems/happy-number/

# TC - O(LogN), SC - O(LogN)
def isHappy(n: int) -> bool:
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return True


test_cases = [
    # (19, True),
    (2, False),
    # (7, True),
    # (23, True),
    # (4, False)
]

for num, expected in test_cases:
    result = isHappy(num)
    print(f"Input: {num}, Output: {result}, Expected: {expected}, {'Pass' if result == expected else 'Fail'}")