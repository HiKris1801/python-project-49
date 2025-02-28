import prompt


def start_game(game_module):  # запуск игры
    print("Welcome to the Brain Games!")  # Приветствуем игрока
    user_name = prompt.string("May I have your name? ")  # Узнаем имя игрока
    print(f"Hello, {user_name}!")

    print(game_module.RULES)  # Показываем правила

    run_game_and_counter_answer(user_name, game_module)


def run_game_and_counter_answer(user_name, game_module):  # подсчет прав. ответов
    correct_answer = 0
    for _ in range(3):
        true_answer, question = game_module.generation_number()
        print(f"Question: {question}")
        answer_user = prompt.string('Your answer:')  # запрос ответа от игрока
        if answer_user.lower() == true_answer:  # проверяем правильность ответа
            correct_answer += 1
            print('Correct!')
        else:
            print(
                f'{answer_user} is wrong answer ;(. Correct answer was {true_answer}.\n Let\'s try again,{user_name} !')
            return
    if correct_answer == 3:  # Проверка, правильных ответов у игрока
        print(f'Congratulations, {user_name}!')

