import random 
import time
from TermControl import TermControl # Self made class to control the terminal colors and clear the screen
from copy import deepcopy

# Creates a Terminal Control object to control the terminal colors and to clear the screen
tc = TermControl()

easy = { #Nathan's Dictionary
    1: ["blue", "sky"],
    2: ["fear", "dark", "death"],
    3: ["pear", "young", "dad", "ground"],
    4: ["cat", "moon", "car", "drink", "snow"],
    5: ["key", "dust", "drum", "jump", "bread", "grass"]
}

medium = { #Ryan's Dictionary
    1: ["able","busy","elder","garlic","holy"],
    2: ["awkward","british","confused","feline","perfume"],
    3: ["burden","boolean","critic","murder","trashcan"],
    4: ["complex","shellfish","backspin","cobweb","hiccup"],
    5: ["velvet","magnet","enrich","hectic","banish"]
}

hard = { #Nathaniel's Dictionary
    1: ["animal", "behavior", "confident" ], 
    2: ["accurate", "ambition", "businessman", "customer"],
    3: ["emphasis", "explorer", "forcible", "fertilize", "heritage" ],
    4: ["kangaroo", "liberate", "lithograph", "luminous", "loyalty"],
    5: ["maintenance", "nominate", "novelist", "numeric", "quintuplet"]
}

# Shuffle the prompt's word order,
# taking the difficulty dict and numWins int as arguments,
# and returning a shuffled list as output
def randomiser(difficulty, numWins) -> list:
    current_list = deepcopy(difficulty[numWins+1])
    random.shuffle(current_list)
    return current_list
      
# Timer counting down for the player to memorise the word order,
# before clearing the screen
def countdown(t) -> None:
    print("Memorize the order of the words before the timer runs out.")
    while t:
        mins, secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format( mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1

# Prints the correct prompts and displays the timer before clearing the screen
# and printing the shuffled prompts
def print_prompts(dictionary, numWins, timer) -> None:
    tc.changeColor("cyan")
    print(dictionary[numWins + 1])
    countdown(timer)
    tc.clearScreen()
    tc.changeColor("magenta")
    print(randomiser(dictionary, numWins))
    tc.resetColor()

# Cleans the user inputs by removing some invalid symbols
def filter(response) -> list:
    invalid_symbols = ['!', ',', '@', '#', '%', "^", "*", '$', '&', '?', '.', "'", '"', "-", "/"]
    response_list = response #define response_list is the same as response

    for i in invalid_symbols: #Sort out all the additional symbols for error
        response_list = response_list.replace(i, "") #sort and remove alll ineligible symbols 
    response_list = response_list.split() #take the response_list and split it based of the spaces " "
    return response_list
    
# Asks for user input and evaluates if the user input matches the correct prompt,
# will return a boolean based on wether it is True or False
def verify(dictionary, numWins) -> bool:
    message_dict = { 
                1: "Zoom zoom, that just flew past you. I didn't see a thing?", 
                2: "Did you see that? Are you sure you can remember?",
                3: "Wow that's hella fast cuhhh",
                4: "Are you confident you can do this? Aren't you a bit demented?", 
                5: "Let it snow, let it snow, can't hold it back... oh you were waiting for me?",
                6: "I need you to focus 0.0", 
                7: "Why are you still here?",
                8: "I'm not sure if I remember what I saw...",
                9: "Ohhh man, I really couldn't remember what I saw...",
                10: "Bing bang bongo, I can't believe I caught all that. Did you?"
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

# Main function of the module, implementing the global variables and the main game loop 
def alzheimerGame() -> None:
    lives = 3
    numWins = 0
    isGameOver = False
    difficulty = None
    timer = 0

    print("Welcome to the Alzheimer memory word game.")
    # Main game loop
    while not isGameOver:
        while difficulty == None:
            choice = input("Please enter a number to choose the game difficulty you would like to play:\n\t1. Easy\n\t2. Medium\n\t3. Hard\n")

            # Reject any choices that are not digits
            if not choice.isdigit():
                print("\nYou have not entered a number.")
                tc.clearScreen()
                continue
            
            # Sets the necessary variables for the game base on the chosen difficulty
            match int(choice):
                case 1:
                    difficulty = easy
                    timer = 10
                case 2:
                    difficulty = medium
                    timer = 8
                case 3:
                    difficulty = hard
                    timer = 5
                case _:
                    tc.clearScreen()
                    print("\nThat is not a valid difficulty.")
                    continue
            
            tc.resetColor()
            print("You have chosen difficulty {}.".format(choice))

        # Print the correct answers and with a countdown timer, then clears the screen and prints the shuffled words
        print_prompts(difficulty, numWins, timer)
        # Prompt the user to enter the correct words, and check them with the answers
        isInputCorrect = verify(difficulty, numWins)

        # Update game state such as lives and numWins based on correct or incorrect inputs 
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
        
        # Check if from the game state on whether the player has won or not, and will terminate the game
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