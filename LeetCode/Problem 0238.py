from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        all_mult = 1
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                all_mult *= num

        for i in range(len(nums)):
            if nums[i] == 0:
                if zeros > 1:
                    nums[i] = 0
                else:
                    nums[i] = all_mult
            else:
                if zeros > 0:
                    nums[i] = 0
                else:
                    nums[i] = int(all_mult / nums[i])

        return nums
