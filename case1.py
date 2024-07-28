import math

def main():
    try:
        num = int(input("Введите положительное целое число: "))
        if num < 0:
            raise ValueError("Число должно быть положительным")
        
        # Использование библиотеки math для работы с большими числами
        result = math.factorial(num)
        print(f"Факториал числа {num} равен: {result}")

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    input("Нажмите Enter чтобы выйти")

if __name__ == "__main__":
    main()