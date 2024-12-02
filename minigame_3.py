#from image import png
#import time

anxiety_level = {1:'low/nothing', 2:'some', 3:'anxious', 4:'social anxiety', 5:'full breakdown'}
current_anxiety = anxiety_level[2]

def anxiety(current_anxiety):
    a = current_anxiety
    if current_anxiety == 'full breakdown':
        return 'ending_1'

def ending_check(a):
    if a == 'full breakdown':
        return ending_1(a)
    elif a == 'social anxiety':
        return ending_2(a)
    elif a == 'anxious':
        return ending_3(a)
    elif a == 'some':
        return ending_4(a)
    elif a == "low/nothing":
        return ending_5(a)
    pass
    
def ending_1(a):
    return 'img_dead'

def ending_2(a):
    return 'img_isolated'

def ending_3(a):
    return 'img_struggles'

def ending_4(a):
    return 'img_fadedfeels'

def ending_5(a):
    return 'img_freedom'

def start_novel(start):
    return scene_1(current_anxiety)

def scene_1(current_anxiety): #first scene to introduce choices
    print("7 years. That's how long I've felt this anxiety for. Hasn't changed one bit during high school. University is just amping that up now.")
    print('img_scene1')
    print('Feels like everything might come crashing down now, what with this project we have to do. How on earth am I supposed to solve this while keeping myself sane?')
    print('1.' /n , '2.' /n , '3.')
    c = int(input('1, 2 or 3'))
    while c > 3 or c < 1:
        print('Invalid option, please select again from the options 1, 2 or 3.')
        c = int(input('1, 2 or 3'))   
    return choice_1(c)

def choice_1(c):
    if c == 1:
        global; current_anxiety = anxiety_level[3] #increase anxiety level by 1, move on to scene 2
        print('Anxiety Level:', current_anxiety)
        return scene_2(current_anxiety)
        #a = anxiety(current_anxiety)
        #if a == 'ending_1':
        #    return ending_1(current_anxiety)
    if c == 2:
        print('Anxiety Level:', current_anxiety)
        return scene_2(current_anxiety) #retain anxiety level, move on to scene 2
        #a = anxiety(current_anxiety)
        #if a == 'ending_1':
        #    return ending_1(current_anxiety)
    if c == 3:
        global; current_anxiety = anxiety_level[1] #decrease anxiety level by 1, move on to scene 2
        print('Anxiety Level:', current_anxiety)
        return scene_2(current_anxiety)
        #a = anxiety(current_anxiety)
        #if a == 'ending_1':
        #    return ending_1(current_anxiety)
        
    

def scene_2(current_anxiety): #first convo with someone
    print()