from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxx = -float('inf')

        start = len(energy) - 1
        while start >= len(energy) - k:
            i = start
            temp, max_batch = 0, -float('inf')
            while i >= 0:
                temp += energy[i]
                if temp > max_batch:
                    max_batch = temp
                i -= k

            if max_batch > maxx:
                maxx = max_batch

            start -= 1

        return int(maxx)
