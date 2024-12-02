import AddictionMonster as am
'''
this portion consists of the relevant variables, data types and functions that are need for the object instantiation, 
namely: 
    - encryption dictionary 
    - question and answer (qna) dictionary 
    - debuff flag dictionary - used because the flag itself is only mutable inside of a dictionary 
    - sight debuff function 

'''
# encryption dictionary - required for the debuff function 
encryption_dict = {'a': '@', 'b': '6', 'c': '(', 'e': '€', 'f': '£', 'g': '&', 'i': '!', 'j': '?', 'k': '<', 'l': '1', 'o': '0', 'q': '9', 's': '$', 't': '7', 'v': '^', 'x': '*', 'y': '¥', 'z': '2'}
# question and answer dictionary with 3 levels of nesting 
qna = {
    "pp_monster": {
        "qns_dict": {"Q1": "AV is good for you"},
        "ans_dict": {"Q1": "yes"}
    },
    "smoke_monster": {
        "qns_dict": {"Q1": "Is vaping is good for you?"},
        "ans_dict": {"Q1": "no"}
    },
    "drug_monster": {
        "qns_dict": {"Q1": "Drugs are good for you"},
        "ans_dict": {"Q1": "yes"}
    },
    "gambling_monster": {
        "qns_dict": {"Q1": "How much do you want to gamble?"},
        "ans_dict": {"Q1": "yes"}
    },
    "alcohol_monster": {
        "qns_dict": {"Q1": "Alcohol is haram"},
        "ans_dict": {"Q1": "yes"}
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
this portion is the instantiation of objects from the AddictionMonster class which will create a "monster" 
for 3 main vices - alcohol, gambling and smoking.

<addiction name> = new AddictionMonster()

'''

### alcohol monster 

alcohol =  am.AddictionMonster('alcohol_monster')
alcohol.battle(qna, debuff_dict,sight_debuff)

smoking =  am.AddictionMonster('smoke_monster')
smoking.battle(qna, debuff_dict,sight_debuff)

gambling =  am.AddictionMonster('gambling_monster')
gambling.battle(qna, debuff_dict,sight_debuff)
