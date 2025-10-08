from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_table = {}
        unfiltered_output = []

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        for a in hash_table.keys():
            hash_table[a] -= 1
            for b in hash_table.keys():
                if hash_table[b] == 0:
                    continue
                c = - a - b
                hash_table[b] -= 1
                if c in hash_table.keys() and hash_table[c] != 0:
                    unfiltered_output.append(sorted([a, b, c]))
                hash_table[b] += 1

        output_set_list_dict = {}
        for list in unfiltered_output:
            output_set_list_dict[tuple(list)] = list

        output = []
        for set_key in output_set_list_dict.keys():
            output.append(output_set_list_dict[set_key])

        return output
