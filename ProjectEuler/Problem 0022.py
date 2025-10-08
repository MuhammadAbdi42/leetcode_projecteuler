import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'Files', '0022.txt')
with open(file_path, 'r') as f:
    names = f.read().upper().strip('''"''').split('''","''')
    names.sort()

output = 0
for i, name in enumerate(names):
    score = 0
    for letter in name:
        score += ord(letter) - 64
    output += score * (i + 1)

print(output)
