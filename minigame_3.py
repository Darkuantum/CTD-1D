anxiety_level = {1:'low/nothing', 2:'some', 3:'anxious', 4:'social anxiety', 5:'full breakdown'}



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
    
