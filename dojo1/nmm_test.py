#!/usr/bin/python

import unittest
import nmm

class NineMensMorrisTest(unittest.TestCase):

    def testRepresentation(self):
        # (Possibly not a legal position)
        Board = nmm.Board("1", "0", ["a7","d7"], ["a1","b2","c3"], "B")
        self.assertEquals(Board.getPosition(), "1,0 a7,d7 a1,b2,c3 B")

        Board = nmm.Board("0", "0", ["a7","d7","g4"], ["a1","b2","c3"], "W")
        self.assertEquals(Board.getPosition(), "0,0 a7,d7,g4 a1,b2,c3 W")
        self.assertEquals(Board.getBoard(),
"""\
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
""")

    def testMoveChecking(self):
        Board = nmm.Board("0", "0", ['a7','d7','g4'],
                            ['a1','b2','c3'], "W")

        self.assertTrue(Board.move(src="a7", tgt="a4"))
        # Can't place new men
        self.assertFalse(Board.move(tgt="a4"))
        # Can't move from vacant square
        self.assertFalse(Board.move(src="a4", tgt="b4"))
        # Can't move into occupied square
        self.assertFalse(Board.move(src="a7", tgt="d7"))
        # Captured man must be there
        self.assertFalse(Board.move(src="g4", tgt="g7", cap="a4"))
        # Not black's move
        self.assertFalse(Board.move(src="a1", tgt="a4"))

        # Can't choose to capture man in mill when there
        # is an alternative
        Board = nmm.Board("0", "0", "a7,d7,g4", "a1,b2,d1,g1", "W")
        self.assertFalse(Board.move(src="g4", tgt="g7", cap="a1"))


    def testParseBoard(self):
        b_str = "0,0 a7,d7,g4 a1,b2,c3 W"
        b = nmm.Board.parse(b_str)
        self.assertTrue(b.getPosition(), b_str)

    


if __name__ == '__main__':
    unittest.main()
