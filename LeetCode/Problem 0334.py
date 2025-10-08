from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num, max_num = nums[0], nums[-1]
        mins, maxs = [], []

        for i in range(1, len(nums) - 1):
            mins.append(min_num)
            if nums[i] < min_num:
                min_num = nums[i]

        for i in range(len(nums) - 2, 0, -1):
            maxs.append(max_num)
            if nums[i] > max_num:
                max_num = nums[i]

        for i in range(1, len(nums) - 1):
            if mins[i - 1] < nums[i] < maxs[-(i-1) - 1]:
                return True

        return False
