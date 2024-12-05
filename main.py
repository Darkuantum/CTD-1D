# Importing all the different minigames as modules from the other python files.
from minigame_1 import addictionGame
from minigame_2 import alzheimerGame
from minigame_3 import number_memory_game

# Menu for the overall app, allows the user to choose which game to play, or to exit the app.
def main():
    print("Welcome to Team 07's app.")
    isExitApp = False

    # Main App loop
    while not isExitApp:
        choice = input("Choose a game to play by entering a number:\n\t1. Monster Battle Game\n\t2. Word Memory Game\n\t3. Number Memory Game\n\t4. Exit App\n")

        match choice:
            case "1":
                addictionGame()
            case "2":
                alzheimerGame()
            case "3":
                number_memory_game()
            case "4":
                isExitApp = True
            case _:
                print("That is not a valid input.")

if __name__ == "__main__":
    main()