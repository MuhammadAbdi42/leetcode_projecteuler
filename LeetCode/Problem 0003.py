class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        for ind, char in enumerate(s):
            substring = ''
            for i in range(ind, len(s)):
                if s[i] not in substring:
                    substring += s[i]
                else:
                    break
            if len(substring) > output:
                output = len(substring)

        return output
