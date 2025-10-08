from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for largest in range(len(nums) - 1, 1, -1):
            l, r = 0, largest - 1
            while l < r:
                if nums[l] + nums[r] > nums[largest]:
                    output += r - l
                    r -= 1
                else:
                    l += 1

        return output
