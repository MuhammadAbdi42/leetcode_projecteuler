from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        i, j = 0, len(nums) - 2

        if len(nums) == 1 and nums[0] < target:
            return 1

        while i <= j:
            pivot = (i + j) // 2
            pair = (nums[pivot], nums[pivot + 1])
            if pair[0] < target <= pair[1]:
                index = pivot + 1
                break
            elif pair[0] == target:
                index = pivot
                break
            else:
                if pivot == 0 and target < pair[0]:
                    index = 0
                    break
                elif pivot == len(nums) - 2 and target > pair[1]:
                    index = len(nums)
                    break
                else:
                    if pair[0] > target:
                        j = pivot - 1
                    else:
                        i = pivot + 1

        return index
