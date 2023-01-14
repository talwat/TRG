from shutil import get_terminal_size

"""
Clears the screen by printing a lot of new lines
"""
def clear():
    # Prints out a ton of new lines to clear the terminal, somehow is faster than os.system("clear") and minimizes flashing
    print("\n" * get_terminal_size().lines, end='\x1b[H')