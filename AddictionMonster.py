### creating a class for the addiction monster battle ### 

class AddictionMonster:
    
    def __init__(self,name,player_hp=370) -> None:
        self.name = name 
        self.monster_hp = 100 
        self.player_hp = player_hp

    def battle(self, qna, debuff_dd,debuff): ## qna and debuff can be functions that can be defined with minigame_1.py 
        '''this function sets the battle for the specific monster
           inputs : 
           qna - dictionary input 
           debuff_dict - flag to check if debuff needed. wrapped in dictionary to amke it mutable
           debuff - function to actually debuff if the player gets the question wrong 
        '''
        self.qns = qna[self.name]["qns_dict"]
        self.ans = qna[self.name]["ans_dict"]
        self.debuff_flag = False
        self.battle_won = False
        welcome_string = input(f'Welcome to the {self.name} battle! There are 5 yes/no questions with regards to the monster that you need to answer in order to defeat the {self.name}! Are you ready to meet your enemy?(yes/no):\n')
        if welcome_string == 'yes':
            for i in range(1, len(self.qns) +1):
                self.question_no = self.qns['Q'+str(i)] + ':' +  '\n'  
                if debuff_dd['sight']:
                    self.player_ans = debuff(self.question_no)
                else:
                    self.player_ans = input({self.question_no})
                self.player_ans = self.player_ans.lower()
                if self.player_ans == self.ans['Q'+ str(i)]:
                    self.monster_hp -= 20
                    print('monster hp: %d' % self.monster_hp)
                    print('player hp: %d' % self.player_hp)
                    if self.monster_hp == 0:
                        self.battle_won = True 
                        print("You won!")
                        return self.battle_won  # battle_win('smoking_monster')
                else:
                    self.player_hp -= 25
                    print('monster hp: %d' % self.monster_hp)
                    print('player hp: %d' % self.player_hp)
                    if self.player_hp == 0:
                        print("You lost!")
                        return self.battle_won # battle_win('smoking_monster')
        else:
            print("Come back when you are ready.")
                    
