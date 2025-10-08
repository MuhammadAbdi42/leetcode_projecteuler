from collections import Counter


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter_chars = Counter(s)

        chars = ''.join(list(counter_chars.keys()))
        char_repeats = list(counter_chars.values())

        counter_frequency = Counter(char_repeats)
        k_repeats = [(x, counter_frequency[x])
                     for x in counter_frequency.keys()]
        k_repeats.sort(key=lambda x: (x[1], x[0]), reverse=True)

        target = k_repeats[0][0]

        output = ''
        for i in range(len(char_repeats)):
            if char_repeats[i] == target:
                output += chars[i]

        return output
