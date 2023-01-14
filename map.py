import terminal
from game import Game
from player import Player
from type import Map

"""
Reads the map text file (data/map.txt)
"""
def read_map() -> str:
    with open("data/map.txt", "r") as file:
        content = file.read()
        return content.strip()


"""
Parses the map 
"""
def parse_map(raw_map: str) -> Map:
    parsed_map: Map = []

    lines = raw_map.split("\n")

    for line in lines:
        chars = list(line)

        parsed_map.append(chars)
    
    return parsed_map

"""
Renders the map and prints it to the screen
"""
def render_map(game: Game, player: Player):
    # Make copy of game map
    # Note that any modifications we make to 'map' will also apply to 'game.map' because of refrences
    map = game.map

    # Save previous tile
    previous_tile = map[player.coordinates[1]][player.coordinates[0]]

    # Plot the player
    map[player.coordinates[1]][player.coordinates[0]] = "i"

    # Calculate how to print the map
    map_to_print = ""

    for line in map:
        map_to_print += ''.join(line) + "\n"

    # After it's calculated, we put back the tile where the player use to be, so we don't have duplicates of the player
    # This is actually much faster than making a deep copy of 'game.map',
    # and we need this to be as fast as possible so the terminal doesn't flash
    map[player.coordinates[1]][player.coordinates[0]] = previous_tile
    
    # Clearing after we have already calculated the map to reduce the flashing,
    # so we can just display the old map while the new one is rendering.
    terminal.clear()
    print(map_to_print)