import random
import numpy as np


user = ""
end_num = 64
messageDisplayed = False
boardSize = 4 # 4 x 4 board
gameBoard = [[0 for x in range(boardSize)] for x in range(boardSize)]
endMessage = ""


class Game:

    def __init__(self, state, difficulty, score=0):
        self.state = state
        self.difficulty = difficulty
        self.score = score
        self.board = np.zeros((4, 4))

    def print_board(self):
        board_format = ' ' + str(self.board[0][0]) + ' | ' + str(self.board[0][1]) + ' | ' + \
                       str(self.board[0][2]) + ' | ' + str(self.board[0][3] + '\n')
        for i in range(0, boardSize):
            print(board_format)

    def init_gameboard(self):
        for _ in range(2):
            i_1, j_1 = (random.randint(0, 3), random.randint(0, 3))
            self.board[i_1][j_1] = random.randint(2, 4)


