from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        con = True
        index = 0
        while con:
            for i in range(index, len(nums)):
                if i == len(nums) - 1:
                    con = False
                    break
                if nums[i] == nums[i+1]:
                    nums.pop(i+1)
                    index = i
                    break

        return len(nums)
