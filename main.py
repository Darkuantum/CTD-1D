from minigame_1 import addictionGame
from minigame_2 import alzheimerGame
from minigame_4 import number_memory_game

def main():
    print("Welcome to Team 07's app.")
    isExitApp = False
    
    while not isExitApp:
        choice = input("Choose a game to play by entering a number:\n\t1. Addiction Game\n\t2. Alzheimer Word Game\n\t3. Alzheimer Number Game\n\t4. Exit App\n")

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