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
all_position = [(i, j) for i in range(0, boardSize) for j in range(0, boardSize)]

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

    def merge(self, col, direction):

        if direction == 'up' or direction == 'left':
            filtered_col = [i for i in col if i != 0]
        else:
            filtered_col = [i for i in col if i != 0][::-1]

        for i in range(0, len(filtered_col)):
            if i < len(filtered_col) - 1:
                if filtered_col[i] == filtered_col[i + 1]:
                    filtered_col[i] = filtered_col[i] + filtered_col[i + 1]
                    filtered_col[i + 1] = 0

        filtered_col = [i for i in filtered_col if i != 0]

        while len(filtered_col) != 4:
            filtered_col.append(0)

        if direction == 'up' or direction == 'left':
            return filtered_col
        else:
            return filtered_col[::-1]

    def create_random_number(self):
        # create a random number
        # check already occupied ndarray position
        occupied_array = list(zip(*np.nonzero(self.board)))
        array_to_place = [array for array in all_position if array not in occupied_array]
        i, j = random.choice(array_to_place)
        self.board[i][j] = random.choice(initial_set)

    def up_move(self):
        temp_board = self.board.copy()

        for j in range(0, boardSize):
            temp_col = [self.board[i][j] for i in range(0, boardSize)]
            col = self.merge(temp_col, 'up')
            if col != temp_col:
                for i in range(0, boardSize):
                    self.board[i][j] = col[i]

        if not (temp_board == self.board).all():
            self.create_random_number()


    def down_move(self):
        temp_board = self.board.copy()
        for j in range(0, boardSize):
            temp_col = [self.board[i][j] for i in range(0, boardSize)]
            col = self.merge(temp_col, 'down')
            if col != temp_col:
                for i in range(0, boardSize):
                    self.board[i][j] = col[i]

        if not (temp_board == self.board).all():
            self.create_random_number()
        pass

    def left_move(self):
        temp_board = self.board.copy()
        for i in range(0, boardSize):
            temp_col = [self.board[i][j] for j in range(0, boardSize)]
            col = self.merge(temp_col, 'left')
            if col != temp_col:
                for j in range(0, boardSize):
                    self.board[i][j] = col[j]

        if not (temp_board == self.board).all():
            self.create_random_number()
        pass

    def right_move(self):
        temp_board = self.board.copy()
        for i in range(0, boardSize):
            temp_col = [self.board[i][j] for j in range(0, boardSize)]
            col = self.merge(temp_col, 'right')
            if col != temp_col:
                for j in range(0, boardSize):
                    self.board[i][j] = col[j]

        if not (temp_board == self.board).all():
            self.create_random_number()
        pass

    def handle_keypress(self, input):
        if input == 'w':
            self.up_move()
        elif input == 'a':
            self.left_move()
        elif input == 's':
            self.down_move()
        elif input == 'd':
            self.right_move()
        else:
            print("you can only do w/a/s/d")
            return


    def handle_losegame(self):
        print('sorry you lose the game, please try again')
        print('the highest score is {}'.format(np.max(self.board)))


    def number_moveable(self) -> bool:
        if np.count_nonzero(self.board) == boardSize * boardSize:
            counter = 0
            for i in range(0, boardSize):
                temp_row = self.board[i, :]
                temp_col = self.board[:, i]

                if 0 not in np.diff(temp_row) and 0 not in np.diff(temp_col):
                    counter+=1
            if counter == boardSize:
                return False
            else:
                return True


    def lose_game(self) -> bool:

        pass

    def start_game(self):
        self.init_gameboard()
        self.print_board()
        while True:
            input_key = input()
            self.handle_keypress(input_key)
            self.print_board()
            if not self.number_moveable() and self.number_moveable() != None:
                self.handle_losegame()
                break

        pass


if __name__ == '__main__':
    game_2048 = Game()
    game_2048.start_game()

    pass
