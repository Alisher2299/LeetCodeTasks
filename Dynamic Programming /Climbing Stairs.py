"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    step1 = 1
    step2 = 2

    for i in range(3, n + 1):
        sum = step1 + step2
        step1 = step2
        step2 = sum
    return step2


print(climbStairs(5))
