class Board :
    def __init__(self):
        self.board_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.printer = Printer()
        self.inputtext = Textinput()
    def start_game (self):
        run_loop = True 
        round = 0 
        #for i in range(9):   #start at i = 01
        if round%2 == 0 :
            symb = 'X'
        if round%2 == 1 :
            symb = 'o'
            #print(symb)
        while run_loop:
            column = int(input("input column : "))
                #print(str(column))
            if str(column) not in "012" :
                pass
            else :
                row = int(input("input row : "))
                if str(row) not in '012':
                    pass
                else :
                    self.inputtext.input_symb(column,row,symb,self)
                    self.printer.print_board(self)
                    run_loop = False
                    round +=1
                
                


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
        elif (self.board_list[0][1] == self.board_list[1][1] == self.board_list[2][2] and self.board_list[0][1] != ' ') :
            return (f"Player {self.board_list[0][1]} is win")
        elif (self.board_list[0][2] == self.board_list[1][2] == self.board_list[2][2] and self.board_list[0][2] != ' ') :
            return (f"Player {self.board_list[0][2]} is win")

    def getter_symbol (self,column, row) :
        return self.board_list[column][row]

    def setter_symbol (self,column, row, symbol) :
        self.board_list[column][row] = symbol

    def reset_board (self):
        self.board_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    

class Printer :
    def print_board(self,obj):
        print(f"{obj.board_list[0][0]} | {obj.board_list[0][1]} | {obj.board_list[0][1]}")
        print(f"--+---+--")
        print(f"{obj.board_list[1][0]} | {obj.board_list[1][1]} | {obj.board_list[1][2]}")
        print(f"--+---+--")
        print(f"{obj.board_list[2][0]} | {obj.board_list[2][1]} | {obj.board_list[2][2]}")


class Textinput():

    def input_symb(self,indexColumn,indexRow,symbol,obj):
        if obj.board_list[indexColumn][indexRow] == ' ':
            obj.setter_symbol(indexColumn, indexRow, symbol)
        else:
            print ("Cant insert")


a = Board()
a.start_game()
