"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Creates player class
"""
class Player:
    def __init__(self, buckets, row, column):
        self.display = 'A'
        self.num_water_buckets = buckets
        self.row = row
        self.col = column

    def move(self, move):
        self.move = move
        if self.move == "s":
            self.row += 1
        elif self.move == "w":
            self.row -= 1
        elif self.move == "d":
            self.col +=1
        elif self.move == "a":
            self.col -= 1
        elif self.move == "e":
            pass
        else:
            return False

    def get_p_position(self):
        return self.row, self.col

 

