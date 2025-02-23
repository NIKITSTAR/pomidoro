def input_only_digits(prompt):
    while True:
        value = input(prompt)
        try:
            number = int(value)
        except ValueError:
            print('Ошибка: введите цифры!')
            continue

        if 0 <= number <= 120:
            print('Возраст принят')
            return number
        else:
            print('Некорректный возраст. Попробуйте снова.')


old = input_only_digits('Сколько вам лет? :')