### creating a class for the addiction monster battle ### 

class AddictionMonster:
    
    def __init__(self,name) -> None:
        self.name = name 
        self.monster_hp = 100 
        self.player_hp = 100   

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

        for i in range(1, len(self.qns) +1):
            self.question_no = self.qns['Q'+str(i)] + ':' +  '\n'  
            if debuff_dd['sight']:
                self.player_ans = debuff(self.question_no)
            else:
                self.player_ans = input({self.question_no})
            
            if self.player_ans.lower == self.ans['Q'+ str(i)]:
                monster_hp -= 20
                if monster_hp == 0:
                    return  'yay' # battle_win('smoking_monster')
            else:
                player_hp -= 25
                if player_hp == 0:
                    return 'nay' # battle_win('smoking_monster')


