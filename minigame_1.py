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
    "smoke_monster": {
        "qns_dict": {"Q1": "Is vaping is good for you?", "Q2": "Does vaping lead to nicotine addiction?", "Q3": "Is second-hand smoking hamrmful to non-smokers?", "Q4": "Does smoking increase the risk of heart disease?", "Q5": "Is nicotine-free vaping completely safe?"},
        "ans_dict": {"Q1": "no", "Q2": "yes", "Q3": "yes", "Q4": "yes", "Q5": "no"}
    },
    "gambling_monster": {
        "qns_dict": {"Q1": "Does gambling addiction affect a person's mental health?", "Q2": "Is it true that gambling can strain personal relationships?", "Q3": "Is online gambling always regulated and fair?", "Q4": "Are all forms of gambling completely free of risk?", "Q5": "Does gambling guarantee consistent financial gains?"},
        "ans_dict": {"Q1": "yes", "Q2": "yes", "Q3": "no", "Q4": "no", "Q5": "no"}
    },
    "alcohol_monster": {
        "qns_dict": {"Q1": "Can alcohol impair judgment and coordination?", "Q2": "Is it safe to drink alcohol during pregnancy?", "Q3": "Can binge drinking lead to alcohol poisoning?", "Q4": "Does moderate alcohol consumption pose no risks at all?", "Q5": "Does alcohol dehydrate the body?"},
        "ans_dict": {"Q1": "yes", "Q2": "no", "Q3": "yes", "Q4": "no", "Q5": "yes"}
    },
}
# debuff flag in the form of a dictionary lol 
debuff_dict = {'sight' : True}

def sight_debuff(question):
  '''this function implements a debuff in sight for the player by encrypting the question'''
  encrypted_question = ''
  for letter in question.lower():
    encrypted_question += encryption_dict.get(letter, letter)
  return input(encrypted_question)

'''
this portion is the introduction to the game
'''
'''
this portion is the instantiation of objects from the AddictionMonster class which will create a "monster" 
for 3 main vices - alcohol, gambling and smoking.
<addiction name> = new AddictionMonster()
'''


# List of monsters in order of battles
monster_names = ['gambling_monster', 'alcohol_monster', 'smoke_monster']

# Iterate through each monster and initiate the battles
for monster_name in monster_names:
    monster = am.AddictionMonster(monster_name)
    battle_won = monster.battle(qna, debuff_dict, sight_debuff)
    if not battle_won:
        print(f"You lost the battle against {monster_name}. Game Over.")
        break
    else:
        print(f"Congratulations! You defeated the {monster_name}. Moving on to the next battle...")
        time.sleep(3)
else:
    time.sleep(3)
    print("You have successfully beaten your addictions! You're free!")

    