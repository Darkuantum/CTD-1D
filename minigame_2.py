from TermControl import TermControl
import random

level_1 = { #Nathan's Dictionary
    1: ["blue", "sky"],
    2: ["fear", "dark", "death"],
    3: ["pear", "young", "dad", "ground"],
    4: ["cat", "moon", "car", "drink", "snow"],
    5: ["key", "dust", "drum", "jump", "bread", "grass"]
}

level_2 = { #Ryan's Dictionary
    1: ["able","busy","elder","garlic","holy"],
    2: ["awkward","british","confused","feline","perfume"],
    3: ["burden","boolean","critic","murder","trashcan"],
    4: ["complex","shellfish","backspin","cobweb","hiccup"],
    5: ["velvet","magnet","enrich","hectic","banish"]
}

level_3 = { #Nathaniel's Dictionary
    1: ["animal", "behavior", "confident" ], 
    2: ["accurate", "ambition", "businessman", "customer"],
    3: ["emphasis", "explorer", "forcible", "fertilize", "heritage" ],
    4: ["kangaroo", "liberate", "lithograph", "luminous", "loyalty"],
    5: ["maintenance", "nominate", "novelist", "numeric", "quintuplet"]
}

def challenge_player(dictionary, numWins) -> dict:
    pass

def filter(response) -> list:
    invalid_symbols = ['!', ',', '@', '#', '%', "^", "*", '$', '&', '?', '.']
    response_list = response #define response_list is the same as response

    for i in invalid_symbols: #Sort out all the additional symbols for error
        response_list = response_list.replace(i, "") #sort and remove alll ineligible symbols 
    response_list = response_list.split() #take the response_list and split it based of the spaces " "
    return response_list
    
def verify(dictionary, numWins) -> bool:
    message_dict = { 
                1: "Zoom zoom, that just flew past you. I didn't see a thing?", 
                2: "Did you see that? Are you sure you can rememeber?",
                3: "Wow that's hella fast cuhhh",
                4: "Are you confident you can do this? Aren't you a bit demented?", 
                5: "Let it snow, let it snow, can't hold it back... oh you were watiting for me?",
                6: "I need you to focus 0.0", 
                7: "Why are you still here?",
                8: "I'm not sure if I remember what I saw...",
                9: "Ohhh man, I really couldn't remember what I saw...",
                10: "Bing bang bongo, I can't believe caught all that. Did you?"
    }

    message_choice = random.randint(1,10) #randomize the insult message
    print(message_dict[message_choice])
    response = input("What did you see?\n").lower() #lowercase the input
    cleaned_response = filter(response) #Send to clean the response 

    print('You responded with', cleaned_response) 

    if dictionary[numWins + 1] == cleaned_response: #check if the test_list == response_list is correct.
        return True #adjust this to the condition you are looking for
    else:
        return False #adjust this to the condition that you are looking for 
        
def alzheimerGame() -> None:
    lives = 3
    numWins = 0
    isGameOver = False
    difficulty = None

    tc = TermControl()

    print("Welcome to the Alzheimer memory word game.")
    while not isGameOver:
        while difficulty == None:
            choice = input("Please enter a number to choose the game difficulty you would like to play:\n\t1. Easy\n\t2. Medium\n\t3. Hard\n")

            if not choice.isdigit():
                print("\nYou have not entered a number.")
                tc.clearScreen()
                continue

            match int(choice):
                case 1:
                    difficulty = level_1
                case 2:
                    difficulty = level_2
                case 3:
                    difficulty = level_3
                case _:
                    tc.clearScreen()
                    print("\nThat is not a valid difficulty.")
                    continue
            
            tc.resetColor()
            print("You have chosen difficulty {}.".format(choice))

        challenge_player(difficulty, numWins)
        isInputCorrect = verify(difficulty, numWins)
        
        if not isInputCorrect:
            lives -= 1
            tc.changeColor("red")
            print("You just lost 1 life, your current lives is {}.".format(lives))
            tc.resetColor()
        else:
            numWins += 1
            tc.changeColor("green")
            print("You answered correctly, proceed to the next stage.")
            tc.resetColor()
        
        if lives == 0:
            isGameOver = True
            tc.changeColor("red")
            print("You have lost the game")
            tc.resetColor()
        elif numWins == 5:
            isGameOver = True
            tc.changeColor("yellow")
            print("You have won! Congratulations!")
            tc.resetColor()

def main() -> None:
    alzheimerGame()

if __name__ == "__main__":
    main()
