from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game import Game
def test_cells():
    """ Tests if Cell display functions are correct
        Expected: Correct display 
    """
    start = Start()
    assert start.display == 'X','Start display failed'
    end = End()
    assert end.display == 'Y','End display failed'
    air = Air()
    assert air.display == ' ', 'Air display failed'
    wall = Wall()
    assert wall.display == '*', 'Wall display failed'
    fire = Fire()
    assert fire.display == 'F', 'Fire display failed'
    water = Water()
    assert water.display == 'W', 'Water display failed'
    teleport = Teleport('1')
    assert teleport.display == '1', 'Teleport display failed'


    """ Tests if Cell step functions are correct - USE E2E tests since the input is heavily reliant on integration with game.py
    """
    

def run_tests():
    test_cells()

run_tests()