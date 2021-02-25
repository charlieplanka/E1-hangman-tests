# Игра «Виселица»

[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/charlieplanka/E1-hangman-tests/master.png?style=flat-square

[build]: https://travis-ci.org/charlieplanka/E1-hangman-tests

Игра запускается в терминале. Игрок должен угадывать буквы в случайно загаданном слове, вводя их с клавиатуры по очереди. Цель игры — угадать все буквы и открыть слово полностью.
За каждую неправильно угаданную букву начисляется штрафное очко. При достижении максимального числа штрафных очков игра заканчивается.

![](https://i.imgur.com/REDBwzC.png)
  
---
К игре написаны юнит-тесты (**pytest** — 100% coverage), есть интеграция с **Travis CI**.

#### Как запустить игру (Windows)
1. Склонировать репозиторий и перейти в папку с ним.
```
git clone https://github.com/charlieplanka/E1-hangman-tests.git
cd E1-hangman-tests
```
2. Создать виртуальное окружение, активировать.
```
virtualenv venv
.\venv\Scripts\activate
```
3. Установить зависимости.
```
pip install -r requirements.txt
```
4. Запустить приложение.
```
python .\hangman.py
```
5. Чтобы запустить тесты, выполните команду:
```
python -m pytest
```
