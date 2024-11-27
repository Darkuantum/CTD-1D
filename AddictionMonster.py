### creating a class for the addiction monster battle ### 

class AddictionMonster:
    
    def __init__(self,name) -> None:
        self.name = name 
        self.monster_hp = 100 
        self.player_hp = 100   

    def battle(self, qna, debuff): ## qna and debuff can be functions that can be defined with minigame_1.py 
        '''this function sets the battle for the specific monster
            theres a dictionary debuff and a function debuff - need to find a way to make sure they don't conflict 
        '''
        # create separate dictionaries of the qns and answers 
        self.qns = qna[self.name]["qns_dict"]
        self.ans = qna[self.name]["ans_dict"]
        self.debuff_flag = False
        for i in range(len(1, self.qns)+1):
            self.question = self.qns['Q'+str(i)]
            if self.debuff_flag:
                self.player_ans = debuff(self.question)
            else:
                player_ans = input(self.question)
            




