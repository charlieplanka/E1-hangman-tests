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


class Game:
    def __init__(self, word):
        self.word = word
        self.ended = False
        self._word_letters = set(word)
        self._penalties = 0
        self._guessed_letters = set()

    def check_letter(self, letter):
        if len(letter) != 1:
            print('Пожалуйста, введите ровно одну букву')
        elif letter in self._guessed_letters:
            print('Эта буква уже открыта, попробуйте другую')
        elif letter in self.word:
            self._guessed_letters.add(letter)
            self._check_if_win()
        else:
            print('Извините, такой буквы нет')
            self._penalties += 1
            self._check_penalties()
        self.print_game_string()

    def print_game_string(self):
        game_string = [letter if (letter in self._guessed_letters) else LETTER_SPACE for letter in self.word]
        print(*game_string)

    def _check_penalties(self):
        if self._penalties >= MAX_PENALTIES:
            print(f'Вы исчерпали лимит попыток — {MAX_PENALTIES}. Вы проиграли!')
            self.ended = True
        else:
            print(f'Осталось попыток: {MAX_PENALTIES - self._penalties}')

    def _check_if_win(self):
        if self._guessed_letters == self._word_letters:
            print('Вы отгадали слово!')
            self.ended = True


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
        game.check_letter(letter)


if __name__ == '__main__':
    main()
