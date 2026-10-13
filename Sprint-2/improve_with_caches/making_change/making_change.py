from typing import List

cache = {}

def ways_to_make_change(total: int) -> int:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return ways_to_make_change_helper(total, coins)


def ways_to_make_change_helper(total: int, coins: List[int]) -> int:
    if total == 0:
        return 1

    if total < 0 or len(coins) == 0:
        return 0

    key = (total, tuple(coins))

    if key in cache:
        return cache[key]

    coin = coins[0]

    ways = 0

    for count in range(total // coin + 1):
        remaining = total - count * coin

        ways += ways_to_make_change_helper(remaining, coins[1:])

    cache[key] = ways

    return ways
