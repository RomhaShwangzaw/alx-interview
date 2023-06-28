#!/usr/bin/python3
"""Prime Number Game Module
"""


def isWinner(x, nums):
    """Prime Number Game Function
    Args:
      - x: the number of rounds to be played.
      - nums: an array of numbers containing the highest range
              of an array to choose prime numbers from.
    Return:
      - name of the player that won the most rounds.
      - If the winner cannot be determined, `None` is returned.
    Description:
      - Maria and Ben are playing a game. Given a set of consecutive integers
        starting from 1 up to and including n, they take turns choosing a prime
        number from the set and removing that number and its multiples from the
        set. The player that cannot make a move loses the game.
      - They play x rounds of the game, where n may be different for each
        round. Assuming Maria always goes first and both players play
        optimally, determine who the winner of each game is.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
