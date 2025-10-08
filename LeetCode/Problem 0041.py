from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i + 1 == nums[i]:
                i += 1
                continue

            if 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(1, len(nums)+1):
            if i != nums[i-1]:
                return i

        return nums[-1] + 1
