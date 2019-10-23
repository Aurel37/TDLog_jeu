# -*- coding: utf-8 -*-
"""
MOREL Sébastien PION Aurélien
"""

def is_player(val):
    """
    Check if the character val represent and number, here a player
    val : a charcater
    >>> is_player("1")
    (True, 1)
    >>> is_player("*")
    (False, -1)
    """
    try:
        int(val)
    except ValueError:
        return False, -1
    else:
        return True, int(val)


def find_pos_val(grid, x, y):
    """
    Allows us to acces the element of x, y but gives us the list
    of the value and its position into the grid
    """
    if(x <= grid.m and 0 <= x and y <= grid.n and 0 <= y):
        return [grid.get(x, y), x, y]
    else:
        raise ValueError("Out of Boundaries")

def origin_turnstile(x, y, grid):
    """
    Search the origin of a turntile,
    x, y : coordiantes of the player
    grid : the grid
    """
    x_turnstile = 0
    y_turnstile = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            val = grid.get(i + x, j + y)
            if(val == "%"):
                x_turnstile = i + x
                y_turnstile = j + y

    return x_turnstile, y_turnstile


class Objects:
    """
    DESCRITPION

    This is the class of each moving objets, such as a box or the player

    VALUES

    (x, y) :  initial position of the object
    grid : the grid
    val0  : either "1" if the class represent an object,
            either "*" if the class represent a crate
    """

    def __init__(self, x, y, grid, val0):
        self.x = x
        self.y = y
        self.val = val0
        grid.set(x, y, self.val)

    def find_configuration(self, dx, dy, grid):
        """
        Gives us the list of the final position of the turnstile
        """

        x = self.x + dx
        y = self.y + dy
        val = grid.get(x, y)
        x_turnstile, y_turnstile = origin_turnstile(x, y, grid)
        xturn = x_turnstile - x
        yturn = y_turnstile - y
        right = x + dx
        left = x - dx
        up = y + dy
        down = y - dy
        configuration = [[self.val, self.x, self.y],
                         [val, x, y],
                         find_pos_val(grid, right, up),
                         find_pos_val(grid, right + xturn, up + yturn),
                         find_pos_val(grid, right + 2*xturn, up + 2*yturn),
                         find_pos_val(grid, x + 2*xturn, y + 2*yturn),
                         find_pos_val(grid, left + 2*xturn, down + 2*yturn),
                         find_pos_val(grid, left + xturn, down + yturn),
                         ]
        return configuration

    def move(self, dx, dy, grid):
        """
        - return 0 if the object can't move, 1 if it can,
            2 if the object move onto a hole
        - (dx, dy) : indicates the modification of the
            coordinates of the object
        - grid : the  grid
        """
        assert(self.x + dx <= grid.m and 0 <= self.x + dx
               and self.y + dy <= grid.n and 0 <= self.y + dy)
        x = self.x + dx
        y = self.y + dy
        val = grid.get(x, y)

        if (val == " "):

            grid.set(self.x, self.y, " ")
            self.x = x
            self.y = y
            grid.set(self.x, self.y, self.val)
            return 1

        if (val == "*"):

            crate = Moving_objects(x, y, grid, "*")
            dep = crate.move(dx, dy, grid)

            if (dep == 1):

                grid.set(self.x, self.y, " ")
                self.x = x
                self.y = y
                grid.set(self.x, self.y, self.val)
                return 1
            else:
                print('Bump')
                return 0

        if (val == "°" and is_player(self.val)[0]):
            # if the object is a player that enter a turnstile

            x_turnstile, y_turnstile = origin_turnstile(x, y, grid)
            # Let's find where is the turnstile(x, y, grid)
            if (self.x == x_turnstile or self.y == y_turnstile):
                # If the turstile and the x are one the same line,
                # nothing happens
                print('Bump')
                return 0
            else:  # We first need to see if the turnstile can move:
                configuration = self.find_configuration(dx, dy, grid)
                can_turn = True
                for i in range(1, 7):
                    if(configuration[i][0] == "°" and
                       configuration[i + 1][0] != " "):
                        # if no one blocks the turnstile
                        can_turn = False
                if (can_turn):

                    print("erase")
                    grid.set(self.x, self.y, " ")
                    self.x = x + dx
                    self.y = y + dy
                    grid.set(self.x, self.y, self.val)

                    for i in range(4):
                        grid.set(configuration[2*i + 1][1],
                                 configuration[2*i + 1][2],
                                 configuration[2*i - 1][0]
                                 )
                    return 1
                else:
                    return 0
        # manage the dynamic of a player, it is necessary
        # to check if the class represent a player first
        try:
            # check if the class represent an object
            int(self.val)
        except ValueError:
            if (val == "o" and self.val == "*"):

                grid.set(self.x, self.y, " ")
                self.x = x
                self.y = y
                grid.set(self.x, self.y, " ")
                return 1

            if (val == "O" and self.val == "*"):
                grid.set(self.x, self.y, " ")
                grid.set(x, y, "o")
        else:
            if (val == "@"):

                grid.set(self.x, self.y, " ")
                self.x = x
                self.y = y
                grid.set(self.x, self.y, "$")
                return 2

        print('Bump')
        return 0

