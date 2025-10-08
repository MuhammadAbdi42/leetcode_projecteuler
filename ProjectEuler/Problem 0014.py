LIMIT = int(1e6)


sequences = {1: 1, 2: 2, 4: 3}


def collatz_sequence_term_count(n: int) -> int:
    if n in sequences:
        return sequences[n]

    terms = [n]
    while terms[-1] not in sequences.keys():
        if terms[-1] % 2 == 0:
            terms.append(terms[-1]//2)
        else:
            terms.append(3*terms[-1] + 1)

    for i in range(2, len(terms) + 1):
        sequences[terms[-i]] = sequences[terms[-1]] + (i - 1)

    return sequences[n]


index, maxx = 0, 0
for i in range(1, LIMIT):
    if collatz_sequence_term_count(i) > maxx:
        maxx = collatz_sequence_term_count(i)
        index = i

print(index)
