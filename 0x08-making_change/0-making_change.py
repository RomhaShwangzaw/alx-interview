#!/usr/bin/python3
""" Making Change Module
"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed
        to meet a given amount `total`.

        Params:
          * coins - a list of the values of the coins in our possession
          * total - the total amount of coins needed

        Return: fewest number of coins needed to meet total
          - If total is 0 or less, return 0
          - If total cannot be met by any number of coins we have, return -1

        Assumptions:
          - The value of a coin will always be an integer greater than 0
          - We have an infinite number of each denomination of coin in the list
    """
    if total <= 0:
        return 0

    coins.sort()
    coins.reverse()
    no_of_coins = 0
    for c in coins:
        no_of_coins += total // c
        total = total % c
        if total == 0:
            return no_of_coins

    return -1
