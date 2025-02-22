def input_only_letters(prompt):
        value = input(prompt)
        if value.isalpha():
            return value
        else:
            print("Ошибка: введите только буквы без пробелов и цифр")

def input_only_digits(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        else:
            print('Ошибка: введите цифры!')

name = input_only_letters("Введите ваше имя: ")
job = input_only_letters("Введите вашу профессию: ")
years_in_qa = input_only_digits("Сколько лет вы работаете в QA? ")
answer_about_variable = input_only_letters("Что такое переменная (введи только буквы без пробела)? ")
answer_lower = answer_about_variable.lower()
if "хран" in answer_lower or "содерж" in answer_lower or "данн" in answer_lower or "знач" in answer_lower:
    print(f"\nОтлично, {name}! Похоже, вы понимаете, что такое переменная.")
else:
    print(f"\nКажется, вы еще не разобрались с переменными, {name}. Советуем почитать документацию.")

print(f"\nИтого:\nИмя: {name}\nПрофессия: {job}\nСтаж в QA: {years_in_qa} лет(года).")

