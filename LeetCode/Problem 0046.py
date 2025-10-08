from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [nums]

        output = []
        for i in range(len(nums)):
            selected = nums[i]
            prems = self.permute(nums[:i] + nums[i+1:])
            for j in range(len(prems)):
                output.append([selected] + prems[j])

        return output
