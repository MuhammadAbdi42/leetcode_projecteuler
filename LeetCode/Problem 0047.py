from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [nums]

        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            selected = nums[i]
            prems = self.permuteUnique(nums[:i] + nums[i+1:])
            for j in range(len(prems)):
                output.append([selected] + prems[j])

        return output
