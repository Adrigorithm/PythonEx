# cases = []
# counter = 0

# while counter < 8:
#     cases_row = []
#     cases.append(cases_row)
#     counter += 1
#
# print (bcolors.FAIL, cases)


class Bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Board:
    squares = []

    def board_setup(self):
        counter = 0
        while counter < 8:
            row = []
            row_special = (4, 2, 3, 5, 6, 3, 2, 4)
            for count in range(0, 8):
                piece_new = None
                if counter == 0 or counter == 7:
                    if counter == 0:
                        piece_new = Piece(0, row_special[count])
                    else:
                        piece_new = Piece(1, row_special[count])
                elif counter == 1 or counter == 6:
                    if counter == 1:
                        piece_new = Piece(0, 1)
                    else:
                        piece_new = Piece(1, 1)
                square_new = Square(piece_new)
                row.append(square_new)
            self.squares.append(row)
            counter += 1

    def board_print(self):
        board_display = []
        for square_list in self.squares:
            for square in square_list:
                if square.get_piece() is None:
                    board_display.append(-1)
                else:
                    board_display.append(square.get_piece().get_piece_type())
        return board_display


class Square:
    piece = None

    def __init__(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def piece_kill(self):
        self.piece = None

class Piece:
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

    def get_piece_type(self):
        return self.piece_type


class Player:
    color = -1
    pawn = -1
    knight = -1
    bishop = -1
    rook = -1
    queen = -1
    king = -1

    playerdata = []

    def __init__(self, color):
        self.color = color
        self.pawn = 8
        self.knight = 2
        self.bishop = 2
        self.rook = 2
        self.queen = 1
        self.king = 1

    def get_player_data(self):
        playerdata = [self.color, self.pawn, self.knight, self.bishop, self.rook, self.queen, self.king]
        return playerdata


# Main

while True:
    ai = input("Against an AI opponent? (y or n): ")
    if ai.lower() == "y" or ai.lower() == "yes":
        player_colour = input("Black or White: ")
        if player_colour.lower() == "b" or player_colour.lower() == "black":
            player = Player(0)
            player_ai = Player(1)
        elif player_colour.lower() == "w" or player_colour.lower() == "white":
            player = Player(1)
            player_ai = Player(0)
    elif ai.lower() == "n" or ai.lower() == "no":
        player1 = Player(1)
        player2 = Player(0)

board = Board()
board.board_setup()

counter = 0
while counter < 64:
    if counter % 8 == 0:
        print()
    print(board.board_print()[counter], end="\t")
    counter += 1


