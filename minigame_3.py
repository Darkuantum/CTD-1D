#from image import png

anxiety_level = {1:'low/nothing', 2:'some', 3:'anxious', 4:'social anxiety', 5:'full breakdown'}
current_anxiety = anxiety_level[3]


def anxiety(key):
    a = anxiety_level.get(key)
    return a

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