from TermControl import TermControl

tc = TermControl()
class AddictionMonster:
    def __init__(self, name, monster_hp=100, player_hp=100):
        """Initialize monster with name and health values."""
        self.name = name
        self.monster_hp = monster_hp
        self.player_hp = player_hp

    def battle(self, qna: dict, debuff_dd: dict, debuffFn, lives: int):
        """
        Conducts a battle between the player and the monster.

        Parameters:
        - qna: Dictionary containing questions and answers for all monsters.
        - debuff_dd: Dictionary with the debuff flag.
        - debuffFn: Function to apply the debuff if needed.
        - lives: Remaining player lives.

        Returns:
        - Tuple,Lives: (Boolean, int) -> (Did the player win this battle?, Remaining lives)
        """
        questions_and_answers = qna[self.name]

        print(f"Welcome to the {self.name} battle!")
        print("Answer 5 yes/no questions correctly to defeat the monster.\n")

        # number of questions available
        num_qns = len(qna)
        correct_answers = 0
        for question_text, correct_answer in questions_and_answers:
            # apply debuff if active
            if debuff_dd['sight']:
                player_answer = debuffFn(question_text)
            else:
                player_answer = input(f'{question_text}(yes/no):\n').strip().lower()

            # check if player's answer is valid (i.e. if it is 'yes' or 'no')
            # continuously ask the player for their answer if their input is invalid.
            valid = False
            while not valid:
                if player_answer == 'yes' or player_answer == 'no':
                    valid = True
                else:
                    tc.changeColor('red')
                    print("Your response is invalid. Please answer 'yes' or 'no'.")
                    tc.resetColor()
                    if debuff_dd['sight']:
                        player_answer = debuffFn(question_text)
                    else:
                        player_answer = input(f'{question_text}(yes/no):\n').strip().lower()

            # check the player's answer
            if player_answer == correct_answer:
                debuff_dd['sight'] = False  # disable debuff on correct answer
                self.monster_hp -= 20
                correct_answers += 1 
                print(f"Correct! Monster HP: {self.monster_hp}, Player HP: {self.player_hp}, Lives: {lives}")
            else:
                debuff_dd['sight'] = True  # enable debuff on incorrect answer
                self.player_hp -= 25
                print(f"Wrong! Monster HP: {self.monster_hp}, Player HP: {self.player_hp}, Lives: {lives}")

            # check if the monster is defeated
            if self.monster_hp <= 0:
                return True, lives

            # check if the player loses all HP
            if self.player_hp <= 0:
                print("You lost all your HP in this battle.")
                break

        # if questions are exhausted or HP is 0, player loses a life
        lives -= 1
        if lives > 0:
            tc.changeColor('yellow')
            print(f"You answered {correct_answers} out of {num_qns} questions correctly. Remaining lives: {lives}.")
            tc.resetColor()
        else:
            tc.changeColor('red')
            print("You are out of lives. Game Over!")
            tc.resetColor()

        return False, lives
