import re

class Board:
    def __init__(self, w, b, wposns, bposns, turn):
        """A representation of a 9-man's morris board.

        Arguments are

        - 'w' and 'b' for how many pieces White and Black
          still have in hand
        - 'wposns' is a list of the positions of White's
          stones on the board
        - 'bposns' the same for Black
        - 'turn' is 'W' or 'B' according to whose turn is next.
        """
        self.w = int(w)
        self.b = int(b)
        
        if abs(self.w-self.b) > 1:
            raise Exception("bad w/b combination");

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
        
        data = {}


        return """\
%(a7)s-----------%(d7)s-----------%(g7)s
|           |           | 
|   %(b6)s-------%(d6)s-------%(f6)s   |
|   |       |       |   |
|   |   %(c5)s---%(d5)s---%(e5)   |   |
|   |   |       |   |   |
%(a4)s---%(b4)s---%(c4)s       %(e4)s---%(f4)s---%(g4)s
|   |   |       |   |   |
|   |   %(c3)s---%(d3)s---%(e3)s   |   |
|   |       |       |   |
|   %(b2)s-------%(d2)s-------%(f2)s   |
|           |           |
%(a1)s-----------%(d1)s-----------%(g1)s
"""%data

    @staticmethod
    def parse(boardstr):
        m = re.match(r'(\d),(\d) (\S+) (\S+) ([WB])\Z', boardstr)
        w, b, wposns, bposns, turn = m.groups()
        w, b = int(w), int(b)
        wposns = wposns.split(',')
        bposns = bposns.split(',')
        return Board(w, b, wposns, bposns, turn)

