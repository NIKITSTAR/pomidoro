user_name = 'admin'
job = 'QA'
tool = 'Charles'

user_name_input = input("Введите ваше имя: ")
if not user_name_input:
    print("Имя не указано. Попробуйте снова!")
else:
    user_name = user_name_input
job_input = input("Введите вашу профессию: ")
if not job_input:
    print("Профессия не указана. Попробуйте снова!")
else:
    job = job_input
tool_input = input("Введите ваш любимый инструмент для тестирования: ")
if not tool_input:
    print("Инструмент не указан. Попробуйте снова!")
else:
    tool = tool_input

print(f"\nИтоговая информация о пользователе:\nИмя: {user_name}\nПрофессия: {job}\nЛюбимый инструмент для тестирования: {tool}")
