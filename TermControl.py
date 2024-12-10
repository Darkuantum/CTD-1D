# A class to allow minigames to easily change the text font colour depending on the scenarios.
# The colours are changed using ASCII escape sequence in the terminal, along with additional
# functionalities to clear the terminal and reset the colours.

class TermControl:
    # Dictionary to store ASCII escape sequence for the common colours.
    color = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }

    # Constructor for the class, there is nothing to initialize so it is left empty.
    def __init__(self):
        pass

    # Prints the ASCII escape sequence to clear the terminal.
    def clearScreen(self):
        print("\033[2J", end="", flush=True)

    # Prints the ASCII escape sequence to change colours.
    def changeColor(self, color):
        print(self.color[color], end="", flush=True)

    # Prints the ASCII escape sequence to reset colours.
    def resetColor(self):
        print("\033[0m", end="", flush=True)

# Testing cases for the class when module is run as main file.
def main():
    tc = TermControl()
    print("Hello  world\033[31m!")
    tc.resetColor()
    tc.changeColor(color="blue")
    print("Testing in blue")
    tc.resetColor()

if __name__ == "__main__":
    main()
