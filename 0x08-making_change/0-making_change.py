#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <=0:
        return 0
    count = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
        if(total == 0):
            return count
    return -1
