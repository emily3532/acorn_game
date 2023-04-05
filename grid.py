"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Turns list of list of cells into grid of string
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
from player import(Player)

def grid_to_string(grid, player):
    """Turns a grid and player into a string representing the game board.
        
        Arguments: 
        grid -- list of lists of Cells
        player -- a Player with water buckets
        
        Returns:
            board_with_player: A string representation of the grid and player.
            cell: A cell object the player has stepped on
            ls: A tuple with teleport pads display and location
    """
    board = ''
    ls=[]
    i = 0
    row_counter = 0

    while i < len(grid):
        j = 0
        column_counter = 0

        while j < len(grid[i]):

            if type(grid[i][j]) == Wall:
                k = grid[i][j]
                board += k.display

            elif type(grid[i][j]) == Start:
                row = i
                col = j
                k = grid[i][j]
                board += k.display

            elif type(grid[i][j]) == End:
                k = grid[i][j]
                board += k.display

            elif type(grid[i][j]) == Air:
                k = grid[i][j]
                board += k.display

            elif type(grid[i][j]) == Fire:
                k = grid[i][j]
                board += k.display

            elif type(grid[i][j]) == Water:
                k = grid[i][j]
                board += k.display

            elif type(grid[i][j]) == Teleport:
                k = grid[i][j]
                ls.append((k.display, i, j))
                board += k.display

            j += 1
            column_counter += 1
        board += "\n"
        i += 1
        row_counter += 1
    
    # add player into board
    n = 0
    board_with_player = ''
    player_loc = (player.row) * (column_counter + 1) + (player.col)

    # identify cell stepped on
    cell = grid[player.row][player.col]

    while n < len(board):
        if n == player_loc:
            board_with_player += player.display
        else:
            board_with_player += board[n]
        n+=1

    if player.num_water_buckets == 1:
        board_with_player += "\nYou have {} water bucket.\n".format(player.num_water_buckets)
    else:
        board_with_player += "\nYou have {} water buckets.\n".format(player.num_water_buckets)

    return board_with_player, cell, ls
