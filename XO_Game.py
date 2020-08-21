class Board :
    def __init__(self):
        self.board_list = [[None,None,None],[None,None,None],[None,None,None]]
        self.printer = Printer()
        self.inputtext = Textinput()
    def start_game (self):
        for i in range(9):
            if i%2 == 0 :
                symb = "O"
                column = int(input())
                row = int(input())
                self.inputtext.input_symb(column,row,symb,self)
                self.printer.print_board(self)
            if i%2 == 1 :
                symb = "X"
                column = int(input())
                row = int(input())
                self.inputtext.input_symb(column,row,symb,self)
                self.printer.print_board(self)


    def check_win (self) :
        if (self.board_list[0][0] == self.board_list[0][1] == self.board_list[0][2] and self.board_list[0][0] != None) :
            return (f"Player {self.board_list[0][0]} is win") 
        elif (self.board_list[1][0] == self.board_list[1][1] == self.board_list[1][2] and self.board_list[1][0] != None) :
            return (f"Player {self.board_list[1][0]} is win") 
        elif (self.board_list[2][0] == self.board_list[2][1] == self.board_list[2][2] and self.board_list[2][0] != None) :
            return (f"Player {self.board_list[2][0]} is win")
        elif (self.board_list[0][0] == self.board_list[1][1] == self.board_list[2][2] and self.board_list[0][0] != None) :
            return (f"Player {self.board_list[0][0]} is win")
        elif (self.board_list[0][2] == self.board_list[1][1] == self.board_list[2][0] and self.board_list[0][2] != None) :
            return (f"Player {self.board_list[0][2]} is win")
        elif (self.board_list[0][0] == self.board_list[1][0] == self.board_list[2][0] and self.board_list[0][0] != None) :
            return (f"Player {self.board_list[0][0]} is win")
        elif (self.board_list[0][1] == self.board_list[1][1] == self.board_list[2][2] and self.board_list[0][1] != None) :
            return (f"Player {self.board_list[0][1]} is win")
        elif (self.board_list[0][2] == self.board_list[1][2] == self.board_list[2][2] and self.board_list[0][2] != None) :
            return (f"Player {self.board_list[0][2]} is win")


    def getter_symbol (self,column, row) :
        return self.board_list[row][column]

    def setter_symbol (self,column, row, symbol) :
        self.board_list[row][column] = symbol

    def reset_board (self):
        self.board_list = [[None,None,None],[None,None,None],[None,None,None]]
    

class Printer :
        

    def print_board(self,obj):
        print(f"{obj.board_list[0][0]} | {obj.board_list[0][1]} | {obj.board_list[0][1]}")
        print(f"-----+------+------")
        print(f"{obj.board_list[0][0]} | {obj.board_list[0][1]} | {obj.board_list[0][1]}")
        print(f"-----+------+------")
        print(f"{obj.board_list[0][0]} | {obj.board_list[0][1]} | {obj.board_list[0][1]}")


class Textinput():

    def input_symb(self,indexColumn,indexRow,symbol,obj):
        if obj.board_list[indexColumn][indexRow] == None:
            obj.setter_symbol(indexColumn, indexRow, symbol)
            print("test")
        else:
            print ("Cant insert")


a = Board()
a.start_game()
