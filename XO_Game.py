class Board :

    def __init__(self):
        self.board_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
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
            row = int(input("Enter row :"))
            column = int(input("Enter column : "))

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
            self.board_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            self.start_game()
        else :
            exit() 
            
class Printer :
    def print_board(self,obj):
        print("\n")
        print(f"{obj.getter_symbol(0,0)} | {obj.getter_symbol(0,1)} | {obj.getter_symbol(0,2)}")
        print(f"--+---+--")
        print(f"{obj.getter_symbol(1,0)} | {obj.getter_symbol(1,1)} | {obj.getter_symbol(1,2)}")
        print(f"--+---+--")
        print(f"{obj.getter_symbol(2,0)} | {obj.getter_symbol(2,1)} | {obj.getter_symbol(2,2)}")
        print("\n")

class Textinput():

    def input_symb(self,indexColumn,indexRow,symbol,obj):
        temp = [0,1,2]
        if indexColumn not in temp or indexRow not in temp:
            obj.turn -= 1 
            print ("Can't insert please input again !!!")
        elif obj.board_list[indexRow][indexColumn] == ' ':
            obj.setter_symbol(indexColumn, indexRow, symbol)
          


            


a_board = Board()
a_board.start_game()
