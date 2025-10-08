from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for ind in range(m, m + n, 1):
            nums1[ind] = nums2[ind - (m)]

        nums1.sort()
