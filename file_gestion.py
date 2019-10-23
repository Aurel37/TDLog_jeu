#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# the x represent in the map, the initial position of players

Possible_Values = [" ", "#", "o", "O", "*", "1", "2",
                   "3", "4", "@", "x", "°", "%"]


def file_reader(file):
    """
    Read the  file 'file' containing a map, check if the map is  valid,
    and return the coordinates of the players, the dimensions of the map,
    and a list of the map characters file  : a text file
    """
    my_file = open(file + '.txt', 'r')
    # lignes contain a list representing the document
    lignes = my_file.readlines()
    coordinates_players = []
    # dimension of the map
    n = len(lignes)
    m = len(lignes[n - 1])
    tab = []
    # number_of_x check if there not too much position of players
    # put in the map
    number_of_x = 0
    for i in range(n):
        # we delet the '\n' from the ligne i
        new_ligne = lignes[i]
        new_ligne = new_ligne.replace('\n', "")
        for j in range(m):
            if (new_ligne[j] in Possible_Values ):
                if (new_ligne[j] == 'x'):
                    tab.append(' ')
                    if (number_of_x < 4):
                        coordinates_players.append([j, i])
                        number_of_x += 1
                else:
                    tab.append(new_ligne[j])
            else:
                # the map is not valid
                return [0, 0, 0, False, 0]
        if (len(lignes[i]) - 1) != m and i != n - 1:
            return [0, 0, 0, False, 0]
    my_file.close()
    if(number_of_x != 4):
        return [m, n, 0, False, 0]
    else:
        return [m, n, tab, True, coordinates_players]


def display_listname(file):
    """
    Read a file of name and print them
    file :a text file
    """
    my_file = open(file+'.txt', 'r')
    lignes = my_file.readlines()
    for name in lignes:
        print(name, end='')
    my_file.close()
    return lignes
