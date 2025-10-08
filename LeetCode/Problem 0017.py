from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_digits = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        output = []
        for digit in digits:
            if not output:
                for char in phone_digits[digit]:
                    output.append(char)
            else:
                temp = []
                for char in phone_digits[digit]:
                    for combination in output:
                        temp.append(combination + char)
                output = temp

        return output
