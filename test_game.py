from game import Game
from player import Player 

def test_game():
    
    """ Tests game class constructor
        Expected: filename to be what is given, water = 0, counter = -1
    """
    game= Game('board_test.txt')
    assert game.filename == 'board_test.txt', "game filename failed"
    assert game.water == 0, 'game water attribute failed'
    assert game.counter == -1, 'game counter failed'

    """ Tests game board correctly made
        Expected: game board with number of buckets of water
    """
    actual = game.board()
    expected = "*A**2*\n*2  5*\n*W F5*\n**Y***\n\nYou have 0 water buckets.\n"
    assert actual == expected, "Game board failed"

    """ Tests game cell identifier method
        Expected: teleport cell message
    """
    game.row = 1
    game.col = 1
    game.board()
    actual, message = game.game_cell()
    assert message == "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n", 'Game cell identification failed'

    """ Tests game move out of bounds
        Expected: 'out'
    """
    game.row = 0
    game.col = 0
    game.board()
    move = 'a'
    actual = game.game_move(move)
    expected = 'out'
    assert actual == expected, 'Out of bounds identification failed'


    """ Tests game move quit input
        Expected: 'quit'
    """
    game.board()
    move = 'q'
    actual = game.game_move(move)
    expected = 'quit'
    assert actual == expected, 'Quit input identification failed'

    """ Tests game invalid input
        Expected: 'invalid'
    """
    game.board()
    move = 'asad'
    actual = game.game_move(move)
    expected = 'invalid'
    assert actual == expected, 'Invalid input identification failed'
    
    
    """ TEST MOVE METHODS, CHANGE TO AIR METHOD USING E2E TESTS, GET METHODS JUST DISPLAY VALUES - NOT AS NECESSARY TO TEST.
    """
def run_tests():
    test_game()

run_tests()