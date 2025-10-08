from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        occurances = {}

        for num in nums:
            if num in occurances:
                occurances[num] += 1
            else:
                occurances[num] = 1

        sorted_occurances = sorted(list(occurances.values()))
        weight = 1

        if sorted_occurances:
            max = sorted_occurances[-1]
        else:
            return 0

        for i in sorted_occurances[-2::-1]:
            if i == max:
                weight += 1
            else:
                break

        return weight * max
