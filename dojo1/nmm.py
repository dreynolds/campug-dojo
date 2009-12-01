class Board:
    def __init__(self, position=None):
        pass

    # Checks the legality of a move, and
    # updates the position if it is legal
    def move(self, tgt, src=None, cap=None):
        return False

    # Returns notation for the current game position
    def getPosition(self):
        return "0,0 a7,d7,g4 a1,b2,c3 W"

    # Returns a string representation of the board
    def getBoard(self):
        return """\
W-----------W-----------+
|           |           | 
|   +-------+-------+   |
|   |       |       |   |
|   |   +---+---+   |   |
|   |   |       |   |   |
+---+---+       +---+---W
|   |   |       |   |   |
|   |   B---+---+   |   |
|   |       |       |   |
|   B-------+-------+   |
|           |           |
B-----------+-----------+
"""

import re
def parse(boardstr):
    m = re.match(r'(\d),(\d) (\S*) (\S*) (\S)\Z', boardstr)
    w, b, wposns, bposns, turn = m.groups()
    w, b = int(w), int(b)
    Board()
