import AddictionMonster as am
from TermControl import TermControl
import time
'''
variables, and data types required, namely: 
    - encryption dictionary 
    - question and answer (qna) dictionary 
    - debuff flag dictionary - used because the flag itself is only mutable inside of a dictionary 
    - sight debuff function 
'''
 
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

encryption_dict = {
    'a': '@',
    'b': '6',
    'c': '(',
    'e': '€',
    'f': '£',
    'g': '&',
    'i': '!',
    'j': '?',
    'k': '<',
    'l': '1',
    'o': '0',
    'q': '9',
    's': '$',
    't': '7',
    'v': '^',
    'x': '*',
    'y': '¥',
    'z': '2',
}

 
debuff_dict = {'sight' : True} # debuff flag in the form of a dictionary lol



tc = TermControl() # instance to change colour of text in terminal

def sightDebuff(question) -> str:
  '''applies a debuff by encrypting the question if needed'''
  encrypted_question = ''
  for letter in question.lower():
    encrypted_question += encryption_dict.get(letter, letter)
  return input(f'{encrypted_question}:\n').strip().lower()

# Iterate through each monster and initiate the battles
def addictionGame() -> None:
    monster_names = ['gambling_monster', 'alcohol_monster', 'smoke_monster'] # List of monsters in order of battles
    lives = 3
    for monster_name in monster_names:
        monster = am.AddictionMonster(monster_name)
        isBattleWon, lives = monster.battle(qna, debuff_dict, sightDebuff, lives)
        if not isBattleWon:
            if lives == 0:
                tc.changeColor("red")
                print("You have no more lives. Game Over.")
                tc.resetColor()
                break
        else:
            tc.changeColor("green")
            print(f"Congratulations! You defeated the {monster_name}. Moving on to the next battle...")
            tc.resetColor()
    else:
        tc.changeColor("yellow")
        print("You have successfully beaten all the monsters! You're free!")
        tc.resetColor()

def main() -> None:
    addictionGame()

if __name__ == "__main__":
    main()
    