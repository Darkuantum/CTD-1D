# Importing all the different minigames as modules from the other python files.
from minigame_1 import addictionGame
from minigame_2 import wordMemoryGame
from minigame_3 import numberMemoryGame

# Menu for the overall app, allows the user to choose which game to play, or to exit the app.
def main():

    print("Welcome 3 Hard and Irresistable Game!")
    isExitApp = False

    # Main app loop
    while not isExitApp:

        choice = input("Choose a game to play by entering the number:\n\t1. Monster Battle Game\n\t2. Word Memory Game\n\t3. Number Memory Game\n\t4. Exit App\n")

        match choice:
            case "1":
                addictionGame()
            case "2":
                wordMemoryGame()
            case "3":
                numberMemoryGame()
            case "4":
                isExitApp = True
            case _:
                print("Your input is invalid.")

if __name__ == "__main__":
    main()