import os

class Game:
    def __init__(self, first_player = "X") -> None:
        self.__board = {
                '1': ' ' , '2': ' ' , '3': ' ',
                '4': ' ' , '5': ' ' , '6': ' ',
                '7': ' ' , '8': ' ' , '9': ' '
            }
        self.turno = first_player


    def __show_board(self) -> None:
        print("┌───┬───┬───┐")
        print(f"│ {self.__board['1']} │ {self.__board['2']} │ {self.__board['3']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.__board['4']} │ {self.__board['5']} │ {self.__board['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.__board['7']} │ {self.__board['8']} │ {self.__board['9']} │")
        print("└───┴───┴───┘")


    def __check_move(self, position) -> bool:
        if position in self.__board.keys() and self.__board[position] == ' ':
            return True
        else:
            return False


    def __check_board(self) -> str:
        # CHECK COLUMNS
        if self.__board['1'] == self.__board['4'] == self.__board['7'] != ' ':
            return self.__board['7']
        elif self.__board['2'] == self.__board['5'] == self.__board['8'] != ' ':
            return self.__board['8']
        elif self.__board['3'] == self.__board['6'] == self.__board['9'] != ' ':
            return self.__board['9']

        # CHECK ROWS
        elif self.__board['1'] == self.__board['2'] == self.__board['3'] != ' ':
            return self.__board['1']
        elif self.__board['4'] == self.__board['5'] == self.__board['6'] != ' ':
            return self.__board['8']
        elif self.__board['7'] == self.__board['8'] == self.__board['9'] != ' ':
          return self.__board['7']

        # CHECK DIAGONALS
        elif self.__board['1'] == self.__board['5'] == self.__board['9'] != ' ':
            return self.__board['1']
        elif self.__board['7'] == self.__board['5'] == self.__board['3'] != ' ':
          return self.__board['7']
        
        # CHECK DRAW
        if [*self.__board.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.__board.values()].count(' ')


    def play(self) -> None:
        while ' ' in list(self.__board.values()):
            os.system('clear') # cleaning terminal
            self.__show_board()

            print(f"Turno do {self.turno}, qual sua jogada?")

            while True: # wainting move
                move = input("Jogada: ")

                if self.__check_move(move):
                    break 
                else:
                    print(f"jogado do {self.turno} inválida, jogue novamente.")

            self.__board[move] = self.turno
            _state = self.__check_board()
            os.system('clear') # cleaning terminal

            if _state == "X":
                print("X é o vencedor!!!")
                break

            elif _state == "O":
                print("O é o vencedor!!!")
                break

            elif _state == "empate":
                print("EMPATE!!!")
                break

            # Next player
            self.turno = "X" if self.turno == "O" else "O"

        self.__show_board()