from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        output, zeros = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            r += 1

            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if zeros <= k:
                output = max(output, r-l)

        return output
