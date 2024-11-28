import unittest
from main import *

class TestIntegration(unittest.TestCase):
    def setUp(self):
        """
        Подготовка тестовой среды. Очищаем список пользователей перед каждым тестом.
        """
        users.clear()

    def test_add_user_and_task(self):
        """Интеграционный тест добавления пользователя и задачи."""
        add_user("Иван")
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "Иван")

        user = users[0]
        task = Task("Задача 1", "Описание задачи", time="09:00-10:00", location="Офис")
        user.add_task(task)
        self.assertEqual(len(user.tasks), 1)
        self.assertEqual(user.tasks[0].title, "Задача 1")

    def test_find_and_remove_user(self):
        """Интеграционный тест поиска и удаления пользователя."""
        add_user("Мария")
        self.assertIsNotNone(find_user("Мария"))

        remove_user("Мария")
        self.assertIsNone(find_user("Мария"))
        self.assertEqual(len(users), 0)

    def test_create_and_update_task(self):
        """Интеграционный тест создания и обновления задачи."""
        add_user("Иван")
        user = find_user("Иван")

        # Создание задачи
        task = Task("Задача 1", "Описание задачи", time="09:00-10:00", location="Офис")
        user.add_task(task)
        self.assertEqual(len(user.tasks), 1)

        # Обновление задачи
        task.update_status("In Progress")
        self.assertEqual(user.tasks[0].status, "In Progress")

    def test_remove_task(self):
        """Интеграционный тест удаления задачи."""
        add_user("Мария")
        user = find_user("Мария")
        task = Task("Задача 1", "Описание задачи", time="09:00-10:00", location="Офис")
        user.add_task(task)

        # Удаляем задачу
        removed = user.remove_task("Задача 1")
        self.assertTrue(removed)
        self.assertEqual(len(user.tasks), 0)

    def test_get_userlist(self):
        """Интеграционный тест вывода списка пользователей и задач."""
        add_user("Иван")
        add_user("Мария")

        user_ivan = find_user("Иван")
        user_maria = find_user("Мария")

        user_ivan.add_task(Task("Задача 1", "Описание", time="09:00-10:00"))
        user_maria.add_task(Task("Задача 2", "Описание", time="10:00-11:00"))

        # Вывод списка пользователей
        get_userlist()

        # Проверяем, что список пользователей содержит нужную информацию
        self.assertEqual(len(users), 2)
        self.assertEqual(len(user_ivan.tasks), 1)
        self.assertEqual(len(user_maria.tasks), 1)


if __name__ == "__main__":
    unittest.main()
