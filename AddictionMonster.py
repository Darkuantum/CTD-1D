### creating a class for the addiction monster battle ### 

class AddictionMonster:
    
    def __init__(self,name) -> None:
        self.name = name 
        self.monster_hp = 100 
        self.player_hp = 100   

    def battle(self, qna, debuff_dict,debuff): ## qna and debuff can be functions that can be defined with minigame_1.py 
        '''this function sets the battle for the specific monster
            theres a dictionary debuff and a function debuff - need to find a way to make sure they don't conflict 
        '''
        self.qns = qna[self.name]["qns_dict"]
        self.ans = qna[self.name]["ans_dict"]
        self.debuff_flag = False

        for i in range(len(1, self.qns) +1):
            self.question_no = self.qns['Q'+str(i)]
            if debuff_dict['debuff']:
                self.player_ans = debuff(self.question_no)
            else:
                self.player_ans = input(self.question_no)
            
            if self.player_ans.lower == self.ans[self.question_no]:
                monster_hp -= 20
                if monster_hp == 0:
                    return  'yay' # battle_win('smoking_monster')
            else:
                player_hp -= 25
                if player_hp == 0:
                    return 'nay' # battle_win('smoking_monster')


