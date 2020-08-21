class Board :
    def __init__(self):
        self.board_list = [[None,None,None],[None,None,None],[None,None,None]]
        self.turn = 9
        #self.textinput = Textinput()
    #def start_game (self):
        



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
    def __init__(self):
        self.board = Board()

    def print_board(self):
        print(f"{self.board.board_list[0][0]} | {self.board.board_list[0][1]} | {self.board.board_list[0][1]}")
        print(f"-----+------+------")
        print(f"{self.board.board_list[0][0]} | {self.board.board_list[0][1]} | {self.board.board_list[0][1]}")
        print(f"-----+------+------")
        print(f"{self.board.board_list[0][0]} | {self.board.board_list[0][1]} | {self.board.board_list[0][1]}")


class Textinput():
    def __init__(self):
         self.board = Board()
    def input_symb(self,indexColumn,indexRow,symbol):
        if self.board.board_list[indexColumn][indexRow] == None:
            self.board.setter_symbol (indexColumn, indexRow, symbol)
        else:
            print ("Cant insert")


a = Board()
a.setter_symbol(0,0,"x")
a.setter_symbol(0,2,"x")
a.setter_symbol(0,1,"x")
p = Printer()
p.print_board()
print(a.check_win())
