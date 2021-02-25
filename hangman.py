import random

MAX_PENALTIES = 4
LETTER_SPACE = '_'
WORDS = [
    'skillfactory',
    'testing',
    'blackbox',
    'pytest',
    'unittest',
    'coverage',
    ]

# game statuses
WIN = 'WIN'
LOOSE = 'LOOSE'
GUESSED = 'GUESSED'
WRONG = 'WRONG_LETTER'
NOT_SINGLE = 'NOT_SINGLE_LETTER'
REPETITIVE = 'REPETITIVE_LETTER'


class Game:
    def __init__(self, word=''):
        self.ended = False
        self._word = word
        self._word_letters = set(word)
        self._guessed_letters = set()
        self._penalties = 0
        self._status = None

    def process_letter(self, letter):
        self._check_letter(letter)
        if self._status == GUESSED:
            self._guessed_letters.add(letter)
            self._check_win()
        elif self._status == WRONG:
            self._penalties += 1
            self._check_penalties()

        self._print_status_message()
        self.print_game_string()

    # добавить нечувствительность к регистру
    def _check_letter(self, letter):
        if len(letter) != 1:
            self._status = NOT_SINGLE
        elif letter in self._guessed_letters:
            self._status = REPETITIVE
        elif letter in self._word:
            self._status = GUESSED
        else:
            self._status = WRONG

    def _check_penalties(self):
        if self._penalties >= MAX_PENALTIES:
            self._status = LOOSE
            self.ended = True

    def _check_win(self):
        if self._guessed_letters == self._word_letters:  # возможно, есть лучший способ
            self._status = WIN
            self.ended = True

    def _print_status_message(self):
        if self._status == WIN:
            print('Вы отгадали слово!')
        elif self._status == LOOSE:
            print(f'Вы исчерпали лимит попыток — {MAX_PENALTIES}. Вы проиграли!')
        elif self._status == WRONG:
            print('Извините, такой буквы нет')
            print(f'Осталось попыток: {MAX_PENALTIES - self._penalties}')
        elif self._status == REPETITIVE:
            print('Эта буква уже открыта, попробуйте другую')
        elif self._status == NOT_SINGLE:
            print('Пожалуйста, введите ровно одну букву')

    def print_game_string(self):
        game_string = [letter if (letter in self._guessed_letters) else LETTER_SPACE for letter in self._word]
        print(*game_string)


def print_greeting():
    print('Добро пожаловать в игру «Виселица»! Ваша цель — отгадать все буквы в загаданном слове.')
    print('Вводите буквы с клавиатуры — по одной за раз.')
    print('Если вашей буквы нет в загадонном слове, вы получите штрафное очко.')
    print(f'Максимальное количество штрафных очков — {MAX_PENALTIES}. Если вы наберёте больше, игра закончится.')
    print('Дерзайте!')


def main():
    word = random.choice(WORDS)
    game = Game(word)
    print_greeting()
    game.print_game_string()
    while not game.ended:
        letter = input('\nУгадайте букву: ')
        game.process_letter(letter)


if __name__ == '__main__':
    main()
