import random 
import time

wins = 2 #reference based of nathan

easy = {
    1: ["blue", "sky"],
    2: ["fear", "dark", "death"],
    3: ["pear", "young", "dad", "ground"],
    4: ["cat", "moon", "car", "drink", "snow"],
    5: ["key", "dust", "drum", "jump", "bread", "grass"]
}

medium = {
    1: ["able","busy","elder","garlic","holy"],
    2: ["awkward","british","confused","feline","perfume"],
    3: ["burden","boolean","critic","murder","trashcan"],
    4: ["complex","shellfish","backspin","cobweb","hiccup"],
    5: ["velvet","magnet","enrich","hectic","banish"]
}

hard = {
    1: ["animal", "behavior", "confident" ], 
    2: ["accurate", "ambition", "businessman", "customer"],
    3: ["emphasis", "explorer", "forcible","fertilize", "heritage" ],
    4: ["kangaroo", "liberate", "lithograph", "luminous", "loyalty"],
    5: ["maintenance", "nominate", "novelist", "numeric", "quintuplet"]
}


def randomiser(difficulty):
    current_list = difficulty[wins+1]
    random.shuffle(current_list)
    return current_list
print(randomiser(easy))
      
def time(t):
    t=10
    while t:
        mins, secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format( mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
    return t
