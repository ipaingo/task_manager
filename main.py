from user import User
from task import Task

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

# Добавление задачи
def add_task(name):
    user = find_user(name)
    if user:
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        # Проверка корректности времени
        while True:
            time = input("Введите время выполнения задачи (HH:MM-HH:MM) или оставьте пустым: ") or "Не указано"
            task = Task(title, description, time=time)  # Создаём временный объект Task для проверки времени
            if task.is_valid_time(time):  # Проверяем корректность времени
                break
            else:
                print("Некорректный формат времени. Пожалуйста, введите время в формате HH:MM-HH:MM.")
        location = input("Введите место выполнения задачи или оставьте пустым: ") or "Не указано"
        task = Task(title, description, time=time, location=location)
        user.add_task(task)
        print(f"Задача \"{title}\" добавлена пользователю {name}.")
    else:
        print("Пользователь с таким именем не найден.")

# Обновление задачи
def update_task(name):
    user = find_user(name)
    if user:
        if not user.tasks:
            print("У пользователя нет задач.")
            return

        print("Список задач:")
        for i, task in enumerate(user.tasks, start=1):
            print(f"{i}. {task.title} - {task.status}")

        try:
            task_index = int(input("Введите номер задачи для обновления: ")) - 1
            if 0 <= task_index < len(user.tasks):
                task = user.tasks[task_index]
                print("\nЧто вы хотите обновить?")
                print("1. Статус")
                print("2. Описание")
                print("3. Время выполнения")
                print("4. Местоположение")
                print("5. Все параметры")
                update_choice = input("Выберите действие: ")

                if update_choice == "1":
                    new_status = input("Введите новый статус задачи: ")
                    task.update_status(new_status)
                    print("Статус задачи обновлен.")
                elif update_choice == "2":
                    new_description = input("Введите новое описание задачи: ")
                    task.update_description(new_description)
                    print("Описание задачи обновлено.")
                elif update_choice == "3":
                    new_time = input("Введите новое время выполнения задачи (HH:MM-HH:MM): ")
                    task.update_time(new_time)
                    print("Время выполнения задачи обновлено.")
                elif update_choice == "4":
                    new_location = input("Введите новое место выполнения задачи: ")
                    task.update_location(new_location)
                    print("Местоположение задачи обновлено.")
                elif update_choice == "5":
                    new_status = input("Введите новый статус задачи: ")
                    new_description = input("Введите новое описание задачи: ")
                    new_time = input("Введите новое время выполнения задачи (HH:MM-HH:MM): ")
                    new_location = input("Введите новое место выполнения задачи: ")
                    task.update_all(new_status, new_description, new_time, new_location)
                    print("Все параметры задачи обновлены.")
                else:
                    print("Некорректный выбор.")
            else:
                print("Некорректный номер задачи.")
        except ValueError:
            print("Некорректный ввод.")
    else:
        print("Пользователь с таким именем не найден.")

# Удаление задачи
def remove_task(name):
    user = find_user(name)
    if user:
        if not user.tasks:
            print("У пользователя нет задач.")
            return

        print("Список задач:")
        for i, task in enumerate(user.tasks, start=1):
            print(f"{i}. {task.title} - {task.status}")

        try:
            task_index = int(input("Введите номер задачи для удаления: ")) - 1
            if 0 <= task_index < len(user.tasks):
                task = user.tasks[task_index]
                user.tasks.remove(task)  # Удаление задачи из списка
                print(f"Задача '{task.title}' успешно удалена.")
            else:
                print("Некорректный номер задачи.")
        except ValueError:
            print("Некорректный ввод.")
    else:
        print("Пользователь с таким именем не найден.")


# Вывод списка пользователей и задач
def get_userlist():
    if not users:
        print("Список пользователей пуст.")
    else:
        for user in users:
            print(f"\n{'=' * 20}\n{user.get_info()}")

def main():
    while True:
        print("\nTask Manager")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Создать задачу")
        print("4. Обновить задачу")
        print("5. Удалить задачу")
        print("6. Вывести список пользователей и задач")
        print("7. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            # Добавление пользователя
            name = input("Введите имя пользователя: ")
            add_user(name)
        elif choice == "2":
            # Удаление пользователя
            name = input("Введите имя пользователя, которого хотите удалить: ")
            remove_user(name)
        elif choice == "3":
            # Добавление задачи
            name = input("Введите имя пользователя, которому будет назначена задача: ")
            add_task(name)
        elif choice == "4":
            # Обновление задачи
            name = input("Введите имя пользователя, задачу которого хотите обновить: ")
            update_task(name)
        elif choice == "5":
            # Удаление задачи
            name = input("Введите имя пользователя, задачу которого хотите удалить: ")
            remove_task(name)
        elif choice == "6":
            # Вывод списка пользователей и задач
            get_userlist()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
