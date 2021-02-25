import pytest
from hangman import WIN, LOOSE, GUESSED, WRONG, NOT_SINGLE, REPETITIVE


@pytest.mark.parametrize('letter', ['a', 'k', 'z'])
def test_process_letter_guessed(word, letter):
    '''
    Пользователь правильно угадывает букву
    '''
    word.process_letter(letter)
    assert word._status == GUESSED
    assert letter in word._guessed_letters


@pytest.mark.parametrize('letter', ['o', 'x', 'p'])
def test_process_letter_wrong(word, letter):
    '''
    Пользователь вводит букву, которой нет в слове
    '''
    word.process_letter(letter)
    assert word._status == WRONG
    assert word._penalties == 1


@pytest.mark.parametrize('letter', ['aaaaaaaa', 'akz', ''])
def test_process_letter_not_single(word_empty, letter):
    '''
    Пользователь вводит больше/меньше, чем одну букву
    '''
    word_empty.process_letter(letter)
    assert word_empty._status == NOT_SINGLE


@pytest.mark.parametrize('letter', ['b', 'r', 'y'])
def test_process_letter_repetitive(word_repetitive, letter):
    '''
    Пользователь вводит букву, которая уже угадана
    '''
    word_repetitive.process_letter(letter)
    assert word_repetitive._status == REPETITIVE


def test_check_letter_not_letter():
    pass
