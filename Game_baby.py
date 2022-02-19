from random import randint
from game_engien import game_engien

class Game_baby(game_engien):
    def __init__(self):
        self.fucking_number = randint(0, 10)
        game_engien.choose_game(self)

    def __del__(self):
        print('Игра окончена')

computer_vs_human = Game_baby()


