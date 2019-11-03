
"""This includes some business logic for a chess board program.

Moves are here represented in the UCI move format. For example like:
"e2e4", "e7e5", "e1g1" (white short castling), "e7e8q" (for promotion),
"c5b6" (en passant).

Positions on the chess board are represented as for example "a1", "b5".

Pieces are represented as:

"P": white pawn   -  "p": black pawn
"N": white knight -  "n": black knight
"B": white biship -  "b": black bishop
"R": white rook   -  "r": black rook
"Q": white queen  -  "q": black queen
"K": white king   -  "k": black king
"""

import engine

class Game:

    def __init__(self, FEN_string):
        pass

    def __str__(self):
        """Make it possible to use the print command on objects of this class.
        It prints out a chessboard with the current position.
        """

    def board_value(square):
        """Return "k", "K", "p" etc f there is a piece on the square,
        and None if there is no piece. Square can be "a1", "b5" etc.
        """

    def legal(self, UCI_format_move):
        """Return true iff the move is legal"""
        return

    def make_move(self, UCI_format_move):
        pass

    def check(self):
        pass

    def check_mate(self):
        pass

    def stale_mate():
        pass

    def insufficient_material(self):
        """Return true if and only if the position is king vs king or
        king vs king and light piece."""
        pass

    def draw_by_repetition(self):
        pass

    def draw_by_50_move_rule(self):
        pass


def make_move(FEN_string, UCI_format_move):
    """Return a FEN string for the game state that result after making
    the given move to the given position."""



