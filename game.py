def step(grid, chain, players):
    """
    manage one step of the game
    grid : the grid
    chain : the instruction (a character string)
    player : class of the players
    """
    steps = list(chain)
    nbstep = len(steps)
    finish = True
    number_player = 0
    for i in range(nbstep):
        command = steps[i]
        dx = 0
        dy = 0
        try:
            int(command)
        except ValueError:
            if (finish):
                if (command == ">"):
                    dx = 1
                elif (command == "v"):
                    dy = 1
                elif (command == "^"):
                    dy = -1
                elif (command == "<"):
                    dx = -1
                elif (command == "s"):
                    finish = False
                if (number_player > 0):
                    limit = players[number_player-1].move(dx, dy, grid)
                    if (limit == 2):
                        print("we find the door")
                        finish = False
                grid.display()
        else:
            number_player = int(command)
    return not finish
