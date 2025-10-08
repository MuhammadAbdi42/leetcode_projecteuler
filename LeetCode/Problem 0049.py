from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for i in range(len(strs)):
            str_key = ''.join(sorted(strs[i]))
            if str_key in hash_table.keys():
                hash_table[str_key].append(strs[i])
            else:
                hash_table[str_key] = [strs[i]]

        return list(hash_table.values())
