"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is
returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""


def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    for i in range(x + 1):
        if i * i == x:
            return i
        elif i * i >= x:
            return i - 1


x = 8

print(mySqrt(x))
