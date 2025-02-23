def input_only_digits(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print('Ошибка: введите цифры!')

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

test_cases_per_day = []
for day in days:
    cases = input_only_digits(f"Сколько тест-кейсов выполнено в {day}? ")
    test_cases_per_day.append(cases)

total_cases = sum(test_cases_per_day)
average_cases = total_cases / len(test_cases_per_day)

print(f"Общее количество: {total_cases}, среднее количество {average_cases}")
if average_cases > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")