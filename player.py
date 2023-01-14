from game import Game

class Player:
    coordinates = [1, 0]
    hp = 20
    money = 100
    level = 1
    inventory = []

    def move_up(self, game: Game):
        if self.coordinates[1] <= 0:
            return

        self.coordinates[1] -= 1

    def move_down(self, game: Game):
        if self.coordinates[1] >= len(game.map) - 1:
            return

        self.coordinates[1] += 1

    def move_left(self, game: Game):
        if self.coordinates[0] <= 0:
            return

        self.coordinates[0] -= 1

    def move_right(self, game: Game):
        if self.coordinates[0] >= len(game.map[0]) - 1:
            return

        self.coordinates[0] += 1