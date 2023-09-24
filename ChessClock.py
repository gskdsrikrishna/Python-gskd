#Chess Clock:
import time

class ChessClock:
    def __init__(self, time_per_player):
        self.time_per_player = time_per_player
        self.player1_time = time_per_player
        self.player2_time = time_per_player
        self.current_player = 1

    def start(self):
        while self.player1_time > 0 and self.player2_time > 0:
            self.display_time()
            self.countdown()
            self.switch_players()

        self.display_result()

    def countdown(self):
        start_time = time.time()
        while time.time() - start_time < self.time_per_player:
            self.display_time()
            time.sleep(1)
            if self.current_player == 1:
                self.player1_time -= 1
            else:
                self.player2_time -= 1

    def switch_players(self):
        self.current_player = 3 - self.current_player

    def display_time(self):
        print(f"Player 1: {self.player1_time} seconds")
        print(f"Player 2: {self.player2_time} seconds")
        print("-------------")

    def display_result(self):
        if self.player1_time <= 0:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

# Example usage: Chess clock with 60 seconds per player
clock = ChessClock(60)
clock.start()