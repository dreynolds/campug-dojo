import re

class Board:
    def_data = {}
    for j in '1234567':
        for x in 'abcdefg':
            def_data[x+j] = '+'
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

        self.data = self.def_data.copy()
        for p in self.w_posns:
            self.data[p] = 'W'
        for p in self.b_posns:
            self.data[p] = 'B'

    # Checks the legality of a move, and
    # updates the position if it is legal
    def move(self, tgt, src=None, cap=None):
        """ Move / place a piece. When moving, the piece is moved from src to tgt.
            When placing, only tgt is specified. Cap implies that the move will
            capture a piece.

            We return False if the move was a failure, True if it was allowed.
        """
        if src is None:
            # We're trying to put a new piece down
            return True
        else:
            # We're trying to move a piece
            # Check that the target is empty
            if self.data[tgt] != '+':
                return False
            # If we've got a source piece, we're moving a piece.
            # If we're moving a piece, it must be our own.
            if self.data[src] != self.next_turn:
                return False
            return True

    # Returns notation for the current game position
    def getPosition(self):
        if not(self.w_posns):
            w_repr = '-'
        else:
            w_repr = ','.join(self.w_posns)

        if not(self.b_posns):
            b_repr = '-'
        else:
            b_repr = ','.join(self.b_posns)
        return "%d,%d %s %s %s" % (self.w, self.b, w_repr, b_repr, self.next_turn)

    # Returns a string representation of the board
    def getBoard(self):
        

        return """\
%(a7)s-----------%(d7)s-----------%(g7)s
|           |           | 
|   %(b6)s-------%(d6)s-------%(f6)s   |
|   |       |       |   |
|   |   %(c5)s---%(d5)s---%(e5)s   |   |
|   |   |       |   |   |
%(a4)s---%(b4)s---%(c4)s       %(e4)s---%(f4)s---%(g4)s
|   |   |       |   |   |
|   |   %(c3)s---%(d3)s---%(e3)s   |   |
|   |       |       |   |
|   %(b2)s-------%(d2)s-------%(f2)s   |
|           |           |
%(a1)s-----------%(d1)s-----------%(g1)s
""" % self.data

    @staticmethod
    def parse(boardstr):
        m = re.match(r'(\d),(\d) (\S+) (\S+) ([WB])\Z', boardstr)
        w, b, wposns, bposns, turn = m.groups()
        w, b = int(w), int(b)
        wposns = wposns.split(',')
        bposns = bposns.split(',')
        return Board(w, b, wposns, bposns, turn)

