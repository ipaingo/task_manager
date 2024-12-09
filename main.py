from usermanager import find_user, add_user, remove_user, get_userlist
from task import Task


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
            name = get_non_empty_input("Введите имя пользователя: ")
            add_user(name)
        elif choice == "2":
            # Удаление пользователя
            name = get_non_empty_input("Введите имя пользователя, которого хотите удалить: ")
            remove_user(name)
        elif choice == "3":
            # Добавление задачи
            name = get_non_empty_input("Введите имя пользователя, которому будет назначена задача: ")
            add_task(name)
        elif choice == "4":
            # Обновление задачи
            name = get_non_empty_input("Введите имя пользователя, задачу которого хотите обновить: ")
            update_task(name)
        elif choice == "5":
            # Удаление задачи
            name = get_non_empty_input("Введите имя пользователя, задачу которого хотите удалить: ")
            remove_task(name)
        elif choice == "6":
            # Вывод списка пользователей и задач
            get_userlist()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Добавление задачи
def add_task(name):
    user = find_user(name)
    if user:
        title = get_non_empty_input("Введите название задачи: ")
        description = get_non_empty_input("Введите описание задачи: ")

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
    else:
        print("Пользователь с таким именем не найден.")

# Функция для получения непустого ввода
def get_non_empty_input(prompt):
    """
    Запрашивает у пользователя ввод с проверкой на непустую строку.
    :param prompt: Сообщение для пользователя.
    :return: Введённая пользователем строка.
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("Ввод не может быть пустым. Попробуйте снова.")
        else:
            return value

# Обновление задачи
def update_task(name):
    user = find_user(name)
    if user:
        if not user.tasks:
            print("У пользователя нет задач.")
            return

        show_brief_task_list(user)

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
                execute_user_choice(task, update_choice)
            else:
                print("Некорректный номер задачи.")
        except ValueError:
            print("Некорректный ввод.")
    else:
        print("Пользователь не найден.")

def execute_user_choice(task, update_choice):
    if update_choice == "1":
        new_status = get_non_empty_input("Введите новый статус задачи: ")
        task.update_status(new_status)
        print("Статус задачи обновлен.")
    elif update_choice == "2":
        new_description = get_non_empty_input("Введите новое описание задачи: ")
        task.update_description(new_description)
        print("Описание задачи обновлено.")
    elif update_choice == "3":
        new_time = get_non_empty_input("Введите новое время выполнения задачи (HH:MM-HH:MM): ")
        task.update_time(new_time)
        print("Время выполнения задачи обновлено.")
    elif update_choice == "4":
        new_location = get_non_empty_input("Введите новое место выполнения задачи: ")
        task.update_location(new_location)
        print("Местоположение задачи обновлено.")
    elif update_choice == "5":
        new_status = get_non_empty_input("Введите новый статус задачи: ")
        new_description = get_non_empty_input("Введите новое описание задачи: ")
        new_time = get_non_empty_input("Введите новое время выполнения задачи (HH:MM-HH:MM): ")
        new_location = get_non_empty_input("Введите новое место выполнения задачи: ")
        task.update_all(new_status, new_description, new_time, new_location)
        print("Все параметры задачи обновлены.")
    else:
        print("Некорректный выбор.")

def show_brief_task_list(user):
    print("Список задач:")
    for i, task in enumerate(user.tasks, start=1):
        print(f"{i}. {task.title} - {task.status}")

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


if __name__ == "__main__":
    main()
