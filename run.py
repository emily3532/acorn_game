"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Runs the Acorn game
"""
from game import Game
import os
import sys

# Check proper input
if len(sys.argv) <=1:
    print("Usage python run.py <filename> [play]")
    sys.exit()

# Create game object
filename = sys.argv[1]
game = Game(filename)
game.board()
end, cell = game.game_cell()
print(game.board())

while True:
    # Move player in game
    move = input("Input a move: ").lower()

    if len(sys.argv) == 3:
        if sys.argv[2] == 'play':
            os.system("clear")

    gamemove= game.game_move(move)

    if gamemove == 'quit':
        print("\nBye!")
        sys.exit()
    game.board()
    end, cell = game.game_cell()

    if end == False:
        print(game.board())
        print(cell)
        sys.exit()

    print(game.board())
    if end == True:
        print(cell)
   
   # Handles out of bounds/incorrect moves 
    if gamemove == 'invalid':
        print("Please enter a valid move (w, a, s, d, e, q).\n")

    if gamemove == 'out':
        print("You walked into a wall. Oof!\n")



