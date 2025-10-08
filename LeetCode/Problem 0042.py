from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        total = 0
        max_left, max_right = height[0], height[-1]
        l, r = 1, len(height) - 2

        while l <= r:
            if max_left < max_right:
                if height[l] < max_left:
                    total += max_left - height[l]
                else:
                    max_left = height[l]
                l += 1
            else:
                if height[r] < max_right:
                    total += max_right - height[r]
                else:
                    max_right = height[r]
                r -= 1

        return (total)
