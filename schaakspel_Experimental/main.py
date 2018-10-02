from Class import classes

game_over = False

board = classes.board()
board.board_setup()

while game_over == False:
    print(board.board_display())
    coords = input()
    coord1 = coords[:2]
    coord2 = coords[-2:]
    board.piece_getCoords(coord1, coord2)
    print()

