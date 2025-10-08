LIMIT = 1000


def num_to_words(n: int) -> str:
    # Under 10000

    digits_to_word = {0: '',
                      1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                      6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',

                      10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                      15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',

                      20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                      60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',

                      100: 'hundred', 1000: 'thousand'}

    digits = [0, 0, 0, 0]
    i = 0
    while n > 0:
        digits[i] = n % 10
        n //= 10
        i += 1

    output = ''
    if digits[-1] > 0:
        output += digits_to_word[digits[-1]] + digits_to_word[1000]
        if digits[-2] > 0 or digits[-3] > 0 or digits[-4] > 0:
            output += 'and'
    if digits[-2] > 0:
        output += digits_to_word[digits[-2]] + digits_to_word[100]
        if digits[-3] > 0 or digits[-4] > 0:
            output += 'and'
    if digits[-3] * 10 + digits[-4] > 0:
        if digits[-3] * 10 + digits[-4] in digits_to_word:
            output += digits_to_word[digits[-3] * 10 + digits[-4]]
        else:
            output += digits_to_word[digits[-3]
                                     * 10] + digits_to_word[digits[-4]]

    return output


sumx = 0
for i in range(1, LIMIT+1):
    sumx += len(num_to_words(i))

print(sumx)
