from brain_games.brain_engine.game_engine import (
    start_game,  # Импортируем движок
)
from brain_games.brain_engine.games import prime  # Импортируем модуль игры


def main():  # Передаем модуль игры в движок
    start_game(prime)


if __name__ == "__main__":
    main()