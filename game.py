"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Creates game class
"""
from game_parser import read_lines
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

class Game:
    def __init__(self, filename):
        self.filename = filename
        self.new_board,row,col = read_lines(filename)
        self.row = row
        self.col = col
        self.water = 0
        self.counter = -1 
        self.move_ls = []
    
    def board(self):
        """Repositions players location in the grid and identifies the cell the player stepped on.
        
        Arguments: 
        self -- game instance

        Returns:
        self.grid: A grid with player printed in new location. 
        """  
        self.player = Player(self.water, self.row,self.col)
        self.grid,self.cell, self.teleport = grid_to_string(self.new_board, self.player)
        return self.grid

    def game_cell(self):
        """Initiates the step method for cell the player has stepped on.
        
        Arguments: 
        self -- game instance

        Returns:
        boolean: True -- if there is message to print, False -- if the game needs to end, None -- if no actinos needed
        message: A string with message needed to be printed. 
        """  
        if type(self.cell) == Start:
            self.cell.step(self)
            return None, ''

        elif type(self.cell) == Wall:
            end, message = self.cell.step(self)
            self.move_ls.pop(-1)
            return True, message

        elif type(self.cell) == End:
            end, message = self.cell.step(self)
            return False, message

        elif type(self.cell) == Air:
            self.cell.step(self)
            return None, ''

        elif type(self.cell)== Fire:
            end, message = self.cell.step(self)
            if end == False:
                return False, message

            else:
                return True, message

        elif type(self.cell) == Water:
            end, message = self.cell.step(self)
            return True, message

        elif type(self.cell) == Teleport:
            r, c, message = self.cell.step(self)
            self.row = r
            self.col = c
            return True, message

 
    def game_move(self, move):
        """Moves players location according to input and adds move to list of moves.
        
        Arguments: 
        self -- game instance
        move -- users inputted move command

        Returns:
        string: quit -- if game needs to quit, invalid -- if input was invalid, out -- if player is out of bounds
        """  
        self.move = move
        if move == "q":
            return 'quit'

        if self.player.move(self.move) == False:
            self.counter -=1
            return 'invalid'

        row, col = self.player.get_p_position()
        # Checks if player is out of bounds
        if row < 0 or col < 0 or row > (len(self.new_board)-1) or col > (len(self.new_board[0])-1):
            self.counter -=1
            return 'out'

        # Updates players location and adds it to list of moves
        else:
            self.row = row
            self.col = col
            self.move_ls.append(self.move)
    

    def get_moveLs(self, input):
        
        # Removes move from list if incorrectly added
        if input == "remove":
            self.move_ls.pop(-1)

        return self.move_ls


    def get_moves(self):
        return self.move

  
    def moves_made(self):
        self.counter +=1
        return self.counter

   
    def get_position(self):
        return self.row, self.col


    def get_teleports(self):
        return self.teleport
    
  
    def change_air(self):
        self.new_board[self.row][self.col] = Air()

    def get_water(self):
        return self.water

    def add_water(self):
        self.water+=1
  
    def destroy_water(self):
        self.water -=1
        if self.water < 0:
            self.water = 0