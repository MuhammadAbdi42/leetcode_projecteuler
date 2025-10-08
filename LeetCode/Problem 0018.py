from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        result = sorted([nums[i], nums[j], nums[l], nums[r]])
                        if result not in output:
                            output.append(result)
                        r -= 1
                    elif sum > target:
                        r -= 1
                    elif sum < target:
                        l += 1

        return output
