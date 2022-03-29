from typing import List


def removeElement(nums: List[int], val: int) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j

nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))
