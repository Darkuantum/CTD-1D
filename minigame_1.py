import AddictionMonster as am
import time
'''
this portion consists of the relevant variables, data types and functions that are need for the object instantiation, 
namely: 
    - lives 
    - encryption dictionary 
    - question and answer (qna) dictionary 
    - debuff flag dictionary - used because the flag itself is only mutable inside of a dictionary 
    - sight debuff function 
'''
# encryption dictionary - required for the debuff function 
encryption_dict = {'a': '@', 'b': '6', 'c': '(', 'e': '€', 'f': '£', 'g': '&', 'i': '!', 'j': '?', 'k': '<', 'l': '1', 'o': '0', 'q': '9', 's': '$', 't': '7', 'v': '^', 'x': '*', 'y': '¥', 'z': '2'}
# question and answer dictionary with 3 levels of nesting 
qna = {
    "smoke_monster": [
        ("Is vaping is good for you?", "no"),
        ("Does vaping lead to nicotine addiction?", "yes"),
        ("Is second-hand smoking harmful to non-smokers?", "yes"),
        ("Does smoking increase the risk of heart disease?", "yes"),
        ("Is nicotine-free vaping completely safe?", "no"),
    ],
    "gambling_monster": [
        ("Does gambling addiction affect a person's mental health?", "yes"),
        ("Is it true that gambling can strain personal relationships?", "yes"),
        ("Is online gambling always regulated and fair?", "no"),
        ("Are all forms of gambling completely free of risk?", "no"),
        ("Does gambling guarantee consistent financial gains?", "no"),
    ],
    "alcohol_monster": [
        ("Can alcohol impair judgment and coordination?", "yes"),
        ("Is it safe to drink alcohol during pregnancy?", "no"),
        ("Can binge drinking lead to alcohol poisoning?", "yes"),
        ("Does moderate alcohol consumption pose no risks at all?", "no"),
        ("Does alcohol dehydrate the body?", "yes"),
    ],
}

# debuff flag in the form of a dictionary lol 
debuff_dict = {'sight' : True}

def sight_debuff(question):
  '''this function implements a debuff in sight for the player by encrypting the question'''
  encrypted_question = ''
  for letter in question.lower():
    encrypted_question += encryption_dict.get(letter, letter)
  return input(f'{encrypted_question}:\n').strip().lower()

'''
this portion is the introduction to the game
'''
'''
this portion is the instantiation of objects from the AddictionMonster class which will create a "monster" 
for 3 main vices - alcohol, gambling and smoking.
<addiction name> = new AddictionMonster()
'''


# List of monsters in order of battles
# Initial lives
lives = 3

# List of monsters in order of battles
monster_names = ['gambling_monster', 'alcohol_monster', 'smoke_monster']

# Iterate through each monster and initiate the battles
for monster_name in monster_names:
    monster = am.AddictionMonster(monster_name)
    battle_won, lives = monster.battle(qna, debuff_dict, sight_debuff, lives)
    if not battle_won:
        if lives <= 0:
            print("You have no more lives. Game Over.")
            break
    else:
        print(f"Congratulations! You defeated the {monster_name}. Moving on to the next battle...")
else:
    print("You have successfully beaten all the monsters! You're free!")


    