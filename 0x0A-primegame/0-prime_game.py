#!/usr/bin/python3
"""Prime Number Game Module
"""


def isPrime(a):
    """Determines if a number is a prime number or not.
    Return:
      - True if `a` is a prime number, False otherwise.
    """
    if a < 2:
        return False
    for i in range(2, (a // 2) + 1):
        if a % i == 0:
            return False
    return True


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

    player1 = {
        'name': "Maria",
        'winCount': 0
    }
    player2 = {
        'name': "Ben",
        'winCount': 0
    }
    player = player1

    for i in range(x):
        # Create the list of numbers
        gameNums = list(range(1, nums[i] + 1))
        gameNumsCopy = gameNums.copy()
        for a in gameNums:
            if a not in gameNumsCopy:
                continue
            # Check if the number is prime and
            # remove it and its multiples
            if isPrime(a):
                gameNumsCopy.remove(a)
                for b in gameNumsCopy:
                    if b % a == 0:
                        gameNumsCopy.remove(b)
                # Switch players
                if player == player1:
                    player = player2
                else:
                    player = player1
                continue
        # Check which player won the round
        if player == player1:
            player2['winCount'] += 1
        else:
            player1['winCount'] += 1
        # End of round. Commence with player1.
        player = player1

    # Declare overall winner
    if player1['winCount'] > player2['winCount']:
        return player1['name']
    elif player1['winCount'] < player2['winCount']:
        return player2['name']
    else:
        return None
