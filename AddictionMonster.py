class AddictionMonster:
    def __init__(self, name, monster_hp=100, player_hp=100):
        """Initialize monster with name and health values."""
        self.name = name
        self.monster_hp = monster_hp
        self.player_hp = player_hp

    def battle(self, qna, debuff_dd, debuff_fn, lives):
        """
        Conducts a battle between the player and the monster.

        Parameters:
        - qna: Dictionary containing questions and answers for all monsters.
        - debuff_dd: Dictionary with the debuff flag.
        - debuff_fn: Function to apply the debuff if needed.
        - lives: Remaining player lives.

        Returns:
        - Tuple: (Boolean, int) -> (Did the player win this battle?, Remaining lives)
        """
        questions_and_answers = qna[self.name]
        
        print(f"Welcome to the {self.name} battle!")
        print("Answer 5 yes/no questions correctly to defeat the monster.\n")

        for question_text, correct_answer in questions_and_answers:
            # Apply debuff if active
            if debuff_dd['sight']:
                player_answer = debuff_fn(question_text)
            else:
                player_answer = input(f'{question_text}:\n').strip().lower()

            # Check the player's answer
            if player_answer == correct_answer:
                debuff_dd['sight'] = False  # Disable debuff on correct answer
                self.monster_hp -= 20
                print(f"Correct! Monster HP: {self.monster_hp}, Player HP: {self.player_hp}, Lives: {lives}")
            else:
                debuff_dd['sight'] = True  # Enable debuff on incorrect answer
                self.player_hp -= 25
                print(f"Wrong! Monster HP: {self.monster_hp}, Player HP: {self.player_hp}, Lives: {lives}")

            # Check if the monster is defeated
            if self.monster_hp <= 0:
                print(f"You defeated the {self.name}!")
                return True, lives

            # Check if the player loses all HP
            if self.player_hp <= 0:
                print("You lost all your HP in this battle.")
                break

        # If questions are exhausted or HP is 0, player loses a life
        lives -= 1
        if lives > 0:
            print(f"You lost the battle against {self.name}. Remaining lives: {lives}.")
        else:
            print("You are out of lives. Game Over!")

        return False, lives
