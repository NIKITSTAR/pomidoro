ticket = input("Введите номер билета: ")
if len(ticket) != 6 or not ticket.isdigit():
    print("Неверный формат билета. Введите ровно 6 цифр.")
else:
    first_half = ticket[:3]
    second_half = ticket[3:]
    sum_first = sum(int(digit) for digit in first_half)
    sum_second = sum(int(digit) for digit in second_half)
    if sum_first == sum_second:
        print("Результат: билет счастливый.")
    else:
        print("Результат: билет несчастливый.")
