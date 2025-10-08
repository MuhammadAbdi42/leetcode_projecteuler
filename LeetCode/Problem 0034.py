from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        # Finding left range
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] == target:
                if pivot == 0:
                    left = pivot
                    break
                else:
                    if nums[pivot - 1] != target:
                        left = pivot
                        break
                    else:
                        r = pivot - 1
            elif nums[pivot] > target:
                r = pivot - 1
            else:
                l = pivot + 1

        # Finding right range
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] == target:
                if pivot == len(nums) - 1:
                    right = pivot
                    break
                else:
                    if nums[pivot + 1] != target:
                        right = pivot
                        break
                    else:
                        l = pivot + 1
            elif nums[pivot] > target:
                r = pivot - 1
            else:
                l = pivot + 1

        return [left, right]
