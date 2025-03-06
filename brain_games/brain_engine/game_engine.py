import prompt


def start_game(game_module):  # запуск игры
    print("Welcome to the Brain Games!")  # Приветствуем игрока
    user_name = prompt.string("May I have your name? ")  # Узнаем имя игрока
    print(f"Hello, {user_name}!")

    print(game_module.RULES)  # Показываем правила

    run_game_and_counter_ans(user_name, game_module)


def run_game_and_counter_ans(user_name, game_module):  # подсчет прав. ответов
    correct_answer = 0
    for _ in range(3):
        true_ans, question = game_module.generation_number()
        print(f"Question: {question}")
        ans_user = prompt.string('Your answer:')  # запрос ответа от игрока
        if ans_user.lower() == true_ans:  # проверяем правильность ответа
            correct_answer += 1
            print('Correct!')
        else:
            print(
                f'{ans_user} is wrong answer ;(. Correct answer was {true_ans}')
            print(f'Let\'s try again, {user_name}!')
            return
    if correct_answer == 3:  # Проверка, правильных ответов у игрока
        print(f'Congratulations, {user_name}!')

