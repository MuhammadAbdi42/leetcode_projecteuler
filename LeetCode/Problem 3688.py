from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x % 2 == 0, nums))

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            output = nums[0]
            for i in range(1, len(nums)):
                output |= nums[i]
            return output
