import os
from typing import List

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'Files', '0079.txt')
with open(file_path, 'r') as f:
    key_logs = f.read().split('\n')


passcode = ''
while key_logs:
    last_digits = set()

    for key in key_logs:
        last_digits.add(key[-1])

    not_absolute = set()

    for digit in last_digits:
        for key in key_logs:
            if digit in key and key.index(digit) != len(key) - 1:
                not_absolute.add(digit)

    selected = list(last_digits - not_absolute)[0]

    for i in range(len(key_logs)):
        if selected in key_logs[i]:
            key_logs[i] = key_logs[i].replace(selected, '')

    key_logs = list(filter(lambda x: x != '', key_logs))

    passcode = selected + passcode

print(passcode)
