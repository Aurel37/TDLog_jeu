# -*- coding: utf-8 -*-
"""
MOREL Sébastien PION Aurélien
"""

import grids
import game


def main():
    """
    Code the entiere game: we display every moove and while we don't reach the
    door or while we aren't stuck, it we continue to ask you what moves
    you want to put
    """
    grid, players, end = grids.grid_init()
    if (end):
        grid.display()
        grid.display()
        val = input("Select your moves:")
        while(not game.step(grid, val, players)):
            val = input("Select your moves: (Press s if you are stuck)")
        return "Victory"


if __name__ == "__main__":
    main()
