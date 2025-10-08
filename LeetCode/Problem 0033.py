from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        rotation = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums = nums[i+1:] + nums[:i+1]
                rotation = len(nums) - (i + 1)
                break

        index = -1
        i, j = 0, len(nums) - 1
        while i <= j:
            pivot = (i + j) // 2
            if nums[pivot] == target:
                index = pivot
                break
            elif nums[pivot] > target:
                j = pivot - 1
            elif nums[pivot] < target:
                i = pivot + 1

        if index == -1:
            return -1
        else:
            position = index - rotation
            if position >= 0:
                return position
            else:
                return position + len(nums)
