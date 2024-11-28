import unittest
from main import *

class TestTaskManagerWithoutMocks(unittest.TestCase):
    def setUp(self):
        """
        Подготовка тестовой среды. Очищаем список пользователей перед каждым тестом.
        """
        global users
        users.clear()
        self.user1 = User("Иван")
        self.user2 = User("Мария")
        self.task1 = Task("Задача 1", "Описание 1", status="To Do", time="09:00-10:00", location="Офис")
        self.task2 = Task("Задача 2", "Описание 2", status="In Progress", time="10:00-11:00", location="Дом")

    def test_add_user_success(self):
        """Тест успешного добавления пользователя."""
        add_user("Иван")
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "Иван")

    def test_add_duplicate_user(self):
        """Тест добавления пользователя с существующим именем."""
        add_user("Иван")
        add_user("Иван")
        self.assertEqual(len(users), 1)

    def test_remove_user_success(self):
        """Тест успешного удаления пользователя."""
        users.append(self.user1)
        remove_user("Иван")
        self.assertEqual(len(users), 0)

    def test_remove_user_not_found(self):
        """Тест удаления несуществующего пользователя."""
        add_user("Иван")
        remove_user("Несуществующий")
        self.assertEqual(len(users), 1)

    def test_find_user_success(self):
        """Тест успешного поиска пользователя."""
        users.append(self.user1)
        result = find_user("Иван")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Иван")

    def test_find_user_not_found(self):
        """Тест поиска несуществующего пользователя."""
        result = find_user("Несуществующий")
        self.assertIsNone(result)

    def test_create_task_success(self):
        """Тест успешного создания задачи."""
        user = User("Иван")
        user.add_task(self.task1)
        self.assertEqual(len(user.tasks), 1)
        self.assertEqual(user.tasks[0].title, "Задача 1")

    def test_create_task_duplicate(self):
        """Тест добавления дублирующей задачи."""
        user = User("Иван")
        user.add_task(self.task1)
        user.add_task(self.task1)
        self.assertEqual(len(user.tasks), 1)

    def test_update_task_status(self):
        """Тест обновления статуса задачи."""
        self.user1.add_task(self.task1)
        self.user1.tasks[0].update_status("Completed")
        self.assertEqual(self.user1.tasks[0].status, "Completed")

    def test_remove_task_success(self):
        """Тест успешного удаления задачи."""
        self.user1.add_task(self.task1)
        self.user1.remove_task("Задача 1")
        self.assertEqual(len(self.user1.tasks), 0)

    def test_remove_task_not_found(self):
        """Тест удаления несуществующей задачи."""
        self.user1.add_task(self.task1)
        result = self.user1.remove_task("Несуществующая задача")
        self.assertFalse(result)
        self.assertEqual(len(self.user1.tasks), 1)

    def test_get_user_info(self):
        """Тест получения информации о пользователе."""
        self.user1.add_task(self.task1)
        self.user1.add_task(self.task2)
        info = self.user1.get_info()
        self.assertIn("Задача: Задача 1", info)
        self.assertIn("Задача: Задача 2", info)


if __name__ == "__main__":
    unittest.main()
