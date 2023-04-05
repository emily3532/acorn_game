"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Turns grid into list of list of cells
"""
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
import sys

def read_lines(filename): 
    """Turns a file into a list of list of cells representing the game board.
        
        Arguments: 
        filename -- file containing string of a grid.
        
        Returns:
            parsed: A list of list of cells.
            start_row, start_col: location of the start cell. 
    """
    try:
        f = open(filename, 'r') 
    except FileNotFoundError:
        print ("{} does not exist!".format(filename))
        sys.exit()
    
    lines = []
    i = 0
    while True:
        line = f.readline()
        if line == '':
            break 
        lines.append(line)
    parsed, start_row, start_col = parse(lines)
    f.close()
    return parsed, start_row, start_col


def parse(lines):
    """Turns a line of string into a list of cell objects.
        
        Arguments: 
        lines -- lists of lines of string with cell displays
        
        Returns:
            ls: A list of cells.
            start_row, start_col: location of the start cell. 
    """
    x= Start()
    y= End()
    air = Air()
    wall = Wall()
    fire = Fire()
    water = Water()

    i = 0
    x_count = 0
    y_count = 0
    ls = []
    pair = []
    start_row = 0
    start_col = 0



    while i  <len(lines):
        j = 0
        cells = []


        while j < len(lines[i]):
            if lines[i][j] == x.display:
                x_count += 1
                start_row = i
                start_col = j 
                cells.append(x)

            elif lines[i][j] == y.display:
                y_count += 1
                cells.append(y)

            elif lines[i][j] == air.display:
                cells.append(air)

            elif lines[i][j] == wall.display:
                cells.append(wall) 

            elif lines[i][j] == fire.display:
                cells.append(fire) 

            elif lines[i][j] == water.display:
                cells.append(water) 

            elif lines[i][j].isnumeric():

                if lines[i][j] == '0':
                    raise ValueError("Bad letter in configuration file: 0.")

                teleport = Teleport(lines[i][j])
                pair.append(lines[i][j])
                cells.append(teleport) 

            elif lines[i][j] == "\n":
                break

            else:
                raise ValueError("Bad letter in configuration file: {}.".format(lines[i][j]))

            j += 1

        ls.append(cells)
        i += 1
    
    # Function to test teleport_pairs 
    def teleport_pair(pair):
        """Tests if teleport pairs are correct in grid and their locations.
        
        Arguments: 
        pair -- list of teleport pad cells
        """       
        # Pair is a list of teleport pad numbers
        pair.sort()

        if len(pair) == 1:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pair[0]))

        if pair[0] == pair[1]:
            # This removes pairs from list once found
            pair.remove(pair[1])
            pair.remove(pair[0])

        else:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pair[0]))

    if x_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(x_count))
    if y_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(y_count))

    # Test if teleport pads are correct before testing for teleport pairs
    if len(pair)>0:
        teleport_pair(pair)
    
    return ls, start_row, start_col

