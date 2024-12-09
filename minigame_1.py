import AddictionMonster as am
from TermControl import TermControl
'''
variables, and data types required, namely: 
    - encryption dictionary 
    - question and answer (qna) dictionary 
    - debuff flag dictionary - used because the flag itself is only mutable inside of a dictionary 
    - sight debuff function 
'''

'''
dictionary of questions and answers for each monster:
key : monster name 
value : list of tuples
    -   each tuple relates to one question, where the first element refers to the question, 
        while the second element refers to the correct answer for that question
'''
qna = {
    "Smoke Monster": [
        ("Is vaping is good for you?", "no"),
        ("Does vaping lead to nicotine addiction?", "yes"),
        ("Is second-hand smoking harmful to non-smokers?", "yes"),
        ("Does smoking increase the risk of heart disease?", "yes"),
        ("Is nicotine-free vaping completely safe?", "no"),
    ],
    "Gambling Monster": [
        ("Does gambling addiction affect a person's mental health?", "yes"),
        ("Is it true that gambling can strain personal relationships?", "yes"),
        ("Is online gambling always regulated and fair?", "no"),
        ("Are all forms of gambling completely free of risk?", "no"),
        ("Does gambling guarantee consistent financial gains?", "no"),
    ],
    "Alcohol Monster": [
        ("Can alcohol impair judgment and coordination?", "yes"),
        ("Is it safe to drink alcohol during pregnancy?", "no"),
        ("Can binge drinking lead to alcohol poisoning?", "yes"),
        ("Does moderate alcohol consumption pose no risks at all?", "no"),
        ("Does alcohol dehydrate the body?", "yes"),
    ],
}

''' 
dictionary where the letter in the alphabet (key) maps to its encrypted counterpart (value). 
used in sightDebuff() function.
'''

encryption_dict = {
    'a': '@',
    'b': '6',
    'c': '(',
    'e': '€',
    'f': '£',
    'g': '&',
    'i': '!',
    'j': '?',
    'k': '<',
    'l': '1',
    'o': '0',
    'q': '9',
    's': '$',
    't': '7',
    'v': '^',
    'x': '*',
    'y': '¥',
    'z': '2',
}

 
debuff_dict = {'sight' : True} # debuff flag in the form of a dictionary lol


tc = TermControl() # creates a Terminal Control object to control the terminal colors and to clear the screen

def sightDebuff(question) -> str:
  '''applies a debuff by encrypting the question if needed
    returns the a filtered '''
  encrypted_question = ''
  for letter in question.lower():
    encrypted_question += encryption_dict.get(letter, letter)
  return input(f'{encrypted_question}(yes/no):\n').strip().lower()

def gameStart() -> bool:
    '''this function prints the introduction and validates the input:

        returns : strictly a boolean value - True for yes or False for no  
    .'''
    intro_msg = input(
        "Welcome to Disgustingly Good.\n"
        "Here, you will be fighting against your vices - Alcohol, Smoking, and Gambling,\n"
        "so that you may be free of your addictions.\n"
        "Are you ready? (yes/no)\n"
    )
    if intro_msg[0] == 'y' or intro_msg[0] == 'Y':
        return True 
    else:
        return False 

# Iterate through each monster and initiate the battles
def addictionBattle() -> None:
    """
    Conducts a sequence of battles against addiction monsters using a while loop.
    The player wins if they defeat all 3 monsters (numWins == 3), and loses if they run out of lives
    
    returns: strictly None type - the function is to the game battle's logic. see comments below for explanation
    """
    monster_names = ['Gambling Monster', 'Alcohol Monster', 'Smoke Monster']  # List of monsters
    lives = 3  # Player starts with 3 lives
    numWins = 0  # Initialize win counter
    current_monster_index = 0  # Start with the first monster

    while lives > 0 and numWins < 3:
        # Get the current monster
        monster_name = monster_names[current_monster_index]
        monster = am.AddictionMonster(monster_name)

        # Start the battle
        isBattleWon, lives = monster.battle(qna, debuff_dict, sightDebuff, lives)

        # Check battle result
        if isBattleWon:
            numWins += 1
            tc.changeColor("green")
            print(f"Congratulations! You defeated the {monster_name}.")
            tc.resetColor()
        else:
            tc.changeColor("red")
            print(f"You lost the battle against {monster_name}.")
            tc.resetColor()

        # Move to the next monster or break
        current_monster_index += 1
        if current_monster_index >= len(monster_names):
            break

    # Game outcome
    if numWins == 3:
        tc.changeColor("yellow")
        print("You have successfully beaten all the monsters! You're free!")
        tc.resetColor()
    elif lives == 0:
        tc.changeColor("red")
        print("You have no more lives. Game Over.")
        tc.resetColor()
    else: 
        tc.changeColor("magenta")
        print(f"You beat {lives} out of {len(monster_names)} monsters.\n"
              "Nice job, but we know you can do better.\n"
              "Try again! (or don't, you have free will)."
              )
        tc.resetColor()

def addictionGame() -> None:
    ''' this fucntion is a validation check to see if the player is ready 
        used to execute gameStart(). 

        return: strictly a None type, goal is the execute the relevant functions in sequence
        if gameStart() returned True, execute the game with addictionBattle(). 
        else, print a funny message to try again 
     '''
    isPlayerReady = gameStart()
    if isPlayerReady:
        addictionBattle()
    else:
        print(
            "Seems like you actually aren't ready, or you can't type a simple yes or no without making a mistake,\n"
            "in which case you definitely aren't ready for this game.\n"
            "Try again."
            )

def main() -> None:
    '''
    main function to call addictionGame()
    '''
    addictionGame()

# conditional statement to check if name is main, and then esecute the main()
if __name__ == "__main__":
    main()
    