import random
import time
from TermControl import TermControl

tc = TermControl()

def number_memory_game():
    
    no_of_rand = 5 # number of numbers to memorize in Round 1
    lower_bound = 1
    upper_bound = 51 
    total_no = upper_bound - lower_bound # total number of numbers shown
    continue_game = True
    round = 1
    timer = 10 # amount of time given for player to memorize the numbers

    while continue_game and no_of_rand < total_no/2: # while continue_game == True and the number of numbers to memorize is less than half of the total number of number shown, the game continues

        number_list = generate_number_list(lower_bound, upper_bound) 
        rand_list = generate_rand_list(no_of_rand, lower_bound, upper_bound)
    
        print(f'Round {round}. {total_no} numbers will be shown, and \033[31m{no_of_rand}\033[0m of them will be shown in \033[31mred\033[0m. You are to memorise the numbers shown in red. You have {timer} seconds to memorise the numbers. Good luck!')

        for element in number_list: # for loop to print and display all the numbers in the number_list
            if element in rand_list:
                tc.changeColor("red")
                print(element, end = " ") # if the number is in the list of random numbers generated, the number will be printed in red colour
                tc.resetColor()
            else:
                print(element, end = " ") # else all other numbers will be printed in white colour

        countdown(timer, tc)
        tc.clearScreen()

        filtered_str = False
        while filtered_str == False: # while filtered_str == False, continue to ask the player for input
            user_answer_string = input('What were the numbers shown in red? Enter integers only and add a space after each number!')
            print('\n' + f'Your response: \033[94m{user_answer_string}\033[0m')
            filtered_str = check_if_valid(user_answer_string)

        user_answer_list = convert_str_to_list(filtered_str)
        continue_game = check_answer(user_answer_list, rand_list)
        print('-----------------------------------------')

        if continue_game:
            tc.changeColor("green")
            print('Congratulations, you have won this round!')
            tc.resetColor()
            print('-----------------------------------------')

            no_of_rand += 2 # as the player wins more rounds, the number of numbers to memorize will increase to increase the difficulty of the subsequent rounds
            round += 1

    if continue_game:
        tc.changeColor("green")
        print('Game over!')
        tc.resetColor()
        print(f'You have won {round - 1} rounds! Well done!')
    else:
        tc.changeColor("red")
        print('Game over!')
        tc.resetColor()
        print('The red numbers are {rand_list}. \nYou have lost this round :( \nYou have won {round - 1} round(s). Good job! Try better next time!')')


def generate_number_list(lower_bound, upper_bound): # create a list of integers running from lower_bound to upper_bound
    number_list = []
    for i in range(lower_bound, upper_bound):
        number_list.append(i)
    return number_list


def generate_rand_list(no_of_rand, lower_bound, upper_bound): # create a list of no_of_random random integers from a range of lower_bound to upper_bound
    rand_list = []
    while len(rand_list) < no_of_rand: # while loop to ensure the list of random numbers generated do not contain duplicates 
        rand_no = random.randint(lower_bound, upper_bound)
        if rand_no not in rand_list:
            rand_list.append(rand_no)
    return rand_list


def check_if_valid(str): # check if a string contains only numbers, 
    try: 
        if len(str) == 0:
            print('You have not enter any values. Please enter integers.')
            return False
        for i in str:
            if not(i.isnumeric() or i.isspace() or i == '.'): # check if the string character is not a number, a space or a period
                print('You have entered an invalid input. Please enter only numbers.')
                return False 
        return str
    
    except:
        print('You have entered an invalid input. Please enter only numbers.')
        return False


def convert_str_to_list(str): # create a list of floats from a string of numbers
    float_list = []
    str_list = str.split() # split str based on spaces and create a list of strings
    for string in str_list:
        string = float(string) # convert the strings in str_list to floats
        float_list.append(string)
    return float_list


def check_answer(user_answer, correct_answer): # check if player's response is correct
    if len(user_answer) != len(correct_answer):
        return False
    user_answer.sort()
    correct_answer.sort()
    for user, correct in zip(user_answer, correct_answer):
        if user != correct:
            return False
    return True


def countdown(t, tc):
    while t:
        mins, secs = divmod(t,60)
        timer ='{:02d}:{:02d}'.format( mins, secs)
        tc.changeColor('green')
        print(timer, end="\r")
        tc.resetColor()
        time.sleep(1)
        t -= 1


number_memory_game()