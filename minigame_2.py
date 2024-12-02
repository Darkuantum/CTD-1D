from TermControl import TermControl

level_1 = {
    1: ["blue", "sky"],
    2: ["fear", "dark", "death"],
    3: ["pear", "young", "dad", "ground"],
    4: ["cat", "moon", "car", "drink", "snow"],
    5: ["key", "dust", "drum", "jump", "bread", "grass"]
}

level_2 = {
    1: ["able","busy","elder","garlic","holy"],
    2: ["awkward","british","confused","feline","perfume"],
    3: ["burden","boolean","critic","murder","trashcan"],
    4: ["complex","shellfish","backspin","cobweb","hiccup"],
    5: ["velvet","magnet","enrich","hectic","banish"]
}

level_3 = {
    1: ["animal", "behavior", "confident" ], 
    2: ["accurate", "ambition", "businessman", "customer"],
    3: ["emphasis", "explorer", "forcible", "fertilize", "heritage" ],
    4: ["kangaroo", "liberate", "lithograph", "luminous", "loyalty"],
    5: ["maintenance", "nominate", "novelist", "numeric", "quintuplet"]
}

def challenge_player() -> dict:
    pass

def verify() -> bool:
    pass

def alzheimerGame() -> None:
    lives = 3
    isGameOver = False
    level = None

    tc = TermControl()

    while not isGameOver:
        print("Welcome to the Alzheimer game.")

        while level == None:
            dif = input("Please enter a number to choose the game difficulty you would like to play:\n\t1. Easy\n\t2. Medium\n\t3. Hard\n")

            if not dif.isdigit():
                print("\nYou have not entered a number.")
                tc.clearScreen()
                continue

            tc.changeColor(color="yellow")
            match int(dif):
                case 1:
                    level = level_1
                case 2:
                    level = level_2
                case 3:
                    level = level_3
                case _:
                    tc.clearScreen()
                    print("\nThat is not a valid difficulty.")
                    continue
            
            tc.resetColor()
            print("You have chosen difficulty {}.".format(dif))

        challenge_player()
        isInputCorrect = verify()

        isGameOver = True

        print("-" * 10)

def main() -> None:
    alzheimerGame()

if __name__ == "__main__":
    main()