def input_only_letters(prompt: str) -> str:
    """
    Запрашивает у пользователя ввод строки, содержащей только буквы и пробелы.

    Args:
        prompt (str): Текст запроса пользователю.

    Returns:
        str: Введённая пользователем строка.
    """
    while True:
        value = input(prompt).strip()
        if value.replace(" ", "").isalpha():  # Разрешаем пробелы, но без цифр
            return value
        else:
            print("Ошибка: введите только буквы (без цифр и спецсимволов)!")


def input_only_digits(prompt: str) -> int:
    """
    Запрашивает у пользователя ввод положительного числа.

    Args:
        prompt (str): Текст запроса пользователю.

    Returns:
        int: Введённое число.
    """
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)  # Преобразуем в число для удобства
        else:
            print("Ошибка: введите только цифры!")


def correct_years_word(years: int) -> str:
    """
    Определяет правильное слово для количества лет.

    Args:
        years (int): Количество лет.

    Returns:
        str: Слово "год", "года" или "лет" в зависимости от числа.
    """
    if 11 <= years % 100 <= 14:
        return "лет"
    elif years % 10 == 1:
        return "год"
    elif 2 <= years % 10 <= 4:
        return "года"
    else:
        return "лет"


# Запрашиваем у пользователя данные
name: str = input_only_letters("Введите ваше имя: ")
job: str = input_only_letters("Введите вашу профессию: ")
years_in_qa: int = input_only_digits("Сколько лет вы работаете в QA? ")

# Проверяем знания о переменной
answer_about_variable: str = input("Что такое переменная? ").strip().lower()
if any(word in answer_about_variable for word in ["хран", "содерж", "данн", "знач"]):
    print(f"\nОтлично, {name}! Похоже, вы понимаете, что такое переменная.")
else:
    print(f"\nКажется, вы еще не разобрались с переменными, {name}. Советуем почитать документацию.")

# Вывод итоговой информации
years_word: str = correct_years_word(years_in_qa)
print(f"\nИтоговая информация:")
print(f"Имя: {name}")
print(f"Профессия: {job}")
print(f"Стаж в QA: {years_in_qa} {years_word}.")


