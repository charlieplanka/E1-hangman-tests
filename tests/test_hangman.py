import pytest


@pytest.mark.parametrize('letter', ['a', 'k', 'z'])
def test_check_letter_guessed(word, letter):
    '''
    Пользователь угадывает букву
    '''
    word._check_letter(letter)
    assert word._status == 'GUESSED'


@pytest.mark.parametrize('letter', ['o', 'x', 'p'])
def test_check_letter_wrong(word, letter):
    '''
    Пользователь вводит букву, которой нет в слове
    '''
    word._check_letter(letter)
    assert word._status == 'WRONG_LETTER'


@pytest.mark.parametrize('letter', ['aaaaaaaa', 'akz', ''])
def test_check_letter_not_single(word_empty, letter):
    '''
    Пользователь вводит больше/меньше, чем одну букву
    '''
    word_empty._check_letter(letter)
    assert word_empty._status == 'NOT_SINGLE_LETTER'


@pytest.mark.parametrize('letter', ['b', 'r', 'y'])
def test_check_letter_repetitive(word_repetitive, letter):
    '''
    Пользователь вводит букву, которая уже угадана
    '''
    word_repetitive._check_letter(letter)
    assert word_repetitive._status == 'REPETITIVE_LETTER'


def test_check_letter_not_letter():
    pass
