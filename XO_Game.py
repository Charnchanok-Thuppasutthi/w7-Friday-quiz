class Board :
    def __init__(self):
        self.board_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.printer = Printer()
        self.inputtext = Textinput()
    def start_game (self):
        for i in range(9):
            if i%2 == 0 :
                symb = 'X'    
            if i%2 == 1 : 
                symb = 'O'

            column = int(input("Enter column : "))
            row = int(input("Enter row :"))
            temp = [0,1,2]
            while ( column not in temp ) or (row not in temp) : 
                print(" Enter 0,1,2 PLEASE :) ")
                column = int(input("Enter column : "))
                row = int(input("Enter row : "))

            self.inputtext.input_symb(column,row,symb,self)
            self.printer.print_board(self)
            if i >4:
                if ( self.check_win() != None ) :
                    print(self.check_win())
                    print("\n")

                    self.reset_board() 
        print("DRAW")
        print("\n")
        self.reset_board()


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

    def getter_symbol (self,column, row) :
        return self.board_list[column][row]

    def setter_symbol (self,column, row, symbol) :
        self.board_list[column][row] = symbol

    def reset_board (self):
        result = str(input(" 1v1 Again?(Y / N ) :)"))
        if result in 'Yy' :
            self.board_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            self.start_game()
            
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
        if obj.board_list[indexColumn][indexRow] == ' ':
            obj.setter_symbol(indexColumn, indexRow, symbol)
        else :
            print ("Can't insert")


a_board = Board()
a_board.start_game()
