from player import Player
from game import Game, Mode

import map
import inventory
import input as game_input

game = Game()
player = Player()

print("======================")
print(" TRG, by Tal & Henri")
print("======================")
input("Press enter to begin")

print("Initializing map...")
game.map = map.parse_map(map.read_map())

# Game loop
while True:
    if game.mode == Mode.MAP:
        map.render_map(game, player)
    elif game.mode == Mode.INVENTORY:
        inventory.render_inventory(game, player)
    game_input.read_input(game, player)