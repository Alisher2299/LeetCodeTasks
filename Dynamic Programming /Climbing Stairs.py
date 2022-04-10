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
