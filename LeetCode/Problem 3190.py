from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = map(lambda x: x % 3 != 0, nums)
        return sum(operations)
