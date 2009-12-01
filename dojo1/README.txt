Code Dojo Challange #1
======================

The basic idea is to write a program for playing Nine Men's Morris, a two
player game the rules of which I shall now describe.


Rules
-----

(There are variations in the rules which I will ignore for now, but could
be addressed once the basic challange has been completed.)

The two players are termed White and Black, and each start off with 9 pegs
("men") of their colour in hand. They take it in turns to place their men on
the board, and then to move them around, each player trying to capture the
opponent's men. If one player is reduced to 2 men, or cannot make a legal
move, then this player loses.

The board is square, and has 24 holes ("squares") which a man might occupy.
Some squares are considered to be adjacent, indicated by a line between them
on the board. We can label the squares, and represent the board as so:


a7----------d7----------g7
|           |           | 
|   b6------d6------f6  |
|   |       |       |   |
|   |   c5--d5--e5  |   |
|   |   |       |   |   |
a4--b4--c4      e4--f4--g4
|   |   |       |   |   |
|   |   c3--d3--e3  |   |
|   |       |       |   |
|   b2------d2------f2  |
|           |           |
a1----------d1----------g1

Play is divided into two phases: placing men and moving them. If a player has
men in hand then that player's turn consists of placing one in a vacant
square. Otherwise, the player moves one of their men from its square to
an adjacent vacant square.

If three of a player's men are in a line - in adjacent squares - then this
is called a "mill". When a player forms a mill they capture one of the other
player's men: it is removed from its square on the board and takes no further
part in the game. A man that is part of a mill cannot be captured, unless all
of that player's men are in mills.

(If a player manages to form two mills at once they still only get to capture
one man.)

There is a notation for representing the position at any point in game,
consisting of 4 space-separated fields to indicate the numbers of men
each player has in hand, the squares occupied by white, the squares occupied
by black, and the player who is next to move. Examples:
- new game: "9,9 - - W"
- during the first phase: "7,8 a4,b4 g7 B"
- second phase, white about to win: "0,0 a7,d7,g4 a1,b2,c3 W"


Basic aim
---------

First aim is to write something that can adjudicate games between players:
keeping track of the position, checking whether moves are legal, noticing when
a game is over.

We also want something that can play one side in a game. This could be done by
something as simple as picking an arbitrary legal move, or it could be much
more sophisticated. We want the option of having both sides in a game played
by the computer, and if we had multiple computer player implementations we'd
like to be able to pit them against each other.


Extras
------

It might be possible to use the system described above by directly interacting
with the implementation from a python shell. However, it would be much better
if a proper user interface could be implemented. A text-based interfaced might
be simplest, although ideally we would want to be able to add a graphic
interface, or even a web-based one, without if affecting the core of the
program.

Another possibility is to find some sensible way of dealing with variations in
the rules, which are described next.


Variations
----------

There are a number of optional rules in Nine Men's Morris, and there are also
other games that are closely related.

One optional rule is to say that a man in a mill can never be captured (rather
than saying that it can only be captured if there aren't any men on that side
not in mills). Another is to say that if one player has only three men then
these men can "fly": they are not constrained to move to adjacent squares.

One closely related game is Morabaraba, which is played in South Africa. It
differs from the rules I gave for Nine Men's Morris in the following ways:
- the pieces are called "cows" not "men", and they are "shot" rather than
  "captured"
- each player gets 12 cows, not 9
- there are additional diagonal lines on the board, so that a1-b2-c3,
  g1-f2-e3, a7-b6-c5 and g7-f6-e5 are all potential locations for mills.
- a player reduced to 3 cows can fly them, as described above
- if a player is reduced to 3 cows and neither player shoots a cow within 10
  moves then the game is drawn
- (optional) if a player moves a cow from one mill to form another, they
  cannot move it back again without making some other move first


vim: tw=78
