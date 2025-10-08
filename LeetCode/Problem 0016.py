from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        main_dis = float('inf')
        output = float('inf')

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp_sum = nums[i] + nums[l] + nums[r]
                dis = abs(target - temp_sum)
                if dis < main_dis:
                    main_dis = dis
                    output = temp_sum

                if temp_sum > target:
                    r -= 1
                else:
                    l += 1

        return int(output)
