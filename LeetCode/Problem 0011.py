from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = -float('inf')

        l, r = 0, len(height) - 1
        while l < r:
            if height[l] > height[r]:
                volume = height[r] * (r - l)
                if volume > max_volume:
                    max_volume = volume
                r -= 1
            else:
                volume = height[l] * (r - l)
                if volume > max_volume:
                    max_volume = volume
                l += 1

        return int(max_volume)
