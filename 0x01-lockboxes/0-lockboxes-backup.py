#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened.

    Params: @boxes: a list of lists of integers.
    Description: A key with the same number as a box opens that box.
                 There can be keys that do not have boxes.
                 The first box boxes[0] is unlocked.
    Return True if all boxes can be opened, else return False
    """
    if not boxes or not boxes[0]:
        return False

    boxesLockStatus = [True] * len(boxes)
    boxesLockStatus[0] = False
    canUnlockAllRecursive(boxes, 0, boxesLockStatus)
    for boxLockStatus in boxesLockStatus:
        if boxLockStatus is True:
            return False
    return True


def canUnlockAllRecursive(boxes, boxIndex, boxesLockStatus):
    """a method that determines if all the boxes can be opened recursively.

    Params: @boxes: a list of boxes.
            @boxIndex: the index of the open box.
            @boxesLockStatus: a list containing the lock state of the boxes.
    Description: A key with the same number as a box opens that box.
                 There can be keys that do not have boxes.
                 The first box boxes[0] is unlocked.
                 Updates the boxesLockStatus array.
    """
    for n in boxes[boxIndex]:
        if n < len(boxesLockStatus) and boxesLockStatus[n] is True:
            boxesLockStatus[n] = False
            canUnlockAllRecursive(boxes, n, boxesLockStatus)
