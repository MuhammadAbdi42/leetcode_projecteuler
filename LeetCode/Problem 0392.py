class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0
        for char in s:
            if ind >= len(t):
                return False

            if char in t[ind:]:
                ind = ind + t[ind:].index(char) + 1
            else:
                return False

        return True
