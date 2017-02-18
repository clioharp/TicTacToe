import numpy
from Square import Square


class GameBoard:
    w, h = 3, 3
    board = numpy.zeros((w, h))
    pieces_placed = 0
    game_over = False
    game_winner = 0
    player_turn = True
    player_1_winning_set = [
        # horizontal winning sets
        [Square(0, 0), Square(1, 0), Square(2, 0)],
        [Square(0, 1), Square(1, 1), Square(2, 1)],
        [Square(0, 2), Square(1, 2), Square(2, 2)],
        # vertical winning sets
        [Square(0, 0), Square(0, 1), Square(0, 2)],
        [Square(1, 0), Square(1, 1), Square(1, 2)],
        [Square(2, 0), Square(2, 1), Square(2, 2)],
        # diagonal winning sets
        [Square(0, 0), Square(1, 1), Square(2, 2)],
        [Square(2, 0), Square(1, 1), Square(0, 2)]
    ]
    player_2_winning_set = [
        # horizontal winning sets
        [Square(0, 0), Square(1, 0), Square(2, 0)],
        [Square(0, 1), Square(1, 1), Square(2, 1)],
        [Square(0, 2), Square(1, 2), Square(2, 2)],
        # vertical winning sets
        [Square(0, 0), Square(0, 1), Square(0, 2)],
        [Square(1, 0), Square(1, 1), Square(1, 2)],
        [Square(2, 0), Square(2, 1), Square(2, 2)],
        # diagonal winning sets
        [Square(0, 0), Square(1, 1), Square(2, 2)],
        [Square(2, 0), Square(1, 1), Square(0, 2)]
    ]

    def place_piece(self, square, player_number):
        self.check_valid_move(square)
        self.board[square.x][square.y] = player_number
        self.check_game_won(square)
        # Keep track of how many pieces have been placed so we can terminate if needed
        self.pieces_placed += 1

    def check_valid_move(self, square):
        if square.x > self.w-1 or square.y > self.h-1:
            raise(ValueError('The square you selected is not in the game space.'))
        if not self.board[square.x][square.y] == 0:
            raise(ValueError('The square is already occupied by another piece.'))

    def switch_player_turn(self):
        self.player_turn = not self.player_turn

    def print_board(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.board[x][y] == 0:
                    print_char = '[  ]'
                elif self.board[x][y] == 1:
                    print_char = '[❌ ]'
                else:
                    print_char = '[⭕️ ]'

                print(print_char, end=' ')
            print()
        print()

    def check_game_won(self, square):
        if not self.player_turn:
            relevant_list = self.player_1_winning_set
        else:
            relevant_list = self.player_2_winning_set

        for winning_list in relevant_list:
            matching_item = list(filter(lambda item: item.x == square.x and item.y == square.y, winning_list))
            if not len(matching_item) == 0:
                winning_list.remove(matching_item[0])
                if len(winning_list) == 0:
                    self.set_winner()
                    return

    def set_winner(self):
        self.game_over = True
        if not self.player_turn:
            self.game_winner = 1
        else:
            self.game_winner = 2

    def check_stalemate(self):
        if self.pieces_placed == self.w * self.h:
            self.game_over = True
