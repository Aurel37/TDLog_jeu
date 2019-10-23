# -*- coding: utf-8 -*-
"""
MOREL Sébastien PION Aurélien
"""

def display_rules():
    print("You can play from 1 to 4 players to this game.")
    print("The rules are simple.")
    print("Write the number of the player you want to ")
    print("move then write its instruction.")
    print("The instructions are :\n >: you move to the right")
    print("<: you move to the left\n^: you move upward,")
    print(" v: you move downward")
    # the names of the map are first printed
    print("\nThe maps available are:")


def keep_going():
    """
    Ask the player if he wants to stop the game
    Return a bool according to the answer
    Exemples:
    if you press y:
    >>> keep_going()
    Do you want to quit the game ? (y/n)False
    if you press anything else:
    >>> keep_going()
    Do you want to quit the game ? (y/n)True
    """
    keep_going = input("Do you want to quit the game ? (y/n)")
    if keep_going == "y":
        return False
    return True

