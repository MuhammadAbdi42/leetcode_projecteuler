class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''
        for ind in range(len(s)):
            substring = ''
            for i in range(ind, len(s)):
                test = s[ind: i+1]
                if test == test[::-1]:
                    substring = test
            if len(substring) > len(output):
                output = substring

        return output
