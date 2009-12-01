class Board:
    def __init__(self, w, b, wposns, bposns, turn):
        self.w = w
        self.b = b
        self.w_posns = wposns
        self.b_posns = bposns
        self.next_turn = turn

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
|           |           |w, b, wposns, bposns, turn
B-----------+-----------+
"""

import re
def parse(boardstr):
    m = re.match(r'(\d),(\d) (\S+) (\S+) ([WB])\Z', boardstr)
    w, b, wposns, bposns, turn = m.groups()
    w, b = int(w), int(b)
    wposns = wposns.split(',')
    bposns = bposns.split(',')
    return Board(w, b, wposns, bposns, turn)

