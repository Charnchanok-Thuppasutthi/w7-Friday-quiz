class Board :

    def __init__(self):
        self.board_list = [['1','2','3'],['4','5','6'],['7','8','9']]
        self.turn = 0 

    def start_game (self):
        self.printer = Printer()
        self.inputtext = Textinput()
        while self.turn < 9 :
            if self.turn%2 == 0 :
                symbol = 'X'    
            if self.turn%2 == 1 : 
                symbol = 'O'

            print(f"Player {symbol} please select to place !!\n")
            number = int(input("add number !!!"))
            # row = int(input("Enter row :"))
            # column = int(input("Enter column : "))
            row = (number-1)//3
            column = (number-1)%3
            print(row,column)
            self.inputtext.input_symb(row,column,symbol,self)
            self.printer.print_board(self)
            if self.turn >= 4:
                if ( self.check_win() != None ) :
                    print(self.check_win())
                    print("\n")

                    self.reset_board() 
                elif (self.turn == 8 and self.check_win == None):
                    print("DRAW\n")
                    self.reset_board() 
            self.turn += 1 


    def check_win (self) :
        if (self.board_list[0][0] == self.board_list[0][1] == self.board_list[0][2] and self.board_list[0][0] != ' ') :
            return (f"Player {self.board_list[0][0]} is win") 
        elif (self.board_list[1][0] == self.board_list[1][1] == self.board_list[1][2] and self.board_list[1][0] != ' ') :
            return (f"Player {self.board_list[1][0]} is win") 
        elif (self.board_list[2][0] == self.board_list[2][1] == self.board_list[2][2] and self.board_list[2][0] != ' ') :
            return (f"Player {self.board_list[2][0]} is win")
        elif (self.board_list[0][0] == self.board_list[1][1] == self.board_list[2][2] and self.board_list[0][0] != ' ') :
            return (f"Player {self.board_list[0][0]} is win")
        elif (self.board_list[0][2] == self.board_list[1][1] == self.board_list[2][0] and self.board_list[0][2] != ' ') :
            return (f"Player {self.board_list[0][2]} is win")
        elif (self.board_list[0][0] == self.board_list[1][0] == self.board_list[2][0] and self.board_list[0][0] != ' ') :
            return (f"Player {self.board_list[0][0]} is win")
        elif (self.board_list[0][1] == self.board_list[1][1] == self.board_list[2][1] and self.board_list[0][1] != ' ') :
            return (f"Player {self.board_list[0][1]} is win")
        elif (self.board_list[0][2] == self.board_list[1][2] == self.board_list[2][2] and self.board_list[0][2] != ' ') :
            return (f"Player {self.board_list[0][2]} is win")
        else:
            return None

    def getter_symbol (self, row, column) :
        return self.board_list[row][column]

    def setter_symbol (self, row, column, symbol) :
        self.board_list[row][column] = symbol

    def reset_board (self):
        result = str(input(" 1v1 Again?(Y / N ) :)"))
        if result in 'Yy' :
            self.board_list = [['1','2','3'],['4','5','6'],['7','8','9']]
            self.turn = 0
            self.start_game()
        else :
            exit() 


class Printer :
    def print_board(self,object_board):
        print("\n")
        print(f"{object_board.getter_symbol(2,0)} | {object_board.getter_symbol(2,1)} | {object_board.getter_symbol(2,2)}")
        print(f"--+---+--")
        print(f"{object_board.getter_symbol(1,0)} | {object_board.getter_symbol(1,1)} | {object_board.getter_symbol(1,2)}")
        print(f"--+---+--")
        print(f"{object_board.getter_symbol(0,0)} | {object_board.getter_symbol(0,1)} | {object_board.getter_symbol(0,2)}")
        print("\n")


class Textinput():

    def input_symb(self,indexRow,indexColumn,symbol,object_board):
        temp = [0,1,2]
        not_temp = ['1','2','3','4','5','6','7','8','9']
        if indexColumn not in temp or indexRow not in temp or object_board.board_list[indexRow][indexColumn] not in not_temp :
            object_board.turn -= 1 
            print ("Can't insert please input again !!!")
        elif object_board.board_list[indexRow][indexColumn] in not_temp:
            object_board.setter_symbol(indexRow, indexColumn,  symbol)
          


        


a_board = Board()
a_board.start_game()