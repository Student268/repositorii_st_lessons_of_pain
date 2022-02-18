from random import randint

class Game_baby:
    def __init__(self):
        self.fucking_number = randint(0, 10)
        print(self.fucking_number)
        self.start_game()

    def __del__(self):
        print('Игра окончена')

    def start_game(self) -> int:
        while True:
            human_enter_number = input('Вводи свое число, двуногое ничтожество\n')
            if human_enter_number.isnumeric() == False:
                print('Это не похоже на число, думал ты умеешь отличать цифры от букв')
            if int(human_enter_number) > 10:
                print('От 1 до 10, ты куда полез?')
            if int(human_enter_number) < 0:
                print('От 1 до 10, ты куда полез?')
            if int(human_enter_number) < self.fucking_number:
                print('это меньше, чем нужно')
            if int(human_enter_number) > self.fucking_number:
                print('это больше, чем нужно')
            if int(human_enter_number) == self.fucking_number:
                print('Молодец, кожанное недоразумение')
                break


computer_vs_human = Game_baby()
computer_vs_human.start_game()


