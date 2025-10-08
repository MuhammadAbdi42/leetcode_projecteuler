class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = 'AaEeIiOoUu'

        temp = 0
        for i in range(k):
            if s[i] in VOWELS:
                temp += 1
        max_vowel = temp

        for i in range(1, len(s) - k + 1):
            if s[i - 1] in VOWELS:
                temp -= 1
            if s[i + k - 1] in VOWELS:
                temp += 1
            if temp > max_vowel:
                max_vowel = temp

        return max_vowel
