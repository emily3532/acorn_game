"""
Author: Emily Wong
Date: 28 May 2020
Purpose: Creates cell classes 
"""
class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        self.game = game
        self.game.moves_made()

class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        self.game = game
        moves = game.moves_made()
        moves_ls = game.get_moveLs(None)

        if moves == 1:
             message = "\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, "\
            "restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n" \
                "\nYou made {} move.\nYour move: {}\n\n=====================\n====== YOU WIN! =====\n=====================".format(moves, ', '.join(moves_ls))

        else:
            message = "\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, "\
                "restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n" \
                    "\nYou made {} moves.\nYour moves: {}\n\n=====================\n====== YOU WIN! =====\n=====================".format(moves, ', '.join(moves_ls))

        return False, message

class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        self.game = game
        self.game.moves_made()


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        self.game = game
        
        # Section A: Undo move if walk into wall
        if game.get_moves() == "d":
            self.game.game_move("a")
            game.get_moveLs('remove')

        elif game.get_moves() == "a":
            self.game.game_move("d")
            game.get_moveLs('remove')

        elif game.get_moves() == "w":
            self.game.game_move("s")
            game.get_moveLs('remove')

        elif game.get_moves() == "s":
            self.game.game_move("w")
            game.get_moveLs('remove')

        return None, ("You walked into a wall. Oof!\n")
        
        

class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        self.game= game
        moves = game.moves_made()
        moves_ls = game.get_moveLs(None)

        if self.game.get_water() > 0:
            self.game.destroy_water()
            self.game.change_air()
            return None, ("With your strong acorn arms, you throw a water bucket at the fire. "\
                "You acorn roll your way through the extinguished flames!\n")
    
        else:
            message = "\nYou step into the fires and watch your dreams disappear :(.\n"\
                "\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a "\
                    "pile of ash and is scattered to the winds by the next storm... "\
                        "You have been roasted.\n\nYou made {} moves.\nYour moves: {}\n"\
                            "\n=====================\n===== GAME OVER =====\n=====================".format(moves, ', '.join(moves_ls))
            return False, message


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        self.game = game
        self.game.moves_made()
        self.game.add_water()
        self.game.change_air()

        return None, ("Thank the Honourable Furious Forest, you've found a bucket of water!\n")


class Teleport:
    def __init__(self, pads):
        self.display = pads

    def step(self, game):
        self.game=game
        self.game.moves_made()
        row, col = self.game.get_position()
        message = "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n"

        # Section A: Tests where the matching teleport is on the grid
        t = game.get_teleports()
        i = 0
        j = 0
        while i< len(t):
            
            # Section B: Finds matching teleport
            if self.display == t[i][0]:

                if t[i][1] == row and t[i][2] == col:
                    j = i
                    pass

                # Section C: Returns teleport's pair location
                else:
                    return t[i][1], t[i][2], message
            i+=1
        
        #Re-teleports if move is held
        if game.get_moves() == "e":
            return t[j][1], t[j][2], message