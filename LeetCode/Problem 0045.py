from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        destination, jumps = len(nums) - 1, 0
        while destination > 0:
            for i in range(destination):
                distance = destination - i
                if nums[i] >= distance:
                    jumps += 1
                    destination = i
                    break

        return jumps
