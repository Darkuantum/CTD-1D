import random
from time import sleep
from TermControl import TermControl # Custom class to control the text colors and to clear the screen
from getpass import getpass

# Creates a Terminal Control object to control the text colors and to clear the screen
tc = TermControl()


# Create a list of integers running from lower_bound to upper_bound, with upper_bound not included
def generateNumberList(lower_bound, upper_bound) -> list:
    number_list = []
    for i in range(lower_bound, upper_bound):
        number_list.append(i)
    return number_list


# Create a list of (no_of_random) random integers from a range of lower_bound to upper_bound - 1, with upper_bound - 1 included
def generateRandList(no_of_rand, lower_bound, upper_bound) -> list: 
    rand_list = []
    # While loop to ensure the list of random integers generated do not contain duplicates 
    while len(rand_list) < no_of_rand: 
        rand_no = random.randint(lower_bound, upper_bound - 1) # generates a random integer between lower_bound and upper_bound, inclusive of lower_bound and exclusive of upper_bound
        if rand_no not in rand_list:
            rand_list.append(rand_no)
    return rand_list


# Check if a string contains only numbers and if the string is not empty,
# and replaces any instances of a comma to a spacing
def checkValid(str) -> str | bool:
    if len(str) == 0:
        print('You have not enter any values. Please enter integers.')
        return False
    
    str_copy = ''
    for character in str:
        if character == ',':
            str_copy += ' '
        elif not(character.isnumeric() or character.isspace() or character == '.'): # check if the string character is not a number, a space or a period
            print('You have entered an invalid input. Please enter only numbers.')
            return False  
        else:
            str_copy += character
    return str_copy


# Create a list of floats from a string of numerical characters
def convertStrToList(str) -> list:
    float_list = []
    str_list = str.split() # split str based on spaces and create a list of strings
    for string in str_list:
        string = float(string) # convert the strings in str_list to floats
        float_list.append(string)
    return float_list


# Check if the player's response matches the list of random integers
def checkAnswer(user_answer, correct_answer) -> bool: 
    if len(user_answer) != len(correct_answer):
        return False
    user_answer.sort()
    correct_answer.sort()
    for user, correct in zip(user_answer, correct_answer):
        if user != correct:
            return False
    return True


# Create a countdown of t seconds and display it 
def countdown3(t) -> None:
    while t:
        mins, secs = divmod(t, 60) # mins = t//60 | secs = t%60
        timer ='{:02d}:{:02d}'.format(mins, secs) # create a string containing the mins and secs, formmatted to two digits each
        tc.changeColor("green")
        print(timer, end = "\r") # display the timer at the start of the line
        tc.resetColor()
        sleep(1) # delay the loop by one second for the countdown
        t -= 1 


# Main function of the module, implementing the global variables and the main game loop 
def numberMemoryGame() -> None:
    tc.clearScreen()

    no_of_rand = 5 # number of integers to memorize in Round 1
    lower_bound = 1
    upper_bound = 51 
    total_no = upper_bound - lower_bound # total number of integers shown
    continue_game = True
    round = 1
    timer = 10 # amount of time given for player to memorize the numbers

    # Main game loop    
    while continue_game and no_of_rand < total_no/2: # while continue_game == True and the number of integers to memorize is less than half of the total number of integers shown, the game continues
   
        # Create a list of all numbers and a list of random numbers
        number_list = generateNumberList(lower_bound, upper_bound) 
        rand_list = generateRandList(no_of_rand, lower_bound, upper_bound)
    
        print(f'Round {round}. {total_no} numbers will be shown, and \033[31m{no_of_rand}\033[0m of them will be shown in \033[31mred\033[0m. \nYou are to memorise the numbers shown in red. You have {timer} seconds to memorise the numbers. \nAre you ready? The game will be starting soon, good luck!')
        sleep(5)

        # Display the integers, with the random integers displpayed in red and the others in white
        print("[", end = "  ")
        for element in number_list: # for loop to print and display all the numbers in the number_list
            if element in rand_list:
                tc.changeColor("red")
                print(element, end = "  ") # if the number is in the list of random numbers generated, the number will be printed in red colour
                tc.resetColor()
            else:
                print(element, end = "  ") # else all other numbers will be printed in white colour
        print("]")

        # Timer counting down for the player to memorise the numbers, 
        # before clearing the screen
        countdown3(timer)
        tc.clearScreen()
        getpass(prompt = 'Press ENTER to continue.') # to clear the terminal in the event the user types something in the terminal
        tc.clearScreen()

        # While loop to keep prompting the user for their input if it is invalid
        filtered_str = False
        while filtered_str == False: # while filtered_str == False, continue to ask the player for input
            user_answer_string = input('What were the numbers shown in \033[31mred\033[0m? Enter integers only and add a <space> to separate the numbers! \n')
            print('\n' + f'Your response: \033[94m[{user_answer_string}]\033[0m')
            filtered_str = checkValid(user_answer_string)

        user_answer_list = convertStrToList(filtered_str)
        continue_game = checkAnswer(user_answer_list, rand_list)

        tc.clearScreen()

        # If the user has answered correctly
        if continue_game:
            no_of_rand += 2 # as the user wins more rounds, the number of integers to memorize will increase to increase the difficulty of the subsequent rounds
            timer += 2 # as the total number of integers to memorize increases, the amount of time given for memorizing the numbers increases as well
            round += 1
            tc.changeColor("green")
            print(f'Congratulations, you are correct! Get ready, Round {round} is starting!')
            tc.resetColor()
            sleep(3)
        
    # If the user completes all the rounds
    if continue_game:
        tc.changeColor("green")
        print('Game over!')
        tc.resetColor()
        print(f"That's impressive! \nYou have won {round - 1} rounds! Well done!")
        sleep(5)
        tc.clearScreen()

    # If the game ends due to the user's answer being incorrect
    else:
        tc.changeColor("red")
        print('Game over!')
        tc.resetColor()
        print(f'The red numbers are \033[94m{rand_list}\033[0m. Your response was \033[34m{user_answer_list}\033[0m. \nYou have lost this round :( \nYou have won a total of {round - 1} round(s). Good job! Try better next time!')
        sleep(5)
        tc.clearScreen()


def main() -> None:
    numberMemoryGame()

if __name__ == "__main__":
    main()
