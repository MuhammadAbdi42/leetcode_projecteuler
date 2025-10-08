from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for ind, num in enumerate(nums):
            if num not in hash_table.keys():
                hash_table[num] = ind
            else:
                if 2 * num == target:
                    return [hash_table[num], ind]

        for num in hash_table:
            if target - num in hash_table and target - num != num:
                return [hash_table[num], hash_table[target - num]]

        return []
