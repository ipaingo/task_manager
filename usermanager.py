from user import User

users = []

def find_user(name):
    """
    Найти пользователя по имени.
    :param name: Имя пользователя.
    :return: Объект пользователя или None, если не найден.
    """
    for user in users:
        if user.name == name:
            return user
    return None

# Добавление пользователя
def add_user(name):
    if find_user(name):
        print("Пользователь с таким именем уже существует.")
    else:
        user = User(name)
        users.append(user)
        print(f"Пользователь {name} добавлен.")

# Удаление пользователя
def remove_user(name):
    user = find_user(name)
    if user:
        users.remove(user)
        print(f"Пользователь \"{name}\" успешно удалён.")
    else:
        print("Пользователь с таким именем не найден.")

# Вывод списка пользователей и задач
def get_userlist():
    if not users:
        print("Список пользователей пуст.")
    else:
        for user in users:
            print(f"\n{'=' * 20}\n{user.get_info()}")
