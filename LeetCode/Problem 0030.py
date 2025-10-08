from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        total_length = len(words) * word_length

        need = Counter(words)

        output = []
        for i in range(0, len(s) - total_length + 1):
            window = s[i:i + total_length]
            valid = True

            if len(need) == 1:
                check_word = words[0] * need[words[0]]
                if window == check_word:
                    output.append(i)
                    continue

            seen = {}
            for j in range(len(words)):
                check_word = window[j * word_length: (j+1) * word_length]
                if check_word in need:
                    if check_word not in seen:
                        seen[check_word] = 1
                    else:
                        if seen[check_word] >= need[check_word]:
                            valid = False
                            break
                        else:
                            seen[check_word] += 1
                else:
                    valid = False
                    break

            if valid:
                output.append(i)

        return output
