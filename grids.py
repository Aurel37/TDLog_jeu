# -*- coding: utf-8 -*-
"""
MOREL Sébastien PION Aurélien
"""

import rules
import file_gestion
import objects

Possible_Values = [" ", "#", "o", "O", "*", "1", "2",
                   "3", "4","@", "x", "°", "%"]


class Grid:
    """
    DESCRIPTION

    Class grid, containing the map (an array), the dimension of the map and the
    initial position of the player

    VALUES

    (n0,m0) : dimension of the map
    (x,y) : initial position of the player
    """

    def __init__(self, m0, n0, tab):
        # dimension
        self.n = n0
        self.m = m0
        # map (an array of charachters)
        self.tab = tab
        # initialisation of the walls around the map

    def set(self, x, y, val):
        """
        transform the value of the map by val
        (x, y) : coordinates of the value to change
        val : the new value of (x,y)
        """
        if(x <= self.m and 0 <= x and y <= self.n and 0 <= y):
            if(val in Possible_Values):
                self.tab[x + y * self.m] = val
        else:
            raise ValueError("Out of Boundaries")

    def get(self, x, y):
        """
        return the coordinates (x, y) of the tab
        (x,y) : coordinates to return
        """
        if(x <= self.m and 0 <= x and y <= self.n and 0 <= y):
            return self.tab[x + y * self.m]
        else:
            raise ValueError("Out of Boundaries")

    def display(self):
        """
        display the map
        """
        Map = ''
        for i in range(0, self.n):
            for j in range(0, self.m):
                Map += self.get(j, i)
            Map += '\n'
        print(Map)

    def put(self, x, y, val):
        """
        Check if we can use set during the game only
        """
        assert(self.tab[x + y * self.m] == " ")
        self.set(x, y, val)


def grid_init():
    """
    Initialise the game, upload a map wanted by the player,
    ask how many players will play (between 1 and 4)
    Return a grid, a list of players and a boolean
    to end the game if necessecary
    """
    end = True
    map_valid = True
    # list of players
    players = []
    numbers = ['1', '2', '3', '4']
    rules.display_rules()
    map_names_lignes = file_gestion.display_listname('map_names')
    # the player choose a map
    while (map_valid):
        file = input("\nEnter the name of a map : ")
        try:
            my_file = file_gestion.file_reader(file)
        except FileNotFoundError:
            print("This map doesn't exist, please enter an other map's name")
            # both take in this case the same value
            map_valid = end = rules.keep_going()
        else:
            map_valid = not(my_file[3])
            if (map_valid):
                print("This map is not valid, please enter another map")
                map_valid = end = rules.keep_going()
    number_valid = True
    number = 0
    # then he choose a number of players
    while (number_valid):
        number = input("Please enter a number of players between 1 and 4: ")
        try:
            number_of_player = int(number)
        except ValueError:
            print("You didn't enter a digit-number")
            end = number_valid = rules.keep_going()
        else:
            if (0 < number_of_player and number_of_player <= 4):
                number_valid = False
        if(number_valid):
            print("To many players have been chose") 
    # if end = True the, the map is valid as  well as the number of player
    if (end):
        grid = Grid(my_file[0], my_file[1], my_file[2])
        for i in range(number_of_player):
            players.append(objects.Objects(my_file[-1][i][0],
                                          my_file[-1][i][1],
                                          grid, numbers[i]))
        return (grid, players, end)
    return ((), (), end)


