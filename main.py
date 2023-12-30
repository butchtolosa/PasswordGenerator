import random
import string

def generate_password(length=12):
    # Создаем набор символов, из которых будет генерироваться пароль
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль случайной длины из выбранных символов
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Введите желаемую длину пароля: "))
    generated_password = generate_password(password_length)
    print("Сгенерированный пароль:", generated_password)
