import pytest
from hangman import Game


@pytest.fixture
def word_empty():
    return Game()

# добавить тесты на проверку регистра
@pytest.fixture(params=['akz', 'azzaazkka', 'swachkdlzd'])
def word(request):
    return Game(request.param)


@pytest.fixture(params=[{'b', 'r', 'y'}, {'a', 'b', 's', 'r', 'y', 'z'}])
def word_repetitive(request):
    game = Game()
    game._guessed_letters = request.param
    return game
