from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) == 0:
            return 0
        elif len(merged) % 2 == 0:
            r = int(len(merged)/2)
            return (merged[r] + merged[r-1]) / 2
        else:
            r = int((len(merged) - 1) / 2)
            return merged[r]
