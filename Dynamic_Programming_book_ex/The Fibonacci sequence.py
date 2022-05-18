"""
Return the n-th number in the Fibonacci sequence. The first two numbers in the Fibonacci
sequence are equal to 1; any other number is equal to the sum of the preceding two numbers.
Example: for n = 6, the first 6 numbers of the sequence are [1, 1, 2, 3, 5, 8] so the result
is 8.
"""
N = 10


# Solution 1: brute force, 𝑂(2^n) time
def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


print('1>', fib1(N))

# Solution 2: dynamic programming, top-down O(n)
fib_cache2 = {}


def fib2(n):
    if n <= 2:
        return 1
    if n not in fib_cache2:
        fib_cache2[n] = fib2(n - 1) + fib2(n - 2)
    return fib_cache2[n]


print('2>', fib2(N))


# Solution 2: dynamic programming, bottom-up O(n)
def fib3(n):
    series = [1, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[-1]


print('3>', fib3(N))


# Solution 3:
def fib4(n):
    current = 1
    next_el = 1
    for i in range(n - 2):
        current, next_el = next_el, current + next_el
    return next_el


print('4>', fib4(N))
