class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for ind, char in enumerate(s):
            if char in 'AaEeIiOoUuac':
                vowels.append((ind, char))

        l, r = 0, len(vowels) - 1
        while l < r:
            l_ind, l_vowel = vowels[l][0], vowels[l][1]
            r_ind, r_vowel = vowels[r][0], vowels[r][1]

            s = s[:l_ind] + r_vowel + s[l_ind+1:r_ind] + l_vowel + s[r_ind+1:]

            l += 1
            r -= 1

        return s
