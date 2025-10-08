from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while True:
            if index >= len(nums):
                break
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1

        return len(nums)
