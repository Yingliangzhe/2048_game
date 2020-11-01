import logging
import random
import numpy as np
import keyboard

user = ""
end_num = 64
messageDisplayed = False
boardSize = 4  # 4 x 4 board
endMessage = ""
initial_set = [2, 4]


class Game:

    def __init__(self, score=0):
        self.score = score
        self.board = np.zeros((boardSize, boardSize), dtype=int)

    def print_board(self):
        for i in range(0, boardSize):
            board_format = ' ' + str(self.board[i][0]) + ' | ' + str(self.board[i][1]) + ' | ' + \
                   str(self.board[i][2]) + ' | ' + str(self.board[i][3]) + '\n'
            print(board_format)

    def init_gameboard(self):

        i_1, j_1 = (random.randint(0, 3), random.randint(0, 3))
        self.board[i_1][j_1] = random.choice(initial_set)
        i_2, j_2 = (random.randint(0, 3), random.randint(0, 3))

        while i_2 == i_1 and j_2 == j_1:
            i_2, j_2 = (random.randint(0, 3), random.randint(0, 3))
            if i_2 != i_1 and j_2 != j_1:
                break

        self.board[i_2][j_2] = random.choice(initial_set)

    def up_move(self):
        pass

    def down_move(self):
        pass

    def left_move(self):
        pass

    def right_move(self):
        pass

    def handle_keypress(self):


    def number_moveable(self) -> bool:

        # there are two situations, we can
        if np.count_nonzero(self.board) == boardSize * boardSize:

            for i in range(0, boardSize):
                for j in range(0, boardSize):
                    if i == 0:
                        if j == 0:
                            if self.board[i][j] != self.board[i][j + 1] and self.board[i][j] != self.board[i + 1][j]:
                                logging.debug('game board ist not moveable, you lose the game')
                                return False
                        elif j == boardSize - 1:
                            if self.board[i][j] != self.board[i][j - 1] and self.board[i][j] != self.board[i + 1][j]:
                                logging.debug('game board ist not moveable, you lose the game')
                                return False
                        elif self.board[i][j] != self.board[i][j - 1] and self.board[i][j] != self.board[i][j + 1] and \
                                self.board[i][j] != self.board[i + 1][j]:
                            logging.debug('game board ist not moveable, you lose the game')
                            return False
                    elif i == boardSize -1 :
                        if j == 0:
                            if self.board[i][j] != self.board[i - 1][j] and self.board[i][j] != self.board[i][j + 1]:
                                logging.debug('game board ist not moveable, you lose the game')
                                return False

                        elif j == boardSize - 1:
                            if self.board[i][j] != self.board[i][j - 1] and self.board[i][j] != self.board[i - 1][j]:
                                logging.debug('game board ist not moveable, you lose the game')
                                return False

                        elif self.board[i][j] != self.board[i][j - 1] and self.board[i][j] != self.board[i - 1][j] and \
                                self.board[i][j] != self.board[i][j + 1]:
                            logging.debug('game board ist not moveable, you lose the game')
                            return False

                    elif j == 0:
                        if self.board[i][j] != self.board[i - 1][j] and self.board[i][j] != self.board[j][j + 1] and \
                                self.board[i][j] != self.board[i + 1][j]:
                            logging.debug('game board ist not moveable, you lose the game')
                            return False

                    elif j == boardSize - 1:
                        if self.board[i][j] != self.board[i-1][j] and self.board[i][j] != self.board[j][j - 1] and \
                                self.board[i][j] != self.board[i + 1][j]:
                            logging.debug('game board ist not moveable, you lose the game')
                            return False

                    else:
                        return True

        else:
            return True

    def lose_game(self) -> bool:

        pass

    def start_game(self):
        self.init_gameboard()
        self.print_board()

        pass


if __name__ == '__main__':
    game_2048 = Game()
    game_2048.start_game()

    pass
