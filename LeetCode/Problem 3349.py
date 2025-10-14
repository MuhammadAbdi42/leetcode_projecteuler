from typing import List
from collections import Counter


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i = 0
        while i + 2 * k - 1 < len(nums):
            first, counter_first = nums[i:i+k], Counter(nums[i:i+k])
            second, counter_second = nums[i+k:i+2*k], Counter(nums[i+k:i+2*k])
            if (first == sorted(first) and
                len(counter_first.keys()) == k and
                second == sorted(second) and
                    len(counter_second.keys()) == k):
                return True
            i += 1
        return False
