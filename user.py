class User:
    def __init__(self, name):
        """
        Инициализация пользователя.
        :param name: Имя пользователя.
        """
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Добавляет задачу пользователю.
        Если задача с таким названием уже существует, она не будет добавлена.
        :param task: Объект задачи, который нужно добавить.
        """
        if self._is_task_duplicate(task):
            print(f"Задача с названием '{task.title}' уже существует и не может быть добавлена.")
        else:
            self.tasks.append(task)
            print(f"Задача \"{task.title}\" добавлена пользователю {self.name}.")

    def get_info(self):
        """
        Возвращает строку с информацией о пользователе и его задачах.
        :return: Строка с информацией о пользователе и списке его задач.
        """
        info = f"Пользователь: {self.name}\n     Задачи:\n"
        for task in self.tasks:
            info += task.get_info()
        return info

    def remove_task(self, title):
        """
        Удаляет задачу текущего пользователя по названию.
        :param title: Название задачи, которую нужно удалить.
        :return: True, если задача была удалена, False, если задача с таким названием не найдена.
        """
        task = self.find_task_by_title(title)
        if task:
            self.tasks.remove(task)
            print(f"Задача '{title}' успешно удалена.")
            return True
        print(f"Задача с названием '{title}' не найдена.")
        return False

    # Защищенные методы
    def find_task_by_title(self, title):
        """
        Находит задачу по названию.
        :param title: Название задачи.
        :return: Объект задачи, если найден, иначе None.
        """
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def _is_task_duplicate(self, task):
        """
        Проверяет, существует ли задача с таким же названием.
        :param task: Объект задачи.
        :return: True, если задача с таким названием уже существует, иначе False.
        """
        return any(t.title == task.title for t in self.tasks)
