class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        i = 0
        while i < len(word1) and i < len(word2):
            output += word1[i] + word2[i]
            i += 1

        if len(word1) > i:
            output += word1[i:]
        if len(word2) > i:
            output += word2[i:]

        return output
