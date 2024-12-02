#import time
import random

#change colours with number range of 0-50
#if wrong, instant game over (other idea: score system)



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
            #change colour of i in ls