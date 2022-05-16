"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

n = 5


def count_bit(n: int):
    return [bin(i).count('1') for i in range(n + 1)]


print("my>\t", count_bit(n))


def countBit(n: int):
    count = [0]
    for i in range(1, n + 1):
        count.append(count[i >> 1] + i % 2)
    return count


print('best>', countBit(n))
