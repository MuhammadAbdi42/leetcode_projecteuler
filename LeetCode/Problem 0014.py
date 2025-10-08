from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        for ind, char in enumerate(strs[0]):
            for word in strs[1:]:
                if ind >= len(word) or word[ind] != char:
                    return prefix
            prefix += char

        return prefix
