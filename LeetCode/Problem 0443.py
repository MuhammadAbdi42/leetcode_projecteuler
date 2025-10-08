from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while i < len(chars):
            letter = chars[i]
            count = 1

            while True:
                if i + 1 != len(chars):
                    if chars[i+1] == letter:
                        count += 1
                        i += 1
                    else:
                        i += 1
                        break
                else:
                    i += 1
                    break

            chars[j] = letter
            j += 1
            if count != 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1

        return j
