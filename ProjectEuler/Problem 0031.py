from typing import List

COINS = [1, 2, 5, 10, 20, 50, 100, 200]  # Converted to pence
TARGET = 200  # Converted to pence


def coin_options(coins: List[int], target: int) -> int:
    if target == 0:
        return 1
    if len(coins) == 1:
        if target % coins[0] == 0:
            return 1
        else:
            return 0

    coin = coins[0]
    output = 0

    i = 0
    while i * coin <= target:
        output += coin_options(coins[1:], target - i * coin)
        i += 1

    return output


print(coin_options(COINS, TARGET))
