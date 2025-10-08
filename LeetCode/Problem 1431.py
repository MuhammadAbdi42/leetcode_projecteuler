from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        output = list(map(lambda x: x + extraCandies >= max_candy, candies))
        return output
