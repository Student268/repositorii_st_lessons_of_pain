class game_engien:

    def choose_game(self) -> int:
        enter_game_name = input('В какую игру будем играть?\n 1 - угадывать \n 2 - загадывать\n')
        if enter_game_name == '1':
            self.start_game_houman_play()
        if enter_game_name == '2':
            self.start_game_computer_play()

    def start_game_houman_play(self) -> int:
        while True:
            print(self.fucking_number)
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

    def start_game_computer_play(self) -> int:
        while True:
            print(self.fucking_number)
            answer_houman = input('я угадал твое число?\n')
            if answer_houman == '<':
                self.fucking_number -= 1
            if answer_houman == '>':
                self.fucking_number += 1
            if answer_houman == '=':
                break