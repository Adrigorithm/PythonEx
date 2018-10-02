class board:
    squares = []
    coordinates = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                   "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                   "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                   "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                   "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                   "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                   "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                   "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
    def board_setup(self):
        square_amount = 64
        square_setup_black = [4, 2, 3, 5, 6, 3, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1]
        square_setup_white = [1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 3, 5, 6, 3, 2, 4]
        xy = 0
        xy_reverse = 0

        while xy < square_amount:
            if xy < 16:
                piece_new = piece(0, square_setup_black[xy])
                square_new = square(xy, piece_new, self.coordinates[xy])
                self.squares.append(square_new)
            elif xy > 47:
                piece_new = piece(1, square_setup_white[xy_reverse])
                square_new = square(xy, piece_new, self.coordinates[xy])
                self.squares.append(square_new)
                xy_reverse += 1
            else:
                piece_new = piece(-1, -1)
                square_new = square(xy, piece_new, self.coordinates[xy])
                self.squares.append(square_new)
            xy += 1

    def board_display(self):
        output = []
        counter = 0

        for square in self.squares:
            output.append(square.piece.piece_type)

        while counter < 64:
            if counter == 7 or counter == 15 or counter == 23 or counter == 31 or counter == 39 or counter == 47 or counter == 55:
                print(output[counter])
            else:
                print(output[counter], end=" ")
            counter += 1

        return "\n\n" + "To move a piece, write xx xx eg: moving a piece from a1 to a8 would be: a1a8"

    def piece_getCoords(self, coord1, coord2):
        piece_current = piece(-1, -1)
        piece_target = piece(-1, -1)

        for square in self.squares:
            if square.coordinate == coord1:
                piece_current = square.piece
            if square.coordinate == coord2:
                piece_target = square.piece
        self.piece_move(piece_current, piece_target, coord1, coord2)

    def piece_move(self, piece_current, piece_target, coord1, coord2):
        for square in self.squares:
            if square.coordinate == coord1:
                square.piece = piece_target
            elif square.coordinate == coord2:
                square.piece = piece_current

class square:
    xy = 0
    piece = 0
    coordinate = ""

    def __init__(self, xy, piece, coordinate):
        self.xy = xy
        self.piece = piece
        self.coordinate = coordinate

class piece:
    color = -1
    # Black = 0
    # White = 1
    piece_type = -1
    # Pawn = 1
    # Knight = 2
    # Bishop = 3
    # Rook = 4
    # Queen = 5
    # King = 6

    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

