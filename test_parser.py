from game_parser import parse, read_lines                                                                          
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def test_read_lines():
    """ Tests if read_lines error is correct.
        Expected: '<filename> does not exist'
    """
    try:
         read_lines('filename')
    except FileNotFoundError as e:
         assert str(e) == 'filename does not exist!'

    """ Tests if read_lines function returns correct list of list of cells.
        Expected: Cell objects (identified through a matrix)
    """
    parsed, start_row, start_col = read_lines('board_test.txt')
    assert type(parsed[0][0]) == Wall, "Read_line_test 1 failed"
    assert type(parsed[1][1]) == Teleport, "Read_line_test 2 failed"
    assert type(parsed[3][2]) == End, "Read_line test 3 failed"


def test_parse():
    """ Tests if parse output is correct.
        line mimics the list that read_lines inputs into parse - list of individual strings from a line of board
        Expected: Cell objects
    """

    line = ['******\n', 'X*****\n', 'Y*****']
    p, row, col = parse(line)
    assert type(p[0][0]) == Wall, "Parse test case 1 failed"
    assert type(p[1][0]) == Start, 'Parse test case 2 failed'
    assert type(p[2][0]) == End, 'Parse test case 3 failed'


    """ Tests if parse raises ValueError when there is no 'Y' in grid 
        line mimics the list that read_lines inputs into parse - list of individual strings from a line of board
        Expected: Raised ValueError
    """
    line = ['*****\n', 'X****\n', '*****']
    try:
        assert parse(line)
    except ValueError as e:
        assert str(e) == "Expected 1 ending position, got 0.", "Parse test case 4 failed"


    """ Tests if parse raises ValueError when there is no pair of teleports in grid 
        line mimics the list that read_lines inputs into parse - list of individual strings from a line of board
        Expected: Raised ValueError
    """
    line = ['1******\n', 'X********\n', 'Y*****']
    try:
        assert parse(line)
    except ValueError as e:
        assert str(e) == "Teleport pad 1 does not have an exclusively matching pad.", "Parse test case 5 failed"
    
    """ Tests if parse FIRST raises ValueError for no 'X' in grid 
        line mimics the list that read_lines inputs into parse - list of individual strings from a line of board
        Expected: Raised ValueError, "Expected 1 starting position...."
    """
    line = ['*\n', '\n', '*']
    try:
        assert parse(line)
    except ValueError as e:
        assert str(e) == "Expected 1 starting position, got 0.", "Parse test case 6 failed"


    """ Tests if parse raises ValueError for unknown letters in list
        line mimics the list that read_lines inputs into parse - list of individual strings from a line of board
        Expected: Raised ValueError, "Bad letter in configuration file: #"
    """
    line = ['*\n', 'X\n', '#']
    try:
        assert parse(line)
    except ValueError as e:
        assert str(e) == "Bad letter in configuration file: #.", "Parse test case 7 failed"

    """ Tests if parse raises ValueError for unknown letters in list
        line mimics the list that read_lines inputs into parse - list of individual strings from a line of board
        Expected: Raised ValueError, "Bad letter in configuration file: 0"
    """
    line = ['*\n', 'X\n', '0']
    try:
        assert parse(line)
    except ValueError as e:
        assert str(e) == "Bad letter in configuration file: 0.", "parse test case 8 failed"


    """ DON'T NEED TO TEST FOR NON-LIST INPUT INTO PARSER BECAUSE READ_LINES WILL ALWAYS GIVE PARSE LIST
    """

        
def run_tests():
    test_parse()
    test_read_lines()


run_tests()