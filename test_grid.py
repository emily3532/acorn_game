from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game_parser import read_lines, parse


def test_grid():
    """ Tests if grid output is correct.
        Expected: Board represented in string and message with number of buckets 
    """
    #DUMMY VARIABLES
    board, sr, sc = read_lines('board_test.txt')
    player = Player(0,0,1)
    board, cell, tele = grid_to_string(board, player)
    actual = board
    expected = "*A**2*\n*2  5*\n*W F5*\n**Y***\n\nYou have 0 water buckets.\n"
    assert actual == expected, 'Test for grid 1 failed'
    
    """ Tests if grid output is correct with different player locations and different amount of water
        Expected: Board represented in string with correct player location and message with number of 1 bucket.
    """
    player = Player (1,1,1)
    board, sr, sc = read_lines('board_test.txt')
    board, cell, tele = grid_to_string(board, player)
    actual = board
    expected = "*X**2*\n*A  5*\n*W F5*\n**Y***\n\nYou have 1 water bucket.\n"
    assert actual == expected, 'Test for grid 2 failed' 

    """ THERE IS NO NEED FOR NEGATIVE TEST CASES AS THE INPUT INTO GRID IS ALWAYS GUARANTEED TO BE A LIST OF
        LIST OF CELLS FROM READ_LINES AND PLAYER IS ALWAYS GOING TO BE A PLAYER CLASS. 
    """


    #Below tests are for my own functions added, not part of requirements
    """ Tests if cell function is correct
        Expected: Correctly identifies cell type as teleport
    """
    actual = type(cell)
    expected = Teleport
    assert actual == expected, "Test for grid cell failed"

    """ Tests if teleport function is correct
        Expected: Correctly identifies cell type as teleport
    """
    actual = tele
    expected = [('2', 0, 4), ('2', 1, 1), ('5', 1, 4), ('5', 2, 4)]
    assert actual == expected, 'Test for grid teleports failed'


def run_tests():
    test_grid()

run_tests()