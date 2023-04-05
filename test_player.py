from player import Player

def test_player():
    
    """ Tests if configuration of class is correct
        Expected: display value 'A', water value 0, row value 1, col value 1
    """
    p = Player(0, 1, 1)
    assert p.display == 'A', 'Player display failed'
    assert p.num_water_buckets == 0, "Player buckets failed"
    assert p.row == 1, 'Player row failed'
    assert p.col == 1, 'Player col failed'

    """ Tests if move method of class is correct
        Expected: 'a' will -1 from col
    """
    p.move('a')
    assert p.col == 0, 'Player move failed'
    

    """ Tests reaction to unknown inputs (not a,w,s,d,e,or q)
        Expected: False
    """
    p = Player(0, 1, 0)
    assert p.move('g') == False, 'Player invalid input failed'

    """ Tests reaction to 'e'
        Expected: None
    """
    p = Player(0, 1, 0)
    assert p.move('e') == None,"Player move 'e' failed"

    #Below tests are for my own functions added, not part of requirements
    """ Tests get position after moving
        Expected: (0, 1)
    """
    p = Player(0,0,0)
    p.move('d')
    assert p.get_p_position() == (0, 1),'Player position failed'

def run_tests():
    test_player()


run_tests()