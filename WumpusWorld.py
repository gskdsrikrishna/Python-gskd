class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.agent_location = (0, 0)
        self.wumpus_location = self.generate_random_location()
        self.gold_location = self.generate_random_location()
        self.pit_locations = [self.generate_random_location() for _ in range(size)]
        self.has_gold = False
        self.has_won = False
        self.has_died = False

    def generate_random_location(self):
        import random
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return x, y

    def move_agent(self, x, y):
        new_x = self.agent_location[0] + x
        new_y = self.agent_location[1] + y
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            self.agent_location = new_x, new_y

    def check_perceptions(self):
        perceptions = []
        x, y = self.agent_location

        if self.has_died:
            perceptions.append("You have been eaten by the Wumpus! Game over.")
            return perceptions

        if self.has_won:
            perceptions.append("Congratulations! You have found the gold and climbed out of the Wumpus World.")
            return perceptions

        if self.agent_location == self.gold_location:
            self.has_gold = True
            perceptions.append("You have found the gold!")
            return perceptions

        if self.agent_location == self.wumpus_location:
            self.has_died = True
            perceptions.append("You have been eaten by the Wumpus! Game over.")
            return perceptions

        if self.agent_location in self.pit_locations:
            self.has_died = True
            perceptions.append("You fell into a pit! Game over.")
            return perceptions

        if (x, y + 1) == self.wumpus_location or (x, y - 1) == self.wumpus_location or \
                (x + 1, y) == self.wumpus_location or (x - 1, y) == self.wumpus_location:
            perceptions.append("I smell a Wumpus!")

        if (x, y + 1) in self.pit_locations or (x, y - 1) in self.pit_locations or \
                (x + 1, y) in self.pit_locations or (x - 1, y) in self.pit_locations:
            perceptions.append("I feel a breeze!")

        return perceptions

    def execute_action(self, action):
        if action == 'left':
            self.move_agent(0, -1)
        elif action == 'right':
            self.move_agent(0, 1)
        elif action == 'up':
            self.move_agent(-1, 0)
        elif action == 'down':
            self.move_agent(1, 0)
        elif action == 'grab':
            if self.agent_location == self.gold_location:
                self.has_gold = True
                self.gold_location = None
        elif action == 'shoot':
            if self.agent_location == self.wumpus_location:
                self.has_won = True
        elif action == 'climb':
            if self.agent_location == (0, 0) and self.has_gold:
                self.has_won = True

    def print_perceptions(self, perceptions):
        print("\n".join(perceptions))

    def play(self):
        while not self.has_won and not self.has_died:
            perceptions = self.check_perceptions()
            self.print_perceptions(perceptions)

            print(f"Agent Location: {self.agent_location}")
            print(f"Gold Location: {self.gold_location}")
            print(f"Wumpus Location: {self.wumpus_location}")
            print(f"Pit Locations: {self.pit_locations}")

            action = input("Enter your action (left, right, up, down, grab, shoot, climb): ")
            self.execute_action(action)
            print("")

        if self.has_won:
            print("Congratulations! You have won!")
        elif self.has_died:
            print("Game over. You have lost.")


# Start the Wumpus World game
world = WumpusWorld(size=5)
world.play()