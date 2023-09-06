class Board:

    def __init__(self, game):
        self.game = game
        
    def scoreboard_repr(self, scoreboard):
        for row in range(3):
            for col in range(3):
                print(scoreboard[row][col], end="")
                if col < 2:
                    print(" | ", end="")
            print()
            if row < 2:
                print("-" * 9)

    def print_board(self):
        player1_moves = self.game.player1_moves
        player2_moves = self.game.player2_moves

        mapping = {
            1 : [0, 0],
            2 : [0, 1],
            3 : [0, 2],
            4 : [1, 0],
            5 : [1, 1],
            6 : [1, 2],
            7 : [2, 0],
            8 : [2, 1],
            9 : [2, 2]
        }

        player1_x = [mapping[i] for i in player1_moves]
        player2_o = [mapping[i] for i in player2_moves]

        scoreboard = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        #If game begin
        if (len(player1_moves) + len(player2_moves) == 0):
            return self.scoreboard_repr(scoreboard)
        else:
            for row, col in player1_x:
                scoreboard[row][col] = 'X'
            for row, col in player2_o:
                scoreboard[row][col] = 'O'
        return self.scoreboard_repr(scoreboard)
                
    

class New_Game:

    player1_moves = []
    player2_moves = []

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board(self)
    
    def check_win(self):
        win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]
            
        for path in win:
            if all(position in self.player1_moves for position in path):
                self.board.print_board()
                print(f'{self.player1} wins!')
                return True

            elif all(position in self.player2_moves for position in path):
                self.board.print_board()
                print(f'{self.player2} wins!')
                return True
        return False


    def make_move(self):
        mapping = {
            1 : [0, 0],
            2 : [0, 1],
            3 : [0, 2],
            4 : [1, 0],
            5 : [1, 1],
            6 : [1, 2],
            7 : [2, 0],
            8 : [2, 1],

            9 : [2, 2]
        }
        

        while True:
            
            #Player 1s turn if they have same amount of turns
            player1s_turn = len(self.player1_moves) == len(self.player2_moves)

            grid = int(input("From 1-9, which grid "))
            if (grid in mapping) and (grid not in self.player1_moves) and (grid not in self.player2_moves):
                if player1s_turn:
                    self.player1_moves.append(grid)
                    if self.check_win():
                        return False
                else:
                    self.player2_moves.append(grid)
                    if self.check_win():
                        self.board.print_board()
                        return False

                self.board.print_board()

            else:
                print("Not valid")
                self.make_move()
            


    

game = New_Game("Henrik", "Petter")
game.make_move()






