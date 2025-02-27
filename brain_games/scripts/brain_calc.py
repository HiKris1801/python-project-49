from brain_games.brain_engine.game_engine import (
    start_game,  # Импортируем движок
)
from brain_games.brain_engine.games import calc  # Импортируем модуль игры


def main():  # Передаем модуль игры в движок
    start_game(calc)


if __name__ == "__main__":
    main()