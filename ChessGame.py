class ChessGame:
    def __init__(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
        self.current_player = "white"
        self.move_history = []

    def play_game(self):
        while not self.checkmate():
            self.print_board()
            move = input(f"{self.current_player}'s move: ")
            if self.valid_move(move):
                self.make_move(move)
                self.move_history.append(move)
                if self.current_player == "white":
                    self.current_player = "black"
                else:
                    self.current_player = "white"
            else:
                print("Invalid move, try again.")

        print(f"Checkmate! {self.current_player} wins.")

    def print_board(self):
        print("   A B C D E F G H")
        print("  +---------------+")
        for i, row in enumerate(self.board):
            print(f"{8-i} | {' '.join(row)} | {8-i}")
        print("  +---------------+")
        print("   A B C D E F G H")

    def valid_move(self, move):
        # Check if move is valid
        return True

    def make_move(self, move):
        # Make the move
        pass

    def checkmate(self):
        # Check if there is a checkmate
        return False

game = ChessGame()
game.play_game()
