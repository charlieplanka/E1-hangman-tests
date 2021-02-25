import pytest
from hangman import WIN, LOOSE, GUESSED, WRONG, NOT_SINGLE, REPETITIVE, MAX_PENALTIES


@pytest.mark.parametrize('letter', ['a', 'K', 'z'])
def test_process_letter_guessed(word, letter):
    '''
    Пользователь угадывает букву
    '''
    word.process_letter(letter)
    assert word._status == GUESSED
    assert letter.upper() in word._guessed_letters


@pytest.mark.parametrize('letter', ['o', 'X', 'p', '5', '@'])
def test_process_letter_wrong(word, letter):
    '''
    Пользователь вводит букву, которой нет в слове
    '''
    word.process_letter(letter)
    assert word._status == WRONG
    assert word._penalties == 1


@pytest.mark.parametrize('letter', ['aaaAaaAa', 'akz', ''])
def test_process_letter_not_single(word_empty, letter):
    '''
    Пользователь вводит больше/меньше, чем одну букву
    '''
    word_empty.process_letter(letter)
    assert word_empty._status == NOT_SINGLE


@pytest.mark.parametrize('letter', ['B', 'r', 'Y'])
def test_process_letter_repetitive(word_repetitive, letter):
    '''
    Пользователь вводит букву, которая уже угадана
    '''
    word_repetitive.process_letter(letter)
    assert word_repetitive._status == REPETITIVE


@pytest.mark.parametrize('letter', ['a', 'A'])
def test_process_letter_win(game_win, letter):
    '''
    Пользователь угадывает последнюю букву и выигрывает
    '''
    game_win.process_letter(letter)
    assert game_win._status == WIN
    assert letter.upper() in game_win._guessed_letters
    assert game_win.ended is True


@pytest.mark.parametrize('letter', ['a', 'B'])
def test_process_letter_loose(game_loose, letter):
    '''
    Пользователь вводит неверную букву, исчерпывает лимит попыток и проигрывает
    '''
    game_loose.process_letter(letter)
    assert game_loose._status == LOOSE
    assert game_loose._penalties == MAX_PENALTIES
    assert game_loose.ended is True
