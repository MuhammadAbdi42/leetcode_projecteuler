from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        for num in nums:
            if num in num_count.keys():
                num_count[num] += 1
            else:
                num_count[num] = 1

        output = 0
        for num in nums:
            if num_count[num] == 0:
                continue
            num_count[num] -= 1
            if k - num in num_count:
                if num_count[k - num] != 0:
                    output += 1
                    num_count[k - num] -= 1

        return output
