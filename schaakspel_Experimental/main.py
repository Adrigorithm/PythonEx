from Class import classes

game_over = False

board = classes.board()
board.board_setup()
playerdata = []

color = input("Wil je wit(w) of zwart(z) zijn: ")
if color == "z":
    player = classes.player(0)
else:
    player = classes.player(1)

while game_over == False:
    print(board.board_display())
    coords = input()
    if coords == "score":
        playerdata = player.data_player()
        print()
        print(" --- Statistics --- ")
        print("Color:", playerdata[0])
        print()
        print("Pawn:", playerdata[1])
        print("Knight:", playerdata[2])
        print("Bishop:", playerdata[3])
        print("Rook:", playerdata[4])
        print("Queen:", playerdata[5])
        print("King:", playerdata[6])
    else:
        coord1 = coords[:2]
        coord2 = coords[-2:]
        board.piece_getCoords(coord1, coord2)
    print()

