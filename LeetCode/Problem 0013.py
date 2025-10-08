class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        roman_subtractions = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        output = 0
        while s:
            if s[0:2] in roman_subtractions:
                output += roman_subtractions[s[0:2]]
                s = s[2:]
            else:
                output += roman_to_int[s[0]]
                s = s[1:]

        return output
