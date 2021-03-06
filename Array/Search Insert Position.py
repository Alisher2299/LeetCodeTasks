"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if target == num or target < num:
            return i
    return i + 1


print(searchInsert([1, 3, 5, 6], 10))
