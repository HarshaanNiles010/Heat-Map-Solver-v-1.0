# This is the file where Monte Carlo Search will be implemented for the Heat Map Solver to work
# This should be general derivation of the monte carlo search for the tic-tac-toe model

import random

class MonteCarlo:
    def __init__(self,board,size,current_player):
        self.newBoard = board
        self.size = size
        self.current_player = current_player

    def get_legal_moves(self):
        temp = []
        for i in range(self.size):
            if self.newBoard[i] == "":
                temp.append(i)
        return temp

    def Selection(self):
        temp = self.get_legal_moves()
        return random.choice(temp)

    def play_move(self):
        self.newBoard[self.Selection()] = self.current_player

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"

    def Expansion(self):
        moves = self.get_legal_moves()
        while(len(moves) != 0):
            self.play_move()
            self.change_player()
        pass

    def Simulation(self):
        pass

    def backTracking(self):
        if len(self.get_legal_moves()) >= 2:
            return len(self.get_legal_moves())


class ttt:
    def __init__(self):
        self.board = [""] * 9
        self.win = False
        self.moves = 9
        self.current_player = "O"
        self.size = 9

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def initialize(self):
        self.board = [""] * 9
        self.moves = 9

    def get_Board(self):
        return self.board

    def get_moves(self):
        temp = []
        for i in range(self.size):
            if self.board[i] == "":
                temp.append(i)
        return temp


    def decrease_move(self):
        self.moves = self.moves - 1

    def check_move(self, position):
        if self.board[position] != "":
            return False
        else:
            return True

    def play_move(self, position):
        if self.check_move(position):
            self.board[position] = self.current_player
            self.change_player()
            self.decrease_move()

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"

    def get_current_player(self):
        return self.current_player

    def check_row_win(self):
        if self.board[0] == self.board[1] == self.board[2] != "":
            return True
        elif self.board[3] == self.board[4] == self.board[5] != "":
            return True
        elif self.board[6] == self.board[7] == self.board[8] != "":
            return True
        else:
            return False

    def check_col_win(self):
        if self.board[0] == self.board[3] == self.board[6] != "":
            return True
        elif self.board[1] == self.board[4] == self.board[7] != "":
            return True
        elif self.board[2] == self.board[5] == self.board[8] != "":
            return True
        else:
            return False

    def check_dia_win(self):
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        elif self.board[0] == self.board[4] == self.board[8] != "":
            return True
        else:
            return False

    def check_draw(self):
        if not self.check_row_win() or not self.check_col_win() or not self.check_dia_win():
            return True
        else:
            return False

if __name__ == '__main__':
    T0 = ttt()
    T0.print_board()
    isBool = False
    while not isBool:
        try:
            position = int(input("Enter a position between 1-9: "))
            if position > 9 or position < 0:
                raise Exception
            else:
                if T0.check_move(position):
                    T0.play_move(position)
                else:
                    print(f"current position {position} is already occupied please choose other position")
                T0.print_board()
                if T0.check_dia_win() or T0.check_row_win() or T0.check_col_win():
                    isBool = True
                    print(f"{T0.get_current_player()} is the winner")
                elif T0.check_draw():
                    isBool = True
                    print("It's a draw")


        except Exception:
            print("Please enter a digit between 1-9")
