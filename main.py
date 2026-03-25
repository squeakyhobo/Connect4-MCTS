from src.game import Connect4

def main():
    board = Connect4()
    running = True
    print(board)

    while(running):
        board.make_move()


main()
