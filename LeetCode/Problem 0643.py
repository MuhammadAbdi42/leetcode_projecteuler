from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = 0
        for i in range(k):
            temp += nums[i]
        temp /= k
        max_avg = temp

        for i in range(1, len(nums) - k + 1):
            temp = ((temp * k) - nums[i - 1] + nums[i + k - 1]) / k
            if temp > max_avg:
                max_avg = temp

        return max_avg
