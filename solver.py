"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Solves the acorn game using BFS or DFS
"""
from game import Game
from player import Player
import os
import sys

if len(sys.argv) <=2:
    print("Usage: python3 solver.py <filename> <mode>")
    sys.exit()

mode = sys.argv[2]

def solve(mode):
    """Solves Acorn game using DFS or BFS.
        
    Arguments: 
    mode -- type of solving mode, DFS or BFS

    Returns:
    (if there is a path) game_child: game instance of successful iteration.
    (if there is no path) False 
    """  
    filename = sys.argv[1]
    ls_of_moves = ['s','d','a','w','e']
    
    def node_neighbour(filename, parent, move):
        """Adds a move to the parent game creating a child/neighbour game instance.
        
        Arguments: 
        filename --
        parent --
        move --

        Returns:
        '' or 'Done' or False: 
            '' if the move was sucessful 
            'Done' if the end cell was reached and solution path was found
            False if the move was unsuccessful (eg. walks into wall or into fire without bucket)
        game: The child game instance. 
        """  
        moves = parent.get_moveLs(None)
        game= Game(filename)
        game.board()
        end,cell = game.game_cell()

        for i in moves:
            game.game_move(i)
            game.board()
            end, cell = game.game_cell()
            board=game.board()

        gamemove = game.game_move(move)
        game.board()
        end,cell = game.game_cell()
        game.board()
  

        if "YOU WIN!" in cell:
            return ('Done'), game
        elif "Oof" in cell:
            return False, game
        elif "GAME OVER" in cell:
            return False, game
        else:
            return '', game

    if mode == "DFS":
        game = Game(filename)
        game.board()
        end,cell = game.game_cell()
        nodes_list = [game]
        visited = []

        while True: 
            if len(nodes_list) == 0:
                break
            game = nodes_list.pop(-1)

            for i in ls_of_moves:
                n, game_child = node_neighbour(filename, game, i)
                posr, posc = game_child.get_position()
                position = [posr, posc]

                if n == False:
                    visited.append(position)
                elif n == 'Done':
                    return game_child               
                elif position not in visited:
                    visited.append(position)
                    nodes_list.append(game_child)
                else: 
                    if visited.count(position)<2:
                        visited.append(position)
                        nodes_list.append(game_child)

        return False


    if mode == "BFS":
        game = Game(filename)
        game.board()
        end,cell = game.game_cell()
        nodes_list = [game]
        visited = []
        visited_wat = []

        while True: 
            if len(nodes_list) == 0:
                break
            game = nodes_list.pop(0)

            for i in ls_of_moves:
                n, game_child =node_neighbour(filename, game, i)
                posr, posc = game_child.get_position()
                position = [posr, posc]

                if n == False:
                    visited.append(position)
                elif n == 'Done':
                    return game_child               
                elif position not in visited:
                    visited.append(position)
                    nodes_list.append(game_child)
                else: 
                    if visited.count(position)<2:
                        visited.append(position)
                        nodes_list.append(game_child)
                    
        return False


if __name__ == "__main__":
    solution_found = solve(mode)

    if type(solution_found) == Game:
        game = solution_found
        moves_ls = game.get_moveLs(None)
        num_moves = len(moves_ls)
        print("Path has {} moves.".format(num_moves))
        print("Path: {}".format(', '.join(moves_ls)))
        
    if solution_found == False:
        print("There is no possible path.")
