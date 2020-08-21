class Board :
    def __init__(self):
        self.board_list = [[None,None,None],[None,None,None],[None,None,None]]
        
    # def start_game (self):

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
    

a = Board()
a.setter_symbol(0,1,"X")
a.setter_symbol(0,2,"X")
a.setter_symbol(0,0,"X")
print(a.check_win())


