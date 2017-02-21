from GameBoard import GameBoard
from Square import Square


class printColors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def play_game():

    print('Welcome to my game!\nWhen it is your turn, please enter the square you\'d like to occupy with no spaces, '
          'indexes are from the top left corner')
    gameboard = GameBoard()
    while not gameboard.game_over:
        gameboard.print_board()
        if gameboard.player_turn == 1:
            print('❌ , it is your turn')
        else:
            print('⭕️ , it is your turn')
        player_move = input('Enter your move: ')
        # Try to make a square from the input, if not continue
        try:
            selected_square = Square.from_input(player_move)
        except ValueError as e:
            print(printColors.FAIL + '\n{}\n'.format(str(e)) + printColors.ENDC)
            continue

        # Try to place the piece; if not valid move, error will return up call stack
        try:
            gameboard.place_piece(selected_square)
        except ValueError as e:
            print(printColors.FAIL + '\n{}\n'.format(e) + printColors.ENDC)
            continue
        # Before we do another iteration, let us see if we can still place another piece
        gameboard.check_stalemate()

    gameboard.print_board()
    if gameboard.game_winner == 1:
        print("The winner is ❌ !!!")
    elif gameboard.game_winner == 2:
        print("The winner is ⭕️  !!!")
    else:
        print("Its a draw!")

if __name__ == '__main__':
    play_game()