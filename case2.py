import random

def guess_the_number():
    # Случайным образом выбираем число от 1 до 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Ограничиваем количество попыток

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")

    while attempts < max_attempts:
        try:
            # Запрашиваем у пользователя предположение
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            # Проверяем, было ли предположение правильным
            if guess < number_to_guess:
                print("Слишком маленькое число.")
            elif guess > number_to_guess:
                print("Слишком большое число.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    if attempts == max_attempts:
        print(f"Вы исчерпали все попытки. Загаданное число было {number_to_guess}.")

    # Добавляем запрос на ввод в конце программы, чтобы окно не закрывалось сразу
    input("Нажмите Enter, чтобы выйти из игры.")

# Запускаем игру
guess_the_number()