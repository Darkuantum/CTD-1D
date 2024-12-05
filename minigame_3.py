from time import sleep
import random

#change colours with number range of 0-50
#if wrong, instant game over (other idea: score system)

#display unit here
s = SenseHat() #for now use sensehat, later replace with actual device before submission
dd = {'easy': 'What numbers were red?', 'easy': 'Were there any numbers above 20?', 'easy': 'Input all the numbers in blue.'}
easy = ('easy', 51)
normal = ('medium', 71)
hard = ('hard', 100)
red = [255, 0, 0]
blue = [0, 0, 255]
yellow =  [255, 255, 0]
white = [255, 255, 255]


def difficulty_choice(easy, normal, hard):
    print('Choose difficulty level:')
    print('Easy Difficulty')
    print('Normal Difficulty')
    print('Hard Difficulty')
    difficulty = str(input('Enter your difficulty choice here.'))
    return difficulty


def create_list():
    ls = []
    for i in range(51):
        ls.append(i)
    return ls

def new_list(ls):
    
    random_ls = []
    # a = random.randint(0, 51)
    for i in random:
        if i in ls:
            random_ls.append(i)
            if len(random_ls) = 5:
                return random_ls

def display_colour(easy, normal, hard):
    difficulty = difficulty_choice(easy, normal, hard)
    ls = create_list(difficulty)
    random_ls = new_list(ls)
    print('You have 5 seconds to memorize this list:')
    s.show_message(str[ls], text_colour = red, back_colour = white)
    sleep(5)
    s.clear
    return choice(random_ls)

def choice(ls, dd, difficulty):
    if