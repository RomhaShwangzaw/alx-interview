#!/usr/bin/python3
"""Minimum Operations Module"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n `H` characters in the file. The
    only operations allowed are `Copy All` and `Paste`.

    Returns an integer.
    If n is impossible to achieve, return 0.

    Example:

    n = 9

    H => Copy All => Paste => HH => Paste => HHH =>
    Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

    Number of operations: 6
    """
    total_chars = 1  # no. of H's in the file
    clipboard = 0  # no. of H's copied
    counter = 0  # operations counter

    while total_chars < n:
        # if nothing has been copied yet
        if clipboard == 0:
            # copy all
            clipboard = total_chars
            # paste
            total_chars += clipboard
            # increment operations counter
            counter += 2
            # continue to next loop
            continue

        remaining = n - total_chars  # remaining chars to paste
        # if clipboard contains more chars than remaining
        # it's impossible to arrive at the desired result
        if remaining < clipboard:
            return 0

        # if remaining is not a multiple of the total_chars
        # we only paste what's in the clipboard
        if remaining % total_chars != 0:
            # paste current clipboard
            total_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copy all
            clipboard = total_chars
            # paste
            total_chars += clipboard
            # increment operations counter
            counter += 2

    return counter
