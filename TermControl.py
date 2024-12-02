class TermControl:
    color = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }

    def __init__(self):
        pass

    def clearScreen(self):
        print("\033[2J", end="")

    def changeColor(self, color):
        print(self.color[color], end="")

    def resetColor(self):
        print("\033[0m", end="")

def main():
    tc = TermControl()
    print("Hello \033[31m world!")
    tc.resetColor()
    tc.changeColor(color="blue")
    print("Testing in blue")
    tc.resetColor()

if __name__ == "__main__":
    main()