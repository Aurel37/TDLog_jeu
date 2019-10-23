#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import main

"""
The tests are realised with the text document in the folder of the programm,
the .txt documents used are 'TheForest', 'test_char_map' and 'test_dim_map'
to run this file go in your terminal and go in the folder where the programm is
then write the command : python -m unittest -v test_error_gestion
"""


class TestGrid(unittest.TestCase):
    """
    TestGrid tests the class Grid,
    it tests if the functions size and set works with the map 'TheForest'
    """
    def setUp(self):
        my_file = file_reader("TheForest")
        self.grid = Grid(my_file[0], my_file[1], my_file[2])

    def test_size(self):
        self.assertEqual((self.grid.m, self.grid.n), (40, 18))

    def test_set(self):
        self.grid.set(5, 5, '#')
        self.assertEqual(self.grid.get(5, 5), '#')
        with self.assertRaises(ValueError):
            self.grid.set(45, 45, '#')


class TestObjects(unittest.TestCase):
    """
    TestMoving_objects tests the class Moving_objects,
    it tests only the function move in case the object is a player
    with the map 'theForest'
    """
    def setUp(self):
        my_file = file_reader("TheForest")
        self.grid = Grid(my_file[0], my_file[1], my_file[2])
        self.player_object = Objects(my_file[-1][0][0],
                                            my_file[-1][0][1],
                                            self.grid, 1)

    def test_move(self):
        with self.assertRaises(AssertionError):
            self.player_object.move(-10, -10, self.grid)
        self.assertEqual(self.player_object.move(0, -1, self.grid), 0)
        self.assertEqual(self.player_object.move(0, 1, self.grid), 1)


class Testfilegestion(unittest.TestCase):
    """
    Testfilegestion tests the functions of the Module 'file_gestion',
    the maps used for the tests are 'test_char_map'to check if the
    function file_reader detect an unauthorised character and
    'test_dim_map' to check if file_reader detects if the map
    is not a rectangle
    """

    def test_file_reader(self):
        self.assertEqual(file_reader('test_char_map'), [0, 0, 0, False, 0])
        self.assertEqual(file_reader('test_dim_map'), [0, 0, 0, False, 0])
        with self.assertRaises(FileNotFoundError):
            file_reader('blank_file')

    def test_display_listname(self):
        self.assertEqual(display_listname('map_names'),
                         ['ThePrison\n', 'TheForest\n',
                          'TheTunnel\n', 'PracticeField'])
